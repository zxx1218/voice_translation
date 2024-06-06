# 基于深度学习的中文语音识别模型（支持wav、mp4、m4a等所有格式音频上传）

## 前言

&emsp;&emsp;该开源项目旨在提供一个能够自动检测并识别中文语音的模型，支持wav、mp4、m4a等格式的音频文件上传。无论是从录音设备中获取的wav文件，还是从视频中提取的mp4、m4a文件，我们的模型可以准确识别其中的中文文字内容。通过集成最先进的语音识别技术和深度学习算法，我们的模型能够快速、准确地将声音转换为文字，为用户提供便捷的语音识别体验。

主要功能：

1. 支持多种常见音频格式，包括wav、mp4、m4a等。
2. 实现中文语音自动检测和识别，识别准确率高。
3. 提供简单易用的接口，方便开发者集成到自己的应用程序中。

<hr>


## :sparkles: 中文音频测试：

1. 测试音频文件下载（提供一个.m4a格式的中文人声音频）：

```
百度网盘分享的文件
链接：https://pan.baidu.com/s/1G4TxBwAFO2va34H7AY5iYQ?pwd=plmg 
提取码：plmg
```

2. 下载预训练模型文件并放在指定目录文件下

```
百度网盘分享的文件
链接：https://pan.baidu.com/s/1Db0rSxh7cgsVG1-w7Uc0bw?pwd=touc 
提取码：touc
```

下载model文件后，内含三个model开头的.pt文件，请将`model_Ct_punc.pt`文件`_Ct_punc`部分删除后（即文件名改为model.pt）放在`Ct_punc`文件目录下。

同理将另外两个带后缀的模型下载后删除`_Ct_punc`部分后分别放在其对应的文件目录下

2. 环境配置（推荐使用conda安装环境）

```
# 从github上Clone项目
git clone https://github.com/zxx1218/voice_translation.git

# 使用conda创建环境
conda create -n py310 python=3.10
conda activate py310

# cd到算法根目录下
cd speech_recognition

# 在根目录下安装依赖
pip install -r requirements.txt
```

如果您的显卡支持cuda 11.7及以上，可以直接使用conda导出的yaml文件一次性安装全部环境

```
# cd到算法根目录下
cd speech_recognition

# 安装conda导出的环境
conda env create -f environment.yml

# 激活环境
conda activate modelscope
```

3. 测试音频文件准备好后放在`speech_recognition/datasets`目录下，然后开始执行测试，识别结果将打印在控制台

```
python voice_translation_test.py
```

测试音频截图👇
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/8e959d160359485596a106fe454f56c7.png)

<hr>


## 附

&emsp;&emsp;目前现存的中文音频翻译模型普遍存在标点符号的缺失问题，如果您需要中文标点符号添加请访问这篇CSDN文章，文章内提供一个中文标点重建的轻量级模型👇
[基于深度学习的中文语音识别模型（支持wav、mp4、m4v格式音频上传）--提供源码和经训练的模型【已开源】](https://blog.csdn.net/qq_45566099/article/details/139421116)

<hr>

## 作者联系方式：

- VX：Accddvva
- QQ：1144968929

