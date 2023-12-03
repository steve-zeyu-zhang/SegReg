import os
import nibabel as nib
import numpy as np

nifti_image = nib.load("/code/Struct_NIIGZ/valid/case_39/Seg.nii.gz")

nifti_data = nifti_image.get_fdata()

print(nifti_data.shape)

print(np.unique(nifti_data))