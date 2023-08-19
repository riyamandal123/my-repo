# Importing the necessary module from the tkinter library.
from tkinter import *
import pandas
import random

# Setting a constant for the background color.
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------------------------------#
# Initializing a dictionary to store the current flashcard.
current_card = {}

# Trying to read data from a CSV file, if it doesn't exist, using a default dataset.
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/germany_data.csv")
    # If the file was not found, use the original_data as the dataset to learn.
    to_learn = original_data.to_dict(orient="records")
else:
    # If the file was found, use its content as the dataset to learn.
    to_learn = data.to_dict(orient="records")

# Function to load the next flashcard.
def next_card():
    global current_card, flip_timer
    # Canceling any ongoing timer for flipping the card.
    window.after_cancel(flip_timer)
    # Choosing a random flashcard from the dataset.
    current_card = random.choice(to_learn)
    current_word = current_card["Germany"]
    # Updating the canvas text to display the German word.
    canvas.itemconfig(canvas_title, text="Germany", fill="black")
    canvas.itemconfig(canvas_word, text=current_word, fill="black")
    # Starting a timer to automatically flip the card after 3 seconds.
    flip_timer = window.after(3000, func=flip_card)

# Function to flip the current flashcard.
def flip_card():
    # Changing the canvas background to show the back of the flashcard.
    canvas.itemconfig(canvas_background, image=card_background_img)
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=current_card["English"], fill="white")

# Function to handle known words.
def known_words():
    global current_card
    # Removing the known word from the dataset.
    to_learn.remove(current_card)
    # Creating a new DataFrame with updated dataset and saving it to a CSV file.
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    # Moving to the next flashcard.
    next_card()

# ----------------------------UI-------------------------#
# Creating the main window.
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# Setting a timer to automatically flip the card after 3 seconds.
flip_timer = window.after(3000, func=flip_card)

# Creating the canvas for displaying the flashcards.
canvas = Canvas(width=800, height=528, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_background_img = PhotoImage(file="images/card_back.png")
canvas_background = canvas.create_image(400, 263, image=card_front_img)
canvas_title = canvas.create_text(400, 150, text=" ", font=("Ariel", 40, "italic"), fill="black")
canvas_word = canvas.create_text(400, 263, text=" ", font=("Ariel", 60, "italic"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

# Creating buttons for indicating known and unknown words.
known_button_img = PhotoImage(file="images/right.png")
known_button = Button(image=known_button_img, highlightthickness=0, command=known_words)
known_button.grid(row=1, column=1)

unknown_button_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_button_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

# Initializing the app by loading the first flashcard.
next_card()

# Running the main event loop.
window.mainloop()
