import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import ttk, Style

WORK_TIME = 1 * 60
SHORT_BREAK_TIME = 1 * 60
LONG_BREAK_TIME = 1 * 60

class PomodoroTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x200")
        self.root.title("Pomodoro Időzítő")
        self.style = Style(theme="simplex")
        self.style.theme_use()

        self.timer_label = tk.Label(self.root, text="", font=("TkDefaultFont", 40))
        self.timer_label.pack(pady=20)

        self.start_button = ttk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=5)

        self.stop_button = ttk.Button(self.root, text="Stop", command=self.stop_timer,
                                      state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.work_time, self.break_time = WORK_TIME, SHORT_BREAK_TIME
        self.is_work_time, self.pomodoros_completed, self.is_running = True, 0, False

        self.root.mainloop()

    def start_timer(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.is_running = True
        self.update_timer()
    
    def stop_timer(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.is_running = False

    def update_timer(self):
        if self.is_running:
            if self.is_work_time:
                self.work_time -= 1
                if self.work_time == 0:
                    self.is_work_time = False
                    self.pomodoros_completed += 1
                    self.break_time = LONG_BREAK_TIME if self.pomodoros_completed % 4 == 0 else SHORT_BREAK_TIME
                    messagebox.showinfo("Szép munka!" if self.pomodoros_completed % 4 == 0
                                        else "Szép munka!", "Tarts egy nagyobb szünetet és pihenj!"
                                        if self.pomodoros_completed % 4 == 0
                                        else "Tarts egy gyors szünetet és nyújtsd ki a lábad!")
            else:
                self.break_time -= 1
                if self.break_time == 0:
                    self.is_work_time, self.work_time = True, WORK_TIME
                    messagebox.showinfo("Munkaidő!", "Menj vissza dolgozni!")        
            minutes, seconds = divmod(self.work_time if self.is_work_time else self.break_time, 60)
            self.timer_label.config(text="{:02d}:{:02d}".format(minutes, seconds))
            self.root.after(1000, self.update_timer)

PomodoroTimer()