 

from lxml import etree 
import os

#初始化
global num
isMove = False
#--------重命名文件的格式--------#
nameRule = '%06d'# 06表示000001,000002等命名排序
#--------源文件绝对路径(结尾必须是'\\')--------#
xmldir = "D:\deeplearnITERM\DEL_imge_xml\VOCdevkit\VOC2007\Annotations\\" 
imgsdir = "D:\deeplearnITERM\DEL_imge_xml\VOCdevkit\VOC2007\JPEGImages\\"
#--------目标文件绝对路径(结尾必须是'\\')--------#
outXMLdir ="D:\deeplearnITERM\DEL_imge_xml\hbC_x_Is_DATA\Annotations\\" 
outImagedir = "D:\deeplearnITERM\DEL_imge_xml\hbC_x_Is_DATA\JPEGImages\\"


# def createFile(oripath):
#     xml_list = os.listdir(oripath)
#     for i in xml_list:  # 遍历所有xml文件
#         fullPath = oripath + i  # 完整路径
#         remove_(fullPath)  # 将完整路径作为参数传入调用该函数
 
 
def move_ImageAndXML():  # path 是原来xml文件的完整路径
    num = 1
    labName = ['aeroplane','bicycle','bird','boat','bottle','chair','diningtable','pottedplant','sofa','train','tvmonitor']
    xml_list = os.listdir(xmldir)
    for iA_XML in xml_list:  # 遍历所有xml文件
        fullPath = xmldir + iA_XML  # 完整路径
        tree = etree.parse(fullPath)
        root = tree.getroot()   # 获取根节点
        for object in root.findall('object'):   # 找到根节点下所有“object”节点
            name = str(object.find('name').text)  # 找到object节点下name子节点的值（字符串）
            for deletName in labName:
                if name == deletName:
                    root.remove(object)
        
        #已经找到对应文件开始处理
        if root.findall('object'):  # 找到为object的tag
            # 给新的xml重命名
            s = nameRule % num  # 06表示000001,000002等命名排序
            xml_name = str(s) +'.xml'
            print(num)
            num = num + 1

            #通过xml截取图片文件名
            image_Name = (iA_XML.split(".")[0])
            image_Name = image_Name + ".jpg"

            #写入新的xml文件 并移到对应路径
            new_ann_path = os.path.join(r'%s%s' %(outXMLdir, xml_name))
            tree.write(new_ann_path,encoding='utf-8') #将tree写入新的文件

            #改名
            old_Imagedir = os.path.join(os.path.abspath(imgsdir), image_Name)
            new_Imagedir = os.path.join(os.path.abspath(outImagedir), str(s)+".jpg")
            os.rename(old_Imagedir,new_Imagedir)

if __name__ == '__main__':
    move_ImageAndXML()
