# SegReg: Segmenting OARs by Registering MR Images and CT Annotations

[Zeyu Zhang](https://steve-zeyu-zhang.github.io)<sup>*</sup>, [Xuyin Qi](https://www.linkedin.com/in/xuyin-q-29672524a/), [Bowen Zhang](https://www.adelaide.edu.au/directory/b.zhang), [Biao Wu](https://scholar.google.com/citations?user=Y3SBBWMAAAAJ&hl=en), [Hien Le](https://iconcancercentre.com.au/doctor/hien-le), [Bora Jeong](https://www.linkedin.com/in/bora-jeong-5a3177231/), [Minh-son To](https://www.flinders.edu.au/people/minhson.to), [Richard Hartley](https://users.cecs.anu.edu.au/~hartley/)<sup>✉</sup>

<sup>*</sup>Contact: steve.zeyu.zhang@outlook.com

[![Web Page](https://img.shields.io/badge/Web%20Page-Demo-fedcba?style=flat-square)](https://steve-zeyu-zhang.github.io/SegReg) [![arXiv](https://img.shields.io/badge/arXiv-2311.06956-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2311.06956) [![Papers With Code](https://img.shields.io/badge/Papers%20With%20Code-555555.svg?style=flat-square&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgd2lkdGg9IjUxMiIgIGhlaWdodD0iNTEyIiA+PHBhdGggZD0iTTg4IDEyOGg0OHYyNTZIODh6bTE0NCAwaDQ4djI1NmgtNDh6bS03MiAxNmg0OHYyMjRoLTQ4em0xNDQgMGg0OHYyMjRoLTQ4em03Mi0xNmg0OHYyNTZoLTQ4eiIgc3Ryb2tlPSIjMjFDQkNFIiBmaWxsPSIjMjFDQkNFIj48L3BhdGg+PHBhdGggZD0iTTEwNCAxMDRWNTZIMTZ2NDAwaDg4di00OEg2NFYxMDR6bTMwNC00OHY0OGg0MHYzMDRoLTQwdjQ4aDg4VjU2eiIgc3Ryb2tlPSIjMjFDQkNFIiBmaWxsPSIjMjFDQkNFIj48L3BhdGg+PC9zdmc+)](https://paperswithcode.com/paper/segreg-segmenting-oars-by-registering-mr) [![BibTeX](https://img.shields.io/badge/BibTeX-Citation-eeeeee?style=flat-square)](https://steve-zeyu-zhang.github.io/SegReg/webpage/scholar.html)

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

### Code coming soon.

## News

<b>(11/16/2023)</b> &#127881; Our paper has been promoted by <a href="https://wx.zsxq.com/mweb/views/topicdetail/topicdetail.html?topic_id=188418544524512&inviter_id=585252854845544&share_from=ShareToWechat&keyword=1499f4d11 ">CVer</a>

## Hardware
2 Intel Xeon Platinum 8360Y 2.40GHz CPUs, 8 NVIDIA A100 40G GPUs, and 256GB of RAM

## Citation

```
@article{zhang2023segreg,
  title={SegReg: Segmenting OARs by Registering MR Images and CT Annotations},
  author={Zhang, Zeyu and Qi, Xuyin and Zhang, Bowen and Wu, Biao and Le, Hien and Jeong, Bora and To, Minh-Son and Hartley, Richard},
  journal={arXiv preprint arXiv:2311.06956},
  year={2023}
}
```

## Comparative Studies

- For [UaNet](https://doi.org/10.1038/s42256-019-0099-z), see branch [UaNet](https://github.com/steve-zeyu-zhang/SegReg/tree/UaNet)
- For [SepNet](https://doi.org/10.1016/j.neucom.2021.01.135), see branch [SepNet](https://github.com/steve-zeyu-zhang/SegReg/tree/SepNet)
