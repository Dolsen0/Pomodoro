import tkinter as tk

def format_time(seconds):
    return f"{seconds//60:02d}:{seconds%60:02d}"

def start_countdown(countdown_label, countdown_time, alternate_countdown_time):
    def update_countdown(countdown, countdown_time, alternate_countdown_time):
        countdown -= 1
        countdown_label.config(text=format_time(countdown))
        if countdown == 0:
            countdown_time, alternate_countdown_time = alternate_countdown_time, countdown_time
            countdown = countdown_time
        countdown_label.after(1000, update_countdown, countdown, countdown_time, alternate_countdown_time)

    countdown = countdown_time
    countdown_label.config(text=format_time(countdown))
    countdown_label.after(1000, update_countdown, countdown, countdown_time, alternate_countdown_time)

root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("300x100") # Set the size to 300x100 pixels

countdown_label = tk.Label(root, text="", font=("Helvetica", 24))
countdown_label.pack(padx=20, pady=20)

start = 1500
pause = 300

start_countdown(countdown_label, start, pause)

root.mainloop()