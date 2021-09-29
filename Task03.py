import re

base_text = r"""homEwork:
	tHis iz your homeWork, copy these Text to variable.

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# print(text)

lower_text = base_text.lower() # all text in lowercase and
extra_tabs_text = re.sub(r'\t+', ' ', lower_text).strip() # removing extra tabs
extra_spaces__text = re.sub(r'\s+', ' ', lower_text) # removing extra spaces
sentences_text = '. '.join(map(lambda s: s.strip().capitalize(), extra_spaces__text.split('.'))) # beautiful sentences
iz_replace_text = sentences_text.replace(r"“iz”", r" “iz”").replace(" iz", ' is') # replace iz to is # replace 'Fix“iz”'
new_text = iz_replace_text


# Function which returns last word
def word_list(string):
    # split by space and converting
    # string to list and
    lis = list(string.split(" "))
    print (lis)
    # length of list
    length = len(lis)

    # returning last element in list
    return lis[length - 1]

qlist = word_list(new_text)
qlist.find('\.')

print(new_text)