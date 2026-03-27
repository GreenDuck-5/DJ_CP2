def after_action():
    def continue_screen():
        print("Press Enter to continue.")
        input()
    def clear_screen():
        print("\033c", end="")
    continue_screen()
    clear_screen()

