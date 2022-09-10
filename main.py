from tkinter import *
import  math
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
marks = " "


# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)

    # Timer reset
    canvas.itemconfig(timer_min_text, text="00:")
    canvas.itemconfig(timer_sec_text, text="00")

    # Title reset
    timer_label.config(text="Timer")

    # Checkmarks reset
    tick_label.config(text=" ")

    global reps
    reps = 0





def count_down(count):
    global reps
    global timer
    min =math.floor(count/60)
    sec = count%60
    if sec < 10 or sec == 0:
        sec = f"0{sec}"
    canvas.itemconfig(timer_min_text, text=f"{min}:")
    canvas.itemconfig(timer_sec_text, text=f"{sec}")
    if count>0:
        timer = window.after(1000, count_down, count-1)
    elif count == 0:
        reps = reps + 1
        call_count_down()



def call_count_down():
    global reps
    global marks
    global tick_label
    if (reps == 0 or reps%2 == 0) and reps < 8:
        marks += "✔"
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN, bg=YELLOW)
        tick_label.config(text=marks)

    elif reps%2 != 0 and reps < 6:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Short Break", fg=PINK, bg=YELLOW)
    elif reps == 6:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Long Break", fg=RED, bg=YELLOW)



# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)
# window.minsize()

# canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0 )
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100 , 112, image=tomato_img)
timer_min_text = canvas.create_text(70, 130, text="00:", fill="white", font=(FONT_NAME, 35, "bold"))
timer_sec_text = canvas.create_text(140, 130, text="00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

timer_label = Label(text="Timer", font=("Arial", 24, "bold"), fg=GREEN, bg=YELLOW,)
timer_label.grid(column=1,row=0)

start_button = Button(text="Start", highlightthickness=0, command=call_count_down)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3,row=2)

tick_label = Label(text="", fg=GREEN, bg= YELLOW)
tick_label.grid(column=1,row=4)







window.mainloop()