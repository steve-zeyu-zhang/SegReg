<div align="center"><h1> SegReg: Segmenting OARs by Registering MR Images and CT Annotations <br><sub><sup><a href="https://biomedicalimaging.org/2024/">ISBI 2024</a></sup></sub> </h1>



[Zeyu Zhang](https://steve-zeyu-zhang.github.io), [Xuyin Qi](https://www.linkedin.com/in/xuyin-q-29672524a/), [Bowen Zhang](https://www.adelaide.edu.au/directory/b.zhang), [Biao Wu](https://scholar.google.com/citations?user=Y3SBBWMAAAAJ&hl=en), [Hien Le](https://iconcancercentre.com.au/doctor/hien-le), [Bora Jeong](https://www.linkedin.com/in/bora-jeong-5a3177231/), [Zhibin Liao](https://researchers.adelaide.edu.au/profile/zhibin.liao), [Yunxiang Liu](https://www.adelaide.edu.au/directory/yunxiang.liu), [Johan Verjans](https://researchers.adelaide.edu.au/profile/johan.verjans), [Minh-Son To](https://www.flinders.edu.au/people/minhson.to), [Richard Hartley](http://users.cecs.anu.edu.au/~hartley/)<sup>✉</sup>


[![Website](https://img.shields.io/badge/Website-Demo-fedcba?style=flat-square)](https://steve-zeyu-zhang.github.io/SegReg) [![DOI](https://img.shields.io/badge/DOI-10.1109%2FISBI56570.2024.10635437-fcb520?style=flat-square&logo=doi)](https://doi.org/10.1109/ISBI56570.2024.10635437) [![arXiv](https://img.shields.io/badge/arXiv-2311.06956-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2311.06956) [![OpenReview](https://img.shields.io/badge/OpenReview-8c1b13?style=flat-square)](https://openreview.net/forum?id=rC8bmJoOOTC) [![Papers With Code](https://img.shields.io/badge/Papers%20With%20Code-555555.svg?style=flat-square&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgd2lkdGg9IjUxMiIgIGhlaWdodD0iNTEyIiA+PHBhdGggZD0iTTg4IDEyOGg0OHYyNTZIODh6bTE0NCAwaDQ4djI1NmgtNDh6bS03MiAxNmg0OHYyMjRoLTQ4em0xNDQgMGg0OHYyMjRoLTQ4em03Mi0xNmg0OHYyNTZoLTQ4eiIgc3Ryb2tlPSIjMjFDQkNFIiBmaWxsPSIjMjFDQkNFIj48L3BhdGg+PHBhdGggZD0iTTEwNCAxMDRWNTZIMTZ2NDAwaDg4di00OEg2NFYxMDR6bTMwNC00OHY0OGg0MHYzMDRoLTQwdjQ4aDg4VjU2eiIgc3Ryb2tlPSIjMjFDQkNFIiBmaWxsPSIjMjFDQkNFIj48L3BhdGg+PC9zdmc+)](https://paperswithcode.com/paper/segreg-segmenting-oars-by-registering-mr) [![BibTeX](https://img.shields.io/badge/BibTeX-Citation-eeeeee?style=flat-square)](https://steve-zeyu-zhang.github.io/SegReg/webpage/scholar.html)
</div>

_Organ at risk (OAR) segmentation is a critical
              process in radiotherapy treatment planning such as head and
              neck tumors. Nevertheless, in clinical practice, radiation oncologists 
              predominantly perform OAR segmentations manually
              on CT scans. This manual process is highly time-consuming
              and expensive, limiting the number of patients who can receive
              timely radiotherapy. Additionally, CT scans offer lower soft-tissue
              contrast compared to MRI. Despite MRI providing superior
              soft-tissue visualization, its time-consuming nature makes it
              infeasible for real-time treatment planning. To address these
              challenges, we propose a method called <b>SegReg</b>, which utilizes
              Elastic Symmetric Normalization for registering MRI to perform
              OAR segmentation. SegReg outperforms the CT-only baseline
              by <b>16.78%</b> in mDSC and <b>18.77%</b> in mIoU, showing that it
              effectively combines the geometric accuracy of CT with the
              superior soft-tissue contrast of MRI, making accurate automated
              OAR segmentation for clinical practice become possible._

![pipeline](webpage/pipeline.svg)

![demo](webpage/demo.svg)


## News

<b>(02/10/2024)</b> &#127881; Our paper has been accepted to <a href="https://biomedicalimaging.org/2024/"><b>ISBI 2024</b></a>!

<b>(02/07/2024)</b> 👉 Please see our latest work: <a href="https://steve-zeyu-zhang.github.io/Awesome-3D-Medical-Imaging-Segmentation/"><b>3D Medical Imaging Segmentation: A Comprehensive Survey</b></a> for latest updates on 3D medical imaging segmentation.

<b>(11/16/2023)</b> &#127881; Our paper has been promoted by <a href="https://wx.zsxq.com/dweb2/index/topic_detail/188418544524512"><b>CVer</b></a>.

## Citation

```
@inproceedings{zhang2024segreg,
  title={Segreg: Segmenting oars by registering mr images and ct annotations},
  author={Zhang, Zeyu and Qi, Xuyin and Zhang, Bowen and Wu, Biao and Le, Hien and Jeong, Bora and Liao, Zhibin and Liu, Yunxiang and Verjans, Johan and To, Minh-Son and others},
  booktitle={2024 IEEE International Symposium on Biomedical Imaging (ISBI)},
  pages={1--5},
  year={2024},
  organization={IEEE}
}
```

## Hardware
2 Intel Xeon Platinum 8360Y 2.40GHz CPUs, 8 NVIDIA A100 40G GPUs, and 256GB of RAM

## Environment

For docker container:

```
docker pull stevezeyuzhang/colab:1.7.1
```

For dependencies:

```
conda create -n segreg
```
```
conda activate segreg
```
```
conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=11.0 -c pytorch
```
```
cd SegReg/nnUNet
```
```
pip install -e .
```

```
export nnUNet_raw_data_base="/code/SegReg/DATASET/nnUNet_raw"
export nnUNet_preprocessed="/code/SegReg/DATASET/nnUNet_preprocessed" 
export RESULTS_FOLDER="/code/SegReg/DATASET/nnUNet_trained_models" 
```
```
source /root/.bashrc 
```

## Dataset

For dataset, see  https://han-seg2023.grand-challenge.org/

File directories as follows

```
├── SegReg
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
nnUNet_train 3d_fullres nnUNetTrainerV2 <TASK_ID> <FOLD>
```

### Inferencing

You can train your own model or find our checkpoint [here](https://github.com/steve-zeyu-zhang/SegReg/releases/download/SegReg/segreg_model_best.model).

```
nnUNet_predict -i /code/SegReg/DATASET/nnUNet_raw/nnUNet_raw_data/Task001_<TASK_NAME>/imagesTs -o /code/SegReg/DATASET/nnUNet_raw/nnUNet_raw_data/Task001_<TASK_NAME>/inferTs -t <TASK_ID> -m 3d_fullres -f <FOLD> -chk model_best
```

## Comparative Studies

- For [UaNet](https://doi.org/10.1038/s42256-019-0099-z), see branch [UaNet](https://github.com/steve-zeyu-zhang/SegReg/tree/UaNet)
- For [SepNet](https://doi.org/10.1016/j.neucom.2021.01.135), see branch [SepNet](https://github.com/steve-zeyu-zhang/SegReg/tree/SepNet)

## Ablation Studies

- For [MAML](https://doi.org/10.1007/978-3-030-87193-2_56), see branch [MAML](https://github.com/steve-zeyu-zhang/SegReg/tree/MAML)


## Acknowledgments

- [ANTsPy: Advanced Normalization Tools in Python](https://github.com/ANTsX/ANTsPy)
- [nnU-Net: A Self-Configuring Method for Deep Learning-based Biomedical Image Segmentation](https://github.com/MIC-DKFZ/nnUNet/tree/nnunetv1)
- [HaN-Seg: The head and neck organ-at-risk CT and MR segmentation dataset](https://han-seg2023.grand-challenge.org/)

Also thanks to the works we used in comparative studies:
- [UaNet: Clinically applicable deep learning framework for organs at risk delineation in CT images](https://github.com/uci-cbcl/UaNet)
- [SepNet: Automatic segmentation of organs-at-risk from head-and-neck CT using separable convolutional neural network with hard-region-weighted loss](https://github.com/HiLab-git/SepNet)
- [MAML: Modality-aware Mutual Learning for Multi-modal Medical Image Segmentation](https://github.com/YaoZhang93/MAML)

We would also like to express our sincere gratitude to [Dr. Yang Zhao](https://yangyangkiki.github.io/) for her genuine support of this work.

