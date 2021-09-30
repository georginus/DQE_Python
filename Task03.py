import re

base_text = r"""homEwork:
	tHis iz your homeWork, copy these Text to variable.

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# print(text)

lower_text = base_text.lower()  # all text in lowercase and
iz_replace_text = lower_text.replace(r"“iz”", r" “iz”").replace(" iz ",
                                                                ' is ')  # replace iz to is # replace 'Fix“iz”'

text_formatted = '\n\t'.join(map(lambda s: s.strip().capitalize(), iz_replace_text.split('\n\t')))


# Function which returns words list
def word_list(string):
    str_preformat = '. '.join(map(lambda s: s.strip().capitalize(), string.split('.')))
    lis = list(str_preformat.strip().split(" "))  # split by space and converting
    return lis


def listToString(s):
    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(s))


qlist = word_list(text_formatted)  # text in list by words
# print(qlist)

# for i in range(len(qlist)-1):
#    j = qlist[i].replace(r'.', '')
#    print(j)


for i in qlist:
    r = re.compile(r'\b(\w+[.])')
    last_words_list = list(filter(r.match, qlist))
    last_sentence = [last_words_list[w].replace(r'.', '') for w in range(len(last_words_list))]

last_sentence = listToString(last_sentence)

# create Paragraphs list
for i in range(len(text_formatted)):
    paragraph_list = list(text_formatted.split("\n\t"))

# format Paragraphs and fill temp_text string
temp_text = ''
for sentence in range(len(paragraph_list)):
    sentence_formatted = '. '.join(map(lambda s: s.strip().capitalize(), paragraph_list[sentence].split('.')))
    sentence1_formatted = sentence_formatted
    if sentence1_formatted.endswith('add it to the end of this paragraph. '):
        temp_text += sentence1_formatted + last_sentence.capitalize()+'. '+ '\n\t'
    else:
        temp_text += sentence1_formatted + '\n\t'

print(temp_text)
