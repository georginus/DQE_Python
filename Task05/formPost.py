from News import News
from PrivateAd import PrivateAd
from LifeHack import LifeHack


def formPost():
    is_input_correct = False
    while not is_input_correct:
        post_code = int(input(f'Input Post code:\n\t1 - News\n\t2 - Private Ad\n\t3 - LifeHack\n'))
        if 0 < post_code < 4:
            break
        else:
            print(f'Incorrect Post code. Please try again...\n')
    if post_code == 1:
        text = input('Enter News text:')
        city = input('Enter News city:')
        news = News(text, city)
        post = news.printPost()
    elif post_code == 2:
        text = input('Enter Private Ad text:')
        end_date = input('Enter Private Ad end date(dd/mm/yyyy):')
        ad = PrivateAd(text, end_date)
        post = ad.printPost()
    else:
        text = input('Enter LifeHack text:')
        hashtag = input('Enter LifeHack hashtag:')
        lifehack = LifeHack(text, hashtag)
        post = lifehack.printPost()
    return post