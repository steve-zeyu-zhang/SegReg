# MAML

For original repo, see [MAML](https://github.com/YaoZhang93/MAML)

## Environment

```
conda create -n maml
```
```
conda activate maml
```
```
conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=11.0 -c pytorch
```
```
cd MAMLFrame/nnUNet
```
```
pip install -e .
```

```
export nnUNet_raw_data_base="/code/MAMLFrame/DATASET/nnUNet_raw"
export nnUNet_preprocessed="/code/MAMLFrame/DATASET/nnUNet_preprocessed" 
export RESULTS_FOLDER="/code/MAMLFrame/DATASET/nnUNet_trained_models" 
```
```
source /root/.bashrc 
```

## Dataset

For dataset, see  https://han-seg2023.grand-challenge.org/

File directories as follows

```
├── MAMLFrame
│   ├── DATASET
│   │   ├── nnUNet_preprocessed
│   │   ├── nnUNet_raw
│   │   │   ├── nnUNet_cropped_data
│   │   │   └── nnUNet_raw_data
│   │   │   │   ├── Task001_<TASK_NAME>
│   │   │   │   │   ├── dataset.json
│   │   │   │   │   ├── imagesTr
│   │   │   │   │   │   ├── case_01_0000.nii.gz
│   │   │   │   │   │   ├── case_01_0001.nii.gz
│   │   │   │   │   │   ├── case_02_0000.nii.gz
│   │   │   │   │   │   ├── case_02_0001.nii.gz
│   │   │   │   │   ├── imagesTs
│   │   │   │   │   ├── inferTs
│   │   │   │   │   ├── labelsTr
│   │   │   │   │   │   ├── case_01.nii.gz
│   │   │   │   │   │   ├── case_02.nii.gz
│   │   │   │   │   └── labelsTs
│   │   └── nnUNet_trained_models
│   └── nnUNet
```

## Registration 

```
python register.py <INSTANCE_NUMBER> <TRANSFORMATION>
```

For transformation, see https://antspy.readthedocs.io/en/latest/registration.html

## Segmentation

### Data Preprocessing

```
nnUNet_plan_and_preprocess -t <TASK_ID>
```

### Training

```
nnUNet_train 3d_fullres MAMLTrainerV2 <TASK_ID> <FOLD>
```

### Inferencing

You can train your own model or find our checkpoint [here](https://github.com/steve-zeyu-zhang/SegReg/releases/download/MAML_checkpoint/maml_model_best.model).

```
nnUNet_predict -i /code/MAMLFrame/DATASET/nnUNet_raw/nnUNet_raw_data/Task001_<TASK_NAME>/imagesTs -o /code/MAMLFrame/DATASET/nnUNet_raw/nnUNet_raw_data/Task001_<TASK_NAME>/inferTs -t <TASK_ID> -m 3d_fullres -f <FOLD> -chk model_best
```
