import sys
import re
sys.path.append('../Task04_refactor03')
sys.path.append('../Task05')
sys.path.append('../Task06')

from ImportPost import fileRead
from Refactor03 import returnWordList

def fileRead(filepath='../Task06/task06_result.txt'):
    f = open(filepath, 'r')
    src_text = f.read()
    f.close()
    return src_text

list_of_words = re.findall(r'\w+', fileRead())
# for element in list_of_words:
#     re.sub(, element)

my_list = [item for item in list_of_words if item.isalpha()]

print(my_list)
