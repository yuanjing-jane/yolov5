# coding=utf-8
import xml.dom.minidom
import os
from pathlib import Path

ROOT = r'/mnt/d/work/project/project_fish/data/label_result'
ORI_DIR = 'annotations'
NEW_DIR = 'annotations_fish'
###读取单个xml文件
files=os.listdir(Path(ROOT)/ ORI_DIR) #得到文件夹下所有文件名称
s=[]

def fix_label(dom):
    root = dom.documentElement
    name = root.getElementsByTagName('name')
    if isinstance(name, list):
        for elem in name:
            elem.firstChild.data = 'fish'
    else:
        name.firstChild.data = 'fish'


def save_dom(save_path):
    with open(save_path,'w') as f:
        dom.writexml(f)

for xmlFile in files:
    if not os.path.isdir(xmlFile):
        file_path = Path(ROOT)/ ORI_DIR / xmlFile
        # print(f'{xmlFile} is not dir')
        dom = xml.dom.minidom.parse(str(file_path))
        fix_label(dom)
        save_path = file_path.resolve().parents[1]/NEW_DIR/f'm_{xmlFile}'
        save_dom(save_path)