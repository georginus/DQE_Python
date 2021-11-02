import os
from Task06.ImportPost import fileWrite
from Task05.formPost import formPost
from FileJson import FileJson
from FileTxt import FileTxt
from FileXml import FileXml
from defineFileExtension import defineFileExtension


def writePosts():
    is_input_correct = False
    user_choice = 0
    while not is_input_correct:
        user_choice = int(input(f'Enter \n\t1 if you want to use default path to TXT file \n\t2 if you want to provide your path '
                                f'\n\t3 if you want to enter post manually'))
        if 0 < user_choice < 4:
            break
        else:
            print(f'Bad choice. Please try again...\n')
    try:
        if user_choice == 1:
            FileTxt().parseFileTxt(FileTxt.fileReadTxt()[0])
            filepath = FileTxt.fileReadTxt()[1]
            os.remove(filepath)
        elif user_choice == 2:
            filepath = input(f'Enter file path')
            filetype = defineFileExtension(filepath)
            if filetype == '.json':
                FileJson().parseFileJson(FileJson.fileReadJSON(filepath))
            elif filetype == '.txt':
                FileTxt().parseFileTxt(FileTxt.fileReadTxt(filepath))
            elif filetype == '.xml':
                FileXml().parseFileXml(FileXml.fileReadXml(filepath))
            else:
                pass
            os.remove(filepath)
        else:
            if_continue = 'y'
            while if_continue == 'y':
                fileWrite(formPost())
                if_continue = input('Do you want to continue?(y/N)')
    except:
        pass

    print(f'\nPlease, look at the result in the {FileTxt.fileWriteTxt()} file')

#writePosts()