## 概述

本项目利用python的opencv库和paddlehub库实现了简易的人脸识别+口罩佩戴检测，代码简单易懂，效果较好。



## 环境

①python

请在设备上安装python

②opencv

```powershell
pip install opencv-python
```

③paddlehub

```powershell
pip install paddlehub
```



## 使用

进入项目文件夹，运行

```powershell
python main.py
```

程序将自动下载所需模块，调用摄像头，程序会检测摄像头捕获画面中出现的人脸是否佩戴好了口罩，结果将直接显示在反馈画面上。想要结束程序时，按ESC键退出。