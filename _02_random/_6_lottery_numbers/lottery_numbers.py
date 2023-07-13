import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()
    lottery = ''
    for i in range (6):
        number = random.randint(0, 9)
        lottery += str(number) + ''

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    messagebox.showinfo(title="Lottery Ticket", message=lottery)
    # TODO 2) Display the selected numbers to the user in a pop-up

    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
