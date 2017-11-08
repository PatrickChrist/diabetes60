# Diabetes60 Dataset
RGB-D images of 60 western dishes, home made. Data was recorded using a Microsoft Kinect V2. Feel free to read and cite our corresponding [paper](http://openaccess.thecvf.com/content_ICCV_2017_workshops/w22/html/Christ_Diabetes60_-_Inferring_ICCV_2017_paper.html).

## Raw dataset
The raw dataset contains 60 chunks of RGBD pairs of typical german dishes. Within the current version, there are some duplicate dishes, so there may be more than 60 scenes in total.
Download the raw dataset from [here](https://drive.google.com/drive/u/0/folders/0B0vscETPGI1-eXJDbFROd21XU2M).

## Python utilities
Use the utilities in python/utils.py to load the data. Basically, images are dumped in plain .npz format, whereas color has 4 channels (BGRA) and depth has 1 channel. The helper function in the python package removes the alpha channel by default and performs a barrel roll such that the channel format becomes RGB. The Kinect sensor typically records depth values in millimeters so you can divide the depth values by a factor of 1000 to obtain meters.

## Cite
``
@InProceedings{Christ_2017_ICCV,
author = {Ferdinand Christ, Patrick and Schlecht, Sebastian and Ettlinger, Florian and Grun, Felix and Heinle, Christoph and Tatavatry, Sunil and Ahmadi, Seyed-Ahmad and Diepold, Klaus and Menze, Bjoern H.},
title = {Diabetes60 - Inferring Bread Units From Food Images Using Fully Convolutional Neural Networks},
booktitle = {The IEEE International Conference on Computer Vision (ICCV)},
month = {Oct},
year = {2017}
}
``
