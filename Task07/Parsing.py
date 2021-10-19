import sys
import re


# sys.path.append('../Task04_refactor03')
# sys.path.append('../Task05')
# sys.path.append('../Task06')

# from ImportPost import fileRead
# from Refactor03 import returnWordList


def fileRead(filepath='../Task06/task06_result.txt'):
    f = open(filepath, 'r')
    src_text = f.read()
    f.close()
    return src_text


def list_of_words(text=fileRead()):
    temp_list_of_words = re.findall(r'\w+', text)
    list_of_words = [item for item in temp_list_of_words if item.isalpha()]
    return list_of_words
#print(list_of_words())


def wordsInLower(list_of_words = list_of_words()):
    words_lower_list = []
    for word in list_of_words:
        words_lower = str(word).lower()
        words_lower_list.append(words_lower)
    return words_lower_list


print(wordsInLower())