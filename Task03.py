import re

text = r"""homEwork:
	tHis iz your homeWork, copy these Text to variable.

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# print(text)

new_text = text.lower().capitalize()# .replace(r'\n+', ' ', re.I) # all text in lowercase and
new_text = re.sub(r'\n+', '\n', new_text).strip() # removing white spaces and replace several \n to only one \n
new_text = re.sub(r'\t+', ' ', new_text).strip()
# new_text = re.sub(r'\s+', ' ', new_text)
new_text = '. '.join(map(lambda s: s.strip().capitalize(), new_text.split('.')))



print(new_text)