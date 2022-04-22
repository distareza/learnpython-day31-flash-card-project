from tkinter import *
from MyFlashCard import *
import tkinter

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img_front = PhotoImage(file="images/card_front.png")
img_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=img_front)
canvas.grid(row=0, column=0, columnspan=2)
canvas_title = canvas.create_text(400, 150, text="", font=("Arial", 58, "italic"))
canvas_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

canvas_side = 0

myCard = MyFlashCard()
english_word = ""
next_guess = myCard.next_card()

def next_card():
    global english_word, flip_timer, next_guess
    window.after_cancel(flip_timer)

    next_guess = myCard.next_card()
    canvas.itemconfig(canvas_image, image=img_front)
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=next_guess["French"], fill="black")
    english_word = next_guess["English"]

    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global english_word, flip_timer

    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=img_back)
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=english_word, fill="white")


def is_known():
    try:
        print(f"removing : {next_guess}, length : {myFlashCard.card_length()}")
        myFlashCard.remove(next_guess)
    except:
        pass
    next_card()

x_image = PhotoImage(file="images/wrong.png")
y_image = PhotoImage(file="images/right.png")
unknown_button = Button(image=x_image, highlightthickness=0, command=next_card)
known_button = Button(image=y_image, highlightthickness=0, command=is_known)

known_button.grid(row=1, column=0)
unknown_button.grid(row=1, column=1)

flip_timer = window.after(3000, func=flip_card)

next_card()

window.mainloop()
myFlashCard.save_data()
