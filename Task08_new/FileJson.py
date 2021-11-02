import json
import sys

sys.path.append('../Task05')

from Task05.News import News
from Task05.PrivateAd import PrivateAd
from Task05.LifeHack import LifeHack


class FileJson:
    @staticmethod
    def fileReadJSON(import_file_path = './Import/my_json.json'):
        file_json = json.load(open(import_file_path))
        return file_json

    @staticmethod
    def fileWriteJson(output_file_path='../result.txt', text=''):
        f = open(output_file_path, 'a')
        f.write(text)
        f.close()
        return output_file_path

    def parseFileJson(self, src_text):
        for element in range(len(src_text)):
            json_dict = src_text[element]
            post_code = json_dict["post_code"]
            if post_code == '1':
                text = json_dict["post_text"]
                city = json_dict["post_city"]
                post = News(text, city)
            elif post_code == '2':
                text = json_dict["post_text"]
                end_date = json_dict["end_date"]
                post = PrivateAd(text, end_date)
            elif post_code == '3':
                text = json_dict["post_text"]
                hashtag = json_dict["hashtag"]
                post = LifeHack(text, hashtag)
            else:
                post = News('', '')
            self.fileWriteJson(self.fileWriteJson(), post.printPost())


#file_json = FileJson()
#file_json.parseFileJson(file_json.fileReadJSON())