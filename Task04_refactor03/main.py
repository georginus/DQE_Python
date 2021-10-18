#import sys
#sys.path.append('./Task04_refactor03')
from Task04_refactor03 import Task04_refactor03

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