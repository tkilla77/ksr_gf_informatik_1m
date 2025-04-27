def get_random_time():
    import random, datetime
    hour   = random.randint(0,23)
    minute = random.randint(0,59)
    sec    = random.randint(0,59)

    return datetime.time(hour, minute, sec)

from clock import show_time
import turtle, tkinter

while True:
    time = get_random_time()
    show_time(time)
    inp = turtle.textinput("What time is it?", "Enter 24h time")
    print(time)
    if inp == str(time):
        tkinter.messagebox.showinfo(message=f"Correct: {str(time)}", geometry="+0+0")
    else:
        tkinter.messagebox.showerror(message=f"Incorrect: {str(time)}", geometry="+0+0")

