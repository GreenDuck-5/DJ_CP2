import os
def clear_screen():
    if os.name == 'nt':
        os.system('CLS')
    else:
        os.system('clear')

clear_screen()

_ = 10

for item in range(_):
    print(item+1)

minecraft = 100
print(minecraft)
minecraft /= 10
print(minecraft)