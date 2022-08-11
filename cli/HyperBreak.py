'''
MIT License

Copyright (c) 2022 Fadi1337

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
from src import *
from os.path import exists
OBFUSCATE = HyperBreak_obf
UI = HyperBreak_UI()
UI.clear()
UI.banner_start()
input()
UI.clear()
def main():
    UI.banner()
    UI.fade_type('Enter file path : ')
    file_path = input()
    if not exists(file_path):
        UI.fade_type('Invaild file path or not exists\n')
        UI.restart()
        UI.clear()
        main()
    file=open(file_path,'r',encoding='utf8').read()
    name = file_path.split('/')[-1]
    name = file_path.split('\\')[-1]
    name = name.split('.')[0]
    UI.fade_type('Do you want to rename varables ? [y/n] : ')
    rename=input()
    if rename == 'Y' or rename == 'y':
        print('obfuscating ...')
        code = OBFUSCATE(file,rename=True)
    else:
        print('obfuscating ...')
        code = OBFUSCATE(file,rename=False)
    UI.clear()
    UI.banner()
    with open(f"{name}-HyperBreak.py",'w',encoding='utf8') as f:f.write(code)
    UI.fade_type(f'Your code has been obfuscated and saved as : {name}-HyperBreak.py\n')
    UI.fade_type('\nthanks for using this tool\n')
    UI.fade_type('\n\nPress any key to exit')
    input()
main()