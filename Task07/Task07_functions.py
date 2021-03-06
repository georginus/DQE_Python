import re
import csv


def fileRead(filepath='../Task06/task06_result.txt'):
    f = open(filepath, 'r')
    src_text = f.read()
    f.close()
    return src_text


def list_of_words(text=fileRead()):
    temp_list_of_words = re.findall(r'\w+', text)
    list_of_words = [item for item in temp_list_of_words if item.isalpha()]
    return list_of_words


def list_of_letters(text=fileRead()):
    char_list = [char for char in text]
    return [item for item in char_list if item.isalpha()]


def wordsInLower(list_of_words=list_of_words()):
    words_lower_list = []
    for word in list_of_words:
        words_lower = str(word).lower()
        words_lower_list.append(words_lower)
    return words_lower_list


def countElements(word_list=wordsInLower()):
    word_count_dict = {}
    for i in range(len(word_list)):
        word = word_list[i]
        if word in word_count_dict.keys():
            word_count_dict[word] = word_count_dict.get(word) + 1
        else:
            word_count_dict[word] = 1
    return word_count_dict


def upperLowerLettersDict(letters_dict=countElements(list_of_letters())):
    upper_dict = {}
    lower_dict = {}
    for key, value in letters_dict.items():
        if key.isupper():
            upper_dict[key] = value
        else:
            lower_dict[key] = value
    return upper_dict, lower_dict


# print(countWords())
# upper, lower = upperLowerLettersDict()
# print(upper)
# print(lower)

def countLetterAppearance(upper=upperLowerLettersDict()[0], lower=upperLowerLettersDict()[1]):
    count_all_dict = {}
    for key, value in lower.items():
        if key in upper.keys():
            count_all_dict[key] = value + upper.get(key.upper())
        else:
            count_all_dict[key] = value
    for key, value in upper.items():
        if key.lower() in count_all_dict:
            pass
        else:
            count_all_dict[key.lower] = value
    return count_all_dict


def totalLettersCount(letters=list_of_letters()):
    return len(letters)


def resultFile2Creation(total=totalLettersCount(), upper=upperLowerLettersDict()[0],
                       count_letter_appearance=countLetterAppearance()):
    with open('../Task07/task07_02.csv', 'w', newline='') as csv_file:
        header = ['letter', 'count_all', 'count_uppercase', 'percentage']
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()
        for key, value in count_letter_appearance.items():
            percent = round(value / total * 100, 2)
            upper_count = upper.get(key.upper())
            if upper_count is None:
                upper_count = 0
            writer.writerow(
                {'letter': key, 'count_all': value, 'count_uppercase': upper_count, 'percentage': str(percent) + '%'})
            # print(key, value, upper_count, str(percent)+'%')


def resultFile1Creation(count_words=None):
    if count_words is None:
        count_words = countElements(wordsInLower())
    with open('../Task07/task07_01.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter='-')
        for key, value in count_words.items():
            writer.writerow([key, value])
