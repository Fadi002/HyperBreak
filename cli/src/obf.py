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
import base64, re, random, marshal
from .var import HyperBreak_name_gen
anti_skid = """if __HyperBreak__ != 'HyperBreak by fadi' or __license__ !='MIT License':
    print('You just executed a file protected with HyperBreak dont try to skid this project');input('press enter to exit')
    try:int(oke)
    except:exit(1337)
"""
def encrypt(code, key=0):
    return "".join(([chr(ord(i) + key) for i in code]))
def junker():
    return "__HyperBreak__" * random.randint(5,10)
def encode1(code):
    code = base64.b64encode(code.encode()).decode()
    code = base64.b32encode(code.encode()).decode()
    code = base64.b16encode(code.encode()).decode()
    name = HyperBreak_name_gen()
    nice = 'from base64 import b64decode as {b1};from base64 import b32decode as {b2};{ex}=exec;from base64 import b16decode as {b3};{ex}({b1}({b2}({b3}("{c}"))))'.format(b1=name.random_string(),b2=name.random_string(),b3=name.random_string(),c=code,ex=name.random_string())
    return nice
def mar(code):
    x = compile(code,'','exec')
    n = marshal.dumps(x)
    s = f'import marshal;exec(marshal.loads({n}))'
    return s
def var_renamer(code):
    code = "\n" + code
    damn = re.findall(r"(\w+)(?=( |)=( |))", code)
    name = HyperBreak_name_gen()
    for i in range(len(damn)):
        name_var = name.random_string(i)
        nice = re.sub(r"(?<=[^.])(\b{}\b)".format(damn[i][0]), name_var, code)
        code = ''
        code = f"\n{name.l_and_i(i+random.randint(5,10))}='{name.l_and_i(i+random.randint(5,10))}'"
        code = code + f"\n{name.single_letter_a_lot(i+random.randint(5,10))}='{name.single_letter_a_lot(i+random.randint(5,10))}'"
        code = code + f"\n{name.scream(i+random.randint(5,10))}='{name.scream(i+random.randint(5,10))}'"
        code = code + f"\n{name.l_and_i(i+random.randint(5,10))}='{name.l_and_i(i+random.randint(5,10))}'"
        code = code + f"\n{name.random_string(i+random.randint(5,10))}='{name.random_string(i+random.randint(5,10))}'"
        code = code + f"\n{name.scream(i+random.randint(5,10))}='{name.scream(i+random.randint(5,10))}'"
        code = code + nice
        code = code + f"\n{name.l_and_i(i+random.randint(5,10))}='{name.l_and_i(i+random.randint(5,10))}'"
        code = code + f"\n{name.l_and_i(i+random.randint(5,10))}='{name.l_and_i(i+random.randint(5,10))}'"
        code = code + f"\n{name.random_string(i+random.randint(5,10))}='{name.random_string(i+random.randint(5,10))}'"
        code = code + f"\n{name.random_string(i+random.randint(5,10))}='{name.random_string(i+random.randint(5,10))}'"
        code = code + f"\n{name.scream(i+random.randint(5,10))}='{name.scream(i+random.randint(5,10))}'"
        code = code + f"\n{name.scream(i+random.randint(5,10))}='{name.scream(i+random.randint(5,10))}'"
    return code
def encode2(code):
    key = random.randint(1000,5000)
    ok = encrypt(code,key)
    nice = base64.b85encode(ok.encode())
    lol = mar('__=compile')
    noice = mar('_=exec')
    for i in range(10):
        lol=mar(lol)
    for i in range(5):
        noice=mar(noice)
    algo = f"""
__HyperBreak__ = 'HyperBreak by fadi'
__license__ = 'MIT License'
{lol};{mar(f"{junker()}='{junker()}'")};{junker()}='{junker()}';{mar(f"{junker()}='{junker()}'")};{junker()}='{junker()}';
def _____(___________,_____=0):return "".join([chr(ord(____________)-_____) for ____________ in ___________])
{mar(f"{junker()}='{junker()}'")};{junker()}='{junker()}';{mar(f"{junker()}='{junker()}'")};{junker()}='{junker()}'
{mar(f"{junker()}='{junker()}'")};{junker()}='{junker()}';{mar(f"{junker()}='{junker()}'")};{junker()}='{junker()}'
{mar(f"{junker()}='{junker()}'")};{junker()}='{junker()}';{noice};{mar(f"{junker()}='{junker()}'")};{junker()}='{junker()}'
{mar(f"{junker()}='{junker()}'")};{junker()}='{junker()}';{mar(f"{junker()}='{junker()}'")};{junker()}='{junker()}';{mar(f"{junker()}='{junker()}'")};{junker()}='{junker()}';{mar(f"{junker()}='{junker()}'")};{junker()}='{junker()}';{mar(f"{junker()}='{junker()}'")};{junker()}='{junker()}';{mar(f"{junker()}='{junker()}'")};{junker()}='{junker()}';exec('import os');_(__((_____(__import__('\\x62\\x61\\x73\\x65\\x36\\x34').b85decode({nice}).decode(),{key})),"<https://github.com/Fadi002 HyperBreak on top lol>","exec"));{mar(f"{junker()}='{junker()}'")};{junker()}='{junker()}';{mar(f"{junker()}='{junker()}'")};{junker()}='{junker()}';{junker()}='{junker()}';{junker()}='{junker()}';{mar(f"{junker()}='{junker()}'")};{junker()}='{junker()}';{mar(f"{junker()}='{junker()}'")};{junker()}='{junker()}';
{mar(f"{junker()}='{junker()}'")};{junker()}='{junker()}';{mar(f"{junker()}='{junker()}'")};{junker()}='{junker()}'
{mar(f"{junker()}='{junker()}'")};{junker()}='{junker()}';{mar(f"{junker()}='{junker()}'")};{junker()}='{junker()}'
{mar(f"{junker()}='{junker()}'")};{junker()}='{junker()}';{mar(f"{junker()}='{junker()}'")};{junker()}='{junker()}'"""
    return algo
def HyperBreak_obf(code,rename=False):
    code = code
    code = "\n"+anti_skid+"\n" + code
    if rename:
        code = var_renamer(code)
    code = encode1(code)
    for i in range(10):code = mar(code)
    code = encode2(code)
    return code
