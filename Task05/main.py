from formPost import formPost


# ---Main---
file_path = ''
file_name = 'output.txt'
f = open(file_path + file_name, 'a+')
if_continue = 'y'
while if_continue == 'y':
    f.write(formPost())
    if_continue = input('Do you want to continue?(y/N)')
f.close()
