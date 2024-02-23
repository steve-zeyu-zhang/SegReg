import ants
import numpy as np
import nibabel as nib
import os
import sys

# Load MRI and CT images
mri_image = ants.image_read("/gpfs/regist/case_" + sys.argv[1] +"_IMG_MR_T1.nii.gz")
ct_image = ants.image_read("/gpfs/regist/case_"+ sys.argv[1] +"_IMG_CT.nii.gz")

# Perform registration
registration = ants.registration(
    fixed=ct_image,
    moving=mri_image,
    type_of_transform=sys.argv[2],
)

# Apply the transformation to the MRI image
registered_mri = ants.apply_transforms(
    fixed=ct_image,
    moving=mri_image,
    transformlist=registration['fwdtransforms']
)

# Save the registered MRI image
ants.image_write(registered_mri, "/gpfs/output/case_"+ sys.argv[1] +".nii.gz")



# Load the registered MRI image using NiBabel
nib_registered_mri = nib.load("/gpfs/output/case_"+ sys.argv[1] +".nii.gz")


# Get the minimum and maximum intensity values from the original MRI image
min_intensity = mri_image.min()
max_intensity = mri_image.max()

# Adjust the intensity values of the registered MRI image
nib_registered_mri_data = nib_registered_mri.get_fdata()
nib_registered_mri_data[nib_registered_mri_data < min_intensity] = min_intensity
nib_registered_mri_data[nib_registered_mri_data > max_intensity] = max_intensity

# Create a new NiBabel Nifti1Image from the adjusted data
adjusted_image = nib.Nifti1Image(nib_registered_mri_data, affine=nib_registered_mri.affine)

# Save the adjusted image using NiBabel
nib.save(adjusted_image, "/gpfs/output/case_"+ sys.argv[1] +"_adjusted.nii.gz")