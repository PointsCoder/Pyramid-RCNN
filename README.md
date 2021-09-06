# Pyramid R-CNN

This is a reproduced repo of Pyramid R-CNN for 3D object detection. 

The code is mainly based on [OpenPCDet](https://github.com/open-mmlab/OpenPCDet).

## Introduction
We provide code and training configurations of Pyramid-V/PV on the KITTI and Waymo Open dataset. Checkpoints will not be released. The dataset organization is same with PCDet. 

## Requirements
The codes are tested in the following environment:
* Ubuntu 18.04
* Python 3.6
* PyTorch 1.5
* CUDA 10.1
* OpenPCDet v0.3.0
* spconv v1.2.1

## Installation
a. Clone this repository.
```shell
git clone https://github.com/PointsCoder/Pyramid_R-CNN.git
```

b. Install the dependent libraries as follows:

* Install the dependent python libraries: 
```
pip install -r requirements.txt 
```

* Install the SparseConv library, we use the implementation from [`[spconv]`](https://github.com/traveller59/spconv). 
    * If you use PyTorch 1.1, then make sure you install the `spconv v1.0` with ([commit 8da6f96](https://github.com/traveller59/spconv/tree/8da6f967fb9a054d8870c3515b1b44eca2103634)) instead of the latest one.
    * If you use PyTorch 1.3+, then you need to install the `spconv v1.2`. As mentioned by the author of [`spconv`](https://github.com/traveller59/spconv), you need to use their docker if you use PyTorch 1.4+. 

c. Compile CUDA operators by running the following command:
```shell
python setup.py develop
```

## Training

We train all the models with 8 Tesla V100 GPU (32Gb), and all the configs (epochs/learning rate/batch size) are for 8-GPU Distributed Data Parallel (DDP) training.
Users may change those training parameters if they want to run with different GPU numbers and memories. 

* models
```shell script
# pyramid_rcnn_pv.yaml: pyramid roi head on the point-voxel backbone
# pyramid_rcnn_v.yaml: pyramid roi head on the spconv u-net backbone
```

* DDP training
```shell script
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 sh scripts/dist_train.sh 8 --cfg_file cfgs/waymo_models/pyramid_rcnn_pv.yaml
```

* DDP testing
```shell script
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 sh scripts/dist_test.sh 8 --cfg_file cfgs/waymo_models/pyramid_rcnn_pv.yaml --eval_all
```

## Citation 
If you find this project useful in your research, please consider cite:

```
@article{mao2021pyramid,
  title={Pyramid R-CNN: Towards Better Performance and Adaptability for 3D Object Detection},
  author={Mao, Jiageng and Niu, Minzhe and Bai, Haoyue and Liang, Xiaodan and Xu, Hang and Xu, Chunjing},
  journal={ICCV},
  year={2021}
}
```