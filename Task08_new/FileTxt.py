import sys

sys.path.append('../Task05')

from Task08_new.sentenceFormat import sentenceFormatted
from Task05.News import News
from Task05.PrivateAd import PrivateAd
from Task05.LifeHack import LifeHack
from Task08_new.DBConnection import DBConnection
from datetime import datetime


class FileTxt:
    @staticmethod
    def fileReadTxt(importfilepath='./Import/my_txt.txt'):
        f = open(importfilepath, 'r')
        filepath = importfilepath
        file_txt = f.read().splitlines()
        f.close()
        return file_txt, filepath

    @staticmethod
    def fileWriteTxt(outputfilepath='../result.txt', text=''):
        f = open(outputfilepath, 'a')
        f.write(text)
        f.close()
        return outputfilepath

    def parseFileTxt(self, src_text):
        db = DBConnection()
        for element in src_text:
            parsed_list = element.split('---')
            post_code = parsed_list[0]
            if post_code == '1':
                text = sentenceFormatted(parsed_list[1])
                city = parsed_list[2]
                post = News(text, city)
                post_date = datetime.today().strftime('%d/%m/%Y %H.%M')
                db.insertNews(post_code, text, city, post_date)
            elif post_code == '2':
                text = sentenceFormatted(parsed_list[1])
                end_date = parsed_list[2]
                post = PrivateAd(text, end_date)
                db.insertPrivateAd(post_code, text, end_date)
            elif post_code == '3':
                text = sentenceFormatted(parsed_list[1])
                hashtag = parsed_list[2]
                post = LifeHack(text, hashtag)
                post_date = datetime.today().strftime('%d/%m/%Y %H.%M')
                db.insertLifehack(post_code, text, hashtag, post_date)
            else:
                post = News('', '')
            self.fileWriteTxt('../result.txt', post.printPost())
        db.closeCursor()
