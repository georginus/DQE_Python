import sys
sys.path.append('../Task05')
sys.path.append('../Task04_refactor03')

from Refactor03 import formatText

from Post import Post
from News import News
from PrivateAd import PrivateAd
from LifeHack import LifeHack


def fileRead(src_file_path='./', src_file_name='task06_src.txt'):
    # print(f'src_file_path = {src_file_path}; src_file_name = {src_file_name}')
    f = open(src_file_path + src_file_name, 'r')
    src_text = f.read().splitlines()
    # print(src_text)
    f.close()
    return src_text


def parseSrc(src_text):
    for element in src_text:
        parsed_list = element.split('---')
        post_code = parsed_list[0]
        if post_code == '1':
            text = parsed_list[1]
            src_text_formatted = formatText(text)
            sentence_formatted = '. '.join(map(lambda s: s.strip().capitalize(), src_text_formatted.split('.')))
            city = parsed_list[2]
            news = News(sentence_formatted, city)
            post = news.printPost()
            print(post)
        elif post_code == '2':
            text = parsed_list[1]
            src_text_formatted = formatText(text)
            sentence_formatted = '. '.join(map(lambda s: s.strip().capitalize(), src_text_formatted.split('.')))
            end_date = parsed_list[2]
            ad = PrivateAd(sentence_formatted, end_date)
            post = ad.printPost()
            print(post)
        elif post_code == '3':
            text = parsed_list[1]
            src_text_formatted = formatText(text)
            sentence_formatted = '. '.join(map(lambda s: s.strip().capitalize(), src_text_formatted.split('.')))
            hashtag = parsed_list[2]
            lifehack = LifeHack(sentence_formatted, hashtag)
            post = lifehack.printPost()
            print(post)
    return parsed_list


print(parseSrc(fileRead()))
#print(fileRead())
# print(a)
