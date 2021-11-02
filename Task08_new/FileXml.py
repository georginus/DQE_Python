import sys

sys.path.append('../Task05')

import xml.etree.ElementTree as ET

from Task05.News import News
from Task05.PrivateAd import PrivateAd
from Task05.LifeHack import LifeHack


class FileXml:
    pass

    @staticmethod
    def fileReadXml(importfilepath='./Import/my_xml.xml'):
        xml_file = ET.parse(importfilepath)
        root = xml_file.getroot()
        return root

    @staticmethod
    def fileWriteTxt(outputfilepath='../result.txt', text=''):
        f = open(outputfilepath, 'a')
        f.write(text)
        f.close()
        return outputfilepath

    @staticmethod
    def parseFileXml(xml_root):
        # xml_root = FileXml.fileReadXml()
        xml_dict = {}
        list_common = []
        for post in xml_root:
            for element in post:
                xml_dict[element.tag] = element.text
            list_common.append(xml_dict)
            xml_dict = {}
        for some_dict in range(len(list_common)):
            current_dict = list_common[some_dict]
            post_code = current_dict["post_code"]
            if post_code == '1':
                text = current_dict["post_text"]
                city = current_dict["city"]
                post = News(text, city)
            elif post_code == '2':
                text = current_dict["post_text"]
                end_date = current_dict["date"]
                post = PrivateAd(text, end_date)
            elif post_code == '3':
                text = current_dict["post_text"]
                hashtag = current_dict["hashtag"]
                post = LifeHack(text, hashtag)
            else:
                post = News('', '')
            FileXml.fileWriteTxt('../result.txt', post.printPost())


#FileXml.parseFileXml(FileXml.fileReadXml())

