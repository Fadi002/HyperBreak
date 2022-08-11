import os
def c():
    os.system('cls' if os.name == 'nt' else 'clear')
def py():
    return 'python' if os.name == 'nt' else 'python3'
print('''HyperBreak start menu
[1] cli-mode
[2] webUI mode''')
try:
    nice = int(input('-> '))
except:
    nice = 1
if nice == 1:
    c()
    os.system(py()+" cli\\HyperBreak.py")
elif nice == 2:
    c()
    os.system(py()+" website\\HyperBreak.py")
else:
    c()
    os.system(py()+" cli\\HyperBreak.py")
