import os
def clear_screen(): os.system('CLS') if os.name == 'nt' else os.system('clear')

clear_screen()

_ = 10

for item in range(_):
    print(item + 1)

