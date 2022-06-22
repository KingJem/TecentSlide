

#腾讯防水墙滑块验证码深度学习识别训练

训练集只标注了200张图片

# 添加数据集继续训练
#### 下载验证码放到VOCdevkit/VOC2012/JPEGImages 中
#### 运行 VOCdevkit/02.image_name_type_update.py
#### 数据标注保存到VOCdevkit/VOC2012/Annotations 中
#### 运行 03.voc2012_util.py 
#### 修改 model_data/classes.txt 中的值 我使用的标签是0 
#### 运行 04.make_train_val_test.py 05.voc_annotation.py
#### 修改train.py 中的参数 进行训练


# 服务部署
#### 上传代码到服务器
#### 安装环境
#### 修改模型路径
```python
class CenterNet(object):
    _defaults = {
        "model_path": 'logs/Epoch17-Total_Loss1.8939-Val_Loss1.5785.pth',
    }
```
#### 运行server.py 
