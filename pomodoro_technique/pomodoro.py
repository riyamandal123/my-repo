from tkinter import *
import math
from playsound import playsound  # Import the playsound library
import threading

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(set_timer, text="00:00")
    timer_label.config(text="TIMER")
    checkbox_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def play_clock_sound():
    # Function to play the clock sound in a separate thread
    playsound('clock_sound.mp3')
def start_timer():
    global reps
    # no of repetetions.
    reps += 1
    # to convert them into seconds.
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Create a new thread to play the clock sound
    clock_thread = threading.Thread(target=play_clock_sound)
    clock_thread.start()

    # if reps is a odd number indicating a work session.
    if reps % 2 != 0:
        timer_label.config(text="STUDY", fg=GREEN)
        count_down(work_sec)
    #If reps is a multiple of 8 (indicating a long break).
    elif reps % 8 == 0:
        timer_label.config(text="LONG BREAK", fg=RED)
        count_down(long_break_sec)

    elif reps % 2 == 0:
        timer_label.config(text="SHORT BREAK", fg=PINK)
        count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(set_timer, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
            checkbox_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Technique")
window.config(padx=100, pady=60, bg=YELLOW)

timer_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=2, row=1)

canvas = Canvas(width=203, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
set_timer = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(column=2, row=2)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

checkbox_label = Label(fg=GREEN, bg=YELLOW)
checkbox_label.grid(column=2, row=4)

window.mainloop()
