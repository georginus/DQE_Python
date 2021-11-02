import sys
import os
import json

sys.path.append('../Task05')
sys.path.append('../Task06')
sys.path.append('../Task07')
sys.path.append('../Task04_refactor03')

from News import News
from PrivateAd import PrivateAd
from LifeHack import LifeHack
from formPost import formPost
from ImportPost import fileWrite


def writePosts(src_file_path='./', src_file_name='my_json.json'):
    is_input_correct = False
    while not is_input_correct:
        user_choice = int(input(f'Enter \n\t1 if you want to use default path \n\t2 if you want to provide your path '
                                f'\n\t3 if you want to enter post manually'))
        if 0 < user_choice < 4:
            break
        else:
            print(f'Bad choice. Please try again...\n')
    try:
        if user_choice == 1:
            filepath = src_file_path + src_file_name
            parseSrc(fileRead(filepath))
            os.remove(filepath)
        elif user_choice == 2:
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


def fileRead(file_path):
    json_file = json.load(open(file_path))
    return json_file


def parseSrc(src_text):
    for element in range(len(src_text)):
        json_list = src_text[element]
        post_code = json_list["post_code"]
        if post_code == '1':
            text = json_list["post_text"]
            city = json_list["post_city"]
            post = News(text, city)
            #print(post_code, ' ', text, ' ', city, ' ')
        elif post_code == '2':
            text = json_list["post_text"]
            end_date = json_list["end_date"]
            post = PrivateAd(text, end_date)
            #print(post_code, ' ', text, ' ', end_date, ' ')
        elif post_code == '3':
            text = json_list["post_text"]
            hashtag = json_list["hashtag"]
            post = LifeHack(text, hashtag)
            #print(post_code, ' ', text, ' ', hashtag, ' ')
        fileWrite(post.printPost())
    return
