from lxml import etree 
import os
global num
xmldir = "E:\Graduate\Code\YOLOX_GRA\VOCdevkit\VOC2007\Annotations\\" 


def image_count():  # path 是原来xml文件的完整路径
    tar = {'bus':0,'car':0,'cat':0,'cow':0,'dog':0,'horse':0,'motorbike':0,'person':0,'sheep':0}
    num = 1
    xml_list = os.listdir(xmldir)
    for iA_XML in xml_list:  # 遍历所有xml文件
        num = num + 1
        fullPath = xmldir + iA_XML  # 完整路径
        tree = etree.parse(fullPath)
        root = tree.getroot()   # 获取根节点
        for object in root.findall('object'):   # 找到根节点下所有“object”节点
            name = str(object.find('name').text)  # 找到object节点下name子节点的值（字符串）
            for countName in tar:
                if name == countName:
                    tar[name] = tar[name] + 1
        print('处理第'+ str(num+15000) +'张')
    print('——————————————————————————————————————————————————————————————————————————————————————————————————')
    print('\nVOC数据集已剔除11个分类：aeroplane,bicycle,bird,boat,bottle,chair,diningtable,pottedplant,sofa,train,tvmonitor')
    print('处理后的标注目标框的统计如下:')
    for key in tar:
        print(key+':'+ str(tar[key]))

if __name__ == '__main__':
    image_count()