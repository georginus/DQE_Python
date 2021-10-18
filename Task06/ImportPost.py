import sys
import os
sys.path.append('../Task05')
from News import News
from PrivateAd import PrivateAd
from LifeHack import LifeHack

file_path = '../Task05/'
file_name = 'output.txt'
f = open(file_path + file_name, 'r')
print(f.read())

print(file_path)
a = sys.path
print(a)
news = News('text', 'city')
post = news.printPost()
print(post)