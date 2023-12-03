import nibabel as nib
import numpy as np
import os

def pad_and_save_mri(ct_path, mri_path, output_path):
    # Load the CT and MRI images
    ct_image = nib.load(ct_path)
    mri_image = nib.load(mri_path)

    # Get the image data as a NumPy array
    mri_data = mri_image.get_fdata()
    desired_size = ct_image.get_fdata().shape
    og_shape = mri_data.shape

    # Get the minimum pixel value in the MRI image
    min_pixel_value = mri_data.min()

    # Create an empty array for the padded MRI
    padded_mri = np.full(desired_size, min_pixel_value)

    # Calculate the padding sizes
    pad_x = (desired_size[0] - og_shape[0]) // 2
    pad_y = (desired_size[1] - og_shape[1]) // 2
    pad_z = (desired_size[2] - og_shape[2]) // 2

    # Copy the original MRI data to the center of the padded array
    padded_mri[pad_x:pad_x + og_shape[0], pad_y:pad_y + og_shape[1], pad_z:pad_z + og_shape[2]] = mri_data

    # Create a new Nifti1Image with the padded data
    padded_image = nib.Nifti1Image(padded_mri.astype(np.uint8), affine=ct_image.affine)

    # Save the padded image
    nib.save(padded_image, output_path)

# Define the paths and iterate over the cases
ct_template = "/code/niigz/imagesTs/case_{:02d}_0000.nii.gz"
mri_template = "/code/Struct_NIIGZ/valid/case_{:02d}/Seg.nii.gz"
output_template = "/code/Struct_NIIGZ/valid/case_{:02d}_padded.nii.gz"

for case_num in range(39, 43):  # This will go from 39 to 42
    ct_path = ct_template.format(case_num)
    mri_path = mri_template.format(case_num)
    output_path = output_template.format(case_num)
    
    # Check if files exist before processing
    if os.path.exists(ct_path) and os.path.exists(mri_path):
        pad_and_save_mri(ct_path, mri_path, output_path)
    else:
        print(f"Files for case {case_num} do not exist.")
