# 手册

## 数据预备

*   进入 `./SJTU-AI-Circuit-Design-Contest-2019/utils/yoloconverter/` 目录下。

*   准备 `train_dataset` 和 `val_dataset` 目录下的 `images` 子文件夹，以及对应的 Reduced VOC 格式 `train_list.txt` 及 `val_list.txt` 文稿。
*   使用 Python 3 执行 `main.py` 脚本。按照要求回答图片路径、RVOC 文稿路径、以及输出 Index 文本文件路径。
*   看到 `done`，则说明数据预备阶段顺利完成。

## ~~K-Means 预备~~

*   ~~在完成数据预备步骤之后，应当得到位于 `./SJTU...2019/utils/yoloconverter/` 目录下的 `imp.py` 文件。将其拷贝到 `./kmeans` 文件夹下。~~
*   ~~运行 `./kmeans/main.py` 文件，得到所需的九组 K-Means 归化值。记在心里。~~

## 训练准备

*   把数据预备操作之后得到的数据目录移动到趁手的文件夹。
*   在 `voc.data` 文件中指定 yolo Index 文本文件的路径、分类的数量。
*   在 `voc.names` 文件中指定每一类的字符串名字。
*   ~~在 `./yolov3/cfg/` 目录下新建自己的配置文件，并将 `[yolo] anchors ` 下的值设定为上面得到的 K-Means 值。~~

## 开始训练

>   以下内容基于 PyTorch。

*   进入 `./yolov3` 目录。
*   使用 pip 或 Anaconda 安装 `requirements.txt` 中指定的依赖包。
*   执行 `python train.py` 来开始训练。
    *   用 `--data` 开关指定数据集的位置；
    *   用 `--cfg` 开关指定需要的配置文件位置；
    *   用 `--weight` 开关指定预训练权重文件的位置。
*   训练完成後，将得到的 `pt` 文件保留备用。

## 测试 & 验证

>   以下内容基于 PyTorch。

*   进入 `./yolov3` 目录。
*   调用 `test.py --weights weights/<pt-location>.pt` 脚本来对模型进行验证。

## 结果处理

*   将测试图片放置到 `./test` 目录下你喜欢的地方。
*   将测试结果文本文稿放置到 `./test` 目录下你喜欢的地方。
*   运行 `python normalization.py`，按照要求输入图片文件夹名和文本文件路径名。
*   回答想要把结果文件保存到哪里。
*   检查这个文本文件的内容。