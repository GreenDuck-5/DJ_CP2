def clear_screen(): print("\033c", end="")

clear_screen()

_ = 10

for item in range(_):
    print(item + 1)

def continue_screen(): input("Press \"Enter\" or \"Return\" to continue:\n")

continue_screen()

quit()