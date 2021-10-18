import sys

# from Task04_refactor03 import formatText

sys.path.append('../Task05')
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
        #print(parsed_list)
        post_code = parsed_list[0]
        if post_code == '1':
            text = parsed_list[1]
            city = parsed_list[2]
            news = News(text, city)
            post = news.printPost()
            print(post)
        elif post_code == '2':
            text = parsed_list[1]
            end_date = parsed_list[2]
            ad = PrivateAd(text, end_date)
            post = ad.printPost()
            print(post)
        else:
            text = parsed_list[1]
            hashtag = parsed_list[2]
            lifehack = LifeHack(text, hashtag)
            post = lifehack.printPost()
            #print(parsed_list[1], ' ', parsed_list[2])
            print(post)
    return parsed_list


print(parseSrc(fileRead()))
#print(fileRead())
# print(a)

# news = News('text', 'city')
# post = news.printPost()
# print(post)


my_string = 'Names: Romeo, Juliet'

# split the string at ':'
step_0 = my_string.split(':')

# get the first slice of the list
step_1 = step_0[1]

# split the string at ','
step_2 = step_1.split(',')

# strip leading and trailing edge spaces of each item of the list
step_3 = [name.strip() for name in step_2]

# do all the above operations in one go
one_go = [name.strip() for name in my_string.split(':')[1].split(',')]

# for idx, item in enumerate([step_0, step_1, step_2, step_3]):
#    print("Step {}: {}".format(idx, item))

# print("Final result in one go: {}".format(one_go))
