import os
import sys

sys.path.append('../Task05')
sys.path.append('../Task04_refactor03')

from Refactor03 import formatText
from News import News
from PrivateAd import PrivateAd
from LifeHack import LifeHack
from formPost import formPost


def writePosts(src_file_path='./', src_file_name='task06_src.txt'):
    is_input_correct = False
    while not is_input_correct:
        user_Choice = int(input(f'Enter \n\t1 if you want to use default path \n\t2 if you want to provide your path '
                                f'\n\t3 if you want to enter post manually'))
        if 0 < user_Choice < 4:
            break
        else:
            print(f'Bad choice. Please try again...\n')
    try:
        if user_Choice == 1:
            filepath = src_file_path + src_file_name
            parseSrc(fileRead(filepath))
            os.remove(filepath)
        elif user_Choice == 2:
            filepath = input(f'Enter file path')
            parseSrc(fileRead(filepath))
            os.remove(filepath)
        else:
            if_continue = 'y'
            while if_continue == 'y':
                fileWrite(formPost())
                if_continue = input('Do you want to continue?(y/N)')
    except:
        pass


def fileRead(filepath):
    f = open(filepath, 'r')
    src_text = f.read().splitlines()
    f.close()
    return src_text


def fileWrite(text, result_file_path='./', result_file_name='task06_result.txt'):
    f = open(result_file_path + result_file_name, 'a')
    f.write(text)
    f.close()
    return


def sentenceFormatted(text):
    sentence_formatted = '. '.join(map(lambda s: s.strip().capitalize(), formatText(text).split('.')))
    return sentence_formatted


def parseSrc(src_text):
    for element in src_text:
        parsed_list = element.split('---')
        post_code = parsed_list[0]
        if post_code == '1':
            text = sentenceFormatted(parsed_list[1])
            city = parsed_list[2]
            post = News(text, city)
        elif post_code == '2':
            text = sentenceFormatted(parsed_list[1])
            end_date = parsed_list[2]
            post = PrivateAd(text, end_date)
        elif post_code == '3':
            text = sentenceFormatted(parsed_list[1])
            hashtag = parsed_list[2]
            post = LifeHack(text, hashtag)
        fileWrite(post.printPost())
    return

#print(parseSrc('./task06_src.txt'))
#print(fileRead('./task06_src.txt'))
#a = fileRead('./task06_src.txt')
#b = sentenceFormatted(a)
#print(a[0])