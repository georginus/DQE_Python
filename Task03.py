import re

base_text = r"""homEwork:
	tHis iz your homeWork, copy these Text to variable.

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# print(text)

lower_text = base_text.lower()  # all text in lowercase and
#extra_tabs_text = re.sub(r'\t+', ' ', lower_text).strip()  # removing extra tabs
#extra_spaces__text = re.sub(r'\s+', ' ', lower_text)  # removing extra spaces
# sentences_text = '.'.join(map(lambda s: s.strip().capitalize(), lower_text.split('.')))  # beautiful sentences
#sentences_text = '. '.join(map(lambda s: s.strip().capitalize(), lower_text.split('.\t')))  # beautiful sentences
iz_replace_text = lower_text.replace(r"“iz”", r" “iz”").replace(" iz ",
                                                                    ' is ')  # replace iz to is # replace 'Fix“iz”'

text_formatted = '\n\t'.join(map(lambda s: s.strip().capitalize(), iz_replace_text.split('\n\t')))

print(text_formatted)

paragraph_list = []
for i in range(len(text_formatted)):  # run loop for all elements (dicts) in the list_dict list
    paragraph_list = list(text_formatted.split("\n\t")) # text_formatted[i].split('\n')

print('paragraph_list is: ', paragraph_list)

for sentence in range(len(paragraph_list)):
    sentence_formatted = '. '.join(map(lambda s: s.strip().capitalize(), paragraph_list[sentence].split('.')))
    print('sentence_formatted is: ', sentence_formatted)

new_text = iz_replace_text
#print(new_text)

# Function which returns last word
def word_list(string):
    lis = list(string.split(" "))  # split by space and converting
    return lis


qlist = word_list(new_text)  # text in list by words

for i in qlist:
    r = re.compile(r'\b(\w+[.])')
    last_words_list = list(filter(r.match, qlist))
    last_sentence = [last_words_list[w].replace(r'.', '') for w in range(len(last_words_list))]

# for i in range(len(last_words_list)-1):
#    j = last_words_list[i].replace(r'.', '')
#   print(j)

def listToString(s):
    str1 = " "  # initialize an empty string
    return (str1.join(s))  # return string


last_sentence = listToString(last_sentence).capitalize()

# print(last_sentence)
#print(f"{new_text}{last_sentence}")

