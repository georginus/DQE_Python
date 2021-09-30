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


# Function convert list to string
def listToString(s):
    str1 = " "
    return (str1.join(s))


list_by_words = word_list(text_formatted)  # text in list by words

# last words sentence generating
for i in list_by_words:
    r = re.compile(r'\b(\w+[.])')
    last_words_list = list(filter(r.match, list_by_words))
    last_sentence = [last_words_list[w].replace(r'.', '') for w in range(len(last_words_list))]

last_sentence = listToString(last_sentence)

# create Paragraphs list
for i in range(len(text_formatted)):
    paragraph_list = list(text_formatted.split("\n\t"))

# format Paragraphs and fill temp_text string
final_text = ''
for sentence in range(len(paragraph_list)):
    sentence_formatted = '. '.join(map(lambda s: s.strip().capitalize(), paragraph_list[sentence].split('.')))
    sentence1_formatted = sentence_formatted
    if sentence1_formatted.endswith('add it to the end of this paragraph. '):
        final_text += sentence1_formatted + last_sentence.capitalize() + '. ' + '\n\t'
    else:
        final_text += sentence1_formatted + '\n\t'

print(final_text)


def check_space(string):
    count = 0
    # loop for search each index
    for i in string:
        if i == re.sub(r'\b(\s+)', '  ', final_text):
            count += 1

    return count


print("number of spaces:", check_space(final_text))
