# -*- coding: utf-8 -*-

import os


#  生成VOC 2012 的数据集合目录
def _make_voc_dir():
	pathArr = [
		'VOC2012/Annotations',
		'VOC2012/ImageSets/Action',
		'VOC2012/ImageSets/Main',
		'VOC2012/ImageSets/Layout',
		'VOC2012/ImageSets/Segmentation',
		'VOC2012/JPEGImages',
		'VOC2012/SegmentationClass',
		'VOC2012/SegmentationObject',
	]
	for path in pathArr:
		if not os.path.exists(path):
			os.makedirs(path)


if __name__ == '__main__':
	_make_voc_dir()
