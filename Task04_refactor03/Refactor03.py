import re


def formatText(base_text):
    lower_text = base_text.lower()
    iz_replace_text = lower_text.replace(r"“iz”", r" “iz”").replace(" iz ",
                                                                    ' is ')  # replace iz to is # replace 'Fix“iz”'
    text_formatted = '\n\t'.join(map(lambda s: s.strip().capitalize(), iz_replace_text.split('\n\t')))
    return text_formatted


# Function which returns words list
def returnWordList(base_text):
    text_formatted = formatText(base_text)
    str_preformat = '. '.join(map(lambda s: s.strip().capitalize(), text_formatted.split('.')))
    lis = list(str_preformat.strip().split(" "))  # split by space and converting
    return lis


# Function convert list to string
def listToString(base_text):
    s = generateLastSentence(base_text)
    str1 = " "
    return str1.join(s)


# last words sentence generating
def generateLastSentence(base_text):
    list_by_words = returnWordList(base_text)
    for i in list_by_words:
        r = re.compile(r'\b(\w+[.])')
        last_words_list = list(filter(r.match, list_by_words))
        last_sentence = [last_words_list[w].replace(r'.', '') for w in range(len(last_words_list))]
    return last_sentence


# create Paragraphs list
def generateParagraphList(base_text):
    text_formatted = formatText(base_text)
    for i in range(len(text_formatted)):
        paragraph_list = list(text_formatted.split("\n\t"))
    return paragraph_list


# format Paragraphs and fill temp_text string
def generateFinalText(base_text, end_with):
    final_text = ''
    last_sentence = listToString(base_text)
    paragraph_list = generateParagraphList(base_text)
    for sentence in range(len(paragraph_list)):
        sentence_formatted = '. '.join(map(lambda s: s.strip().capitalize(), paragraph_list[sentence].split('.')))
        if sentence_formatted.endswith(end_with):
            final_text += sentence_formatted + last_sentence.capitalize() + '.' + '\n\t'
        else:
            final_text += sentence_formatted + '\n\t'
    return final_text
