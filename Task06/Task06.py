import sys
import os
sys.path.append('./Task05')
from News import News
from PrivateAd import PrivateAd
from LifeHack import LifeHack

# f = open(file_path + file_name, 'a+')


a = sys.path
print(a)
news = News('text', 'city')
post = news.printPost()
print(post)

