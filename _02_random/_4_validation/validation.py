import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    for i in range 10:
        random_number = random.randint(1, 5)
        if random_number == 1:
            messagebox.showinfo(title="Compliment 1", message="Your hair looks nice!")
        if random_number == 2:
            messagebox.showinfo(title="Compliment 2", message="You look nice!")
        if random_number == 3:
            messagebox.showinfo(title="Compliment 3", message="You light up the room!")
        if random_number == 4:
            messagebox.showinfo(title="Compliment 4", message="On a scale from 1-10, you're a 11!")
        if random_number == 5:
            messagebox.showinfo(title="Compliment 5", message="You are a gift to those around you!")
        print(random_number)

    # TODO 1) Use each value of random_number to give the user a random compliment

    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)
