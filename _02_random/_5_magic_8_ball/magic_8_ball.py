import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    question = simpledialog.askstring(title="Magic 8-ball", prompt="Ask a question and the magic 8-ball will answer:")
    # Make a variable and initialize it to a random number between 0 and 3
    number = random.randint(0, 3)
    # If the random number is 0
    if number == 0:
        messagebox.showinfo(title="Magic 8-ball", message="Yes")
        # tell the user "Yes"

    # If the random number is 1
    if number == 1:
        messagebox.showinfo(title="Magic 8-ball", message="No")
        # tell the user "No"

    # If the random number is 2
    if number == 2:
        messagebox.showinfo(title="Magic 8-ball", message="Maybe you should ask Google?")
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3
    if number == 3:
        messagebox.showinfo(title="Magic 8-ball", message="Do you think that is a good question?")
        # write your own answer
