from News import News
from PrivateAd import PrivateAd
from LifeHack import LifeHack
from Task08_new.DBConnection import DBConnection
from datetime import datetime


def formPost():
    is_input_correct = False
    while not is_input_correct:
        post_code = int(input(f'Input Post code:\n\t1 - News\n\t2 - Private Ad\n\t3 - LifeHack\n'))
        if 0 < post_code < 4:
            break
        else:
            print(f'Incorrect Post code. Please try again...\n')
    db = DBConnection()
    if post_code == 1:
        text = input('Enter News text:')
        city = input('Enter News city:')
        news = News(text, city)
        post = news.printPost()
        post_date = datetime.today().strftime('%d/%m/%Y %H.%M')
        db.insertNews(post_code, text, city, post_date)
    elif post_code == 2:
        text = input('Enter Private Ad text:')
        end_date = input('Enter Private Ad end date(dd/mm/yyyy):')
        ad = PrivateAd(text, end_date)
        post = ad.printPost()
        db.insertPrivateAd(post_code, text, end_date)
    else:
        text = input('Enter LifeHack text:')
        hashtag = input('Enter LifeHack hashtag:')
        lifehack = LifeHack(text, hashtag)
        post = lifehack.printPost()
        post_date = datetime.today().strftime('%d/%m/%Y %H.%M')
        db.insertLifehack(post_code, text, hashtag, post_date)
    db.closeCursor()
    return post




