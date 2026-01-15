def clear_screen(): print("\033c", end="")

clear_screen()

_ = 10

for item in range(_):
    print(item + 1)

