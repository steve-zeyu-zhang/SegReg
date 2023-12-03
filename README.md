# SepNet
For original repo, see [SepNet](https://github.com/HiLab-git/SepNet/tree/master)

#### Dataset

See [HaN-Seg](https://doi.org/10.1002/mp.16197)

#### Environment
Pytorch >= 1.4, SimpleITK >= 1.2, scipy >= 1.3.1, nibabel >= 2.5.0, PyTorch = 1.8.1, torchvision = 0.9.1, CUDA = 10.2
#### GPU
2 NVIDIA GeForce GTX 1080Ti 11G

#### Docker

```
docker pull qiyi007/sepnet:3.0
```

#### File Directory
```
.
|-- SepNet_OAR
|-- DATASET
    |-- train
        |-- case_01
            |-- <your image>.nii.gz
            |-- <your mask>.nii.gz
        |-- case_02
            |-- ...
        |-- ...
   
    |-- valid
        |-- case_xx
            |-- ...


```


#### Code
For Preprocessing

```
cd data_process
python Preprocess.py
```

For training, using Adam optimizer, lr = 1e<sup>-3</sup>, batch size = 4, epoch = 400

Change the `data_root` in `config/train.txt` to your data root;
```
python train.py
```

For inference

```
python Segmentation.py
```
Notise the you may need to padding Seg.nii.gz to keep consistent with the shape of your test data. See `padded.py` as an example.

