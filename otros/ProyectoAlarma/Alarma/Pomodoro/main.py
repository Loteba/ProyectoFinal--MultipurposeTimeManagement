import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25*60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60
counter = 0
mark = ""
timer = None
reset_pressed = False
start_pressed = False


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global counter, mark, reset_pressed, start_pressed

    if not start_pressed:
        pass
    else:
        counter = 0
        mark = ""
        window.after_cancel(timer)
        timer_label.config(text="Tiempo ", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
        canvas.itemconfig(timer_text, text="00:00")
        timer_check.config(text=mark)
        start_pressed = False


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global start_pressed
    if start_pressed:
        reset_timer()
    else:
        timer_label.config(text="Tiempo de Trabajo", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
        start_pressed = True
        count_down(WORK_MIN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global counter
    global mark
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        canvas.itemconfig(timer_text, text=f"{count_min}:0{count_sec}")
    else:
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count >= 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        counter += 1
        if counter < 7:
            if counter % 2 != 0:
                mark += "✓"
                timer_check.config(text=mark)
                timer_label.config(text="Break time", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
                count_down(SHORT_BREAK_MIN)
            else:
                timer_label.config(text="Working time", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
                count_down(WORK_MIN)
        elif counter == 7:
            mark += "✓"
            timer_check.config(text=mark)
            timer_label.config(text="Break time", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
            count_down(LONG_BREAK_MIN)
        else:
            timer_label.config(text="Finished section", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
            canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW)
photo = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=photo)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start = tkinter.Button(text="Iniciar", command=start_timer)
start.grid(column=0, row=2)

reset = tkinter.Button(text="Resetear", command=reset_timer)
reset.grid(column=2, row=2)

timer_label = tkinter.Label(text="Tiempo", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

timer_check = tkinter.Label(fg=GREEN, font=("Arial", 12, "bold"), bg=YELLOW)
timer_check.grid(column=1, row=3)

window.mainloop()
