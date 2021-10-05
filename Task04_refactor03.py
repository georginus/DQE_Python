import re


# def source_text(text):
#     base_text = text
#     return base_text

def formatText(base_text):
    lower_text = base_text.lower()
    iz_replace_text = lower_text.replace(r"“iz”", r" “iz”").replace(" iz ",
                                                                    ' is ')  # replace iz to is # replace 'Fix“iz”'
    text_formatted = '\n\t'.join(map(lambda s: s.strip().capitalize(), iz_replace_text.split('\n\t')))
    return text_formatted


# Function which returns words list
def returnWordList(string):
    str_preformat = '. '.join(map(lambda s: s.strip().capitalize(), string.split('.')))
    lis = list(str_preformat.strip().split(" "))  # split by space and converting
    return lis


# Function convert list to string
def listToString(s):
    str1 = " "
    return (str1.join(s))


# last words sentence generating
def generateLastSentence(list_by_words):
    for i in list_by_words:
        r = re.compile(r'\b(\w+[.])')
        last_words_list = list(filter(r.match, list_by_words))
        last_sentence = [last_words_list[w].replace(r'.', '') for w in range(len(last_words_list))]
    return last_sentence


# create Paragraphs list
def generateParagraphList(text_formatted):
    for i in range(len(text_formatted)):
        paragraph_list = list(text_formatted.split("\n\t"))
    return paragraph_list

# format Paragraphs and fill temp_text string
def generateFinalText(paragraph_list, end_with):
    final_text = ''
    for sentence in range(len(paragraph_list)):
        sentence_formatted = '. '.join(map(lambda s: s.strip().capitalize(), paragraph_list[sentence].split('.')))
        if sentence_formatted.endswith(end_with):
            final_text += sentence_formatted + last_sentence.capitalize() + '.' + '\n\t'
        else:
            final_text += sentence_formatted + '\n\t'
    return final_text


# Main
base_text = r"""homEwork:
	tHis iz your homeWork, copy these Text to variable.

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""
text_formatted = formatText(base_text)
list_by_words = returnWordList(text_formatted)  # text in list by words
last_sentence = listToString(generateLastSentence(list_by_words))
paragraph_list = generateParagraphList(text_formatted)
final_text = generateFinalText(paragraph_list, 'add it to the end of this paragraph. ')

# print result
print(final_text)

# print spaces count
p = re.compile(r'(\s)')
spaces_list = p.findall(final_text)
print("number of spaces: ", len(spaces_list))
