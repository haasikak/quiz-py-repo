
from tkinter import *
from tkinter import messagebox as mb
import json

class Quiz:
    def __init__(self):
        self.q_no = 0
        self.correct = 0

        self.time_per_question = 15  # seconds per question
        self.remaining_time = self.time_per_question

        self.opt_selected = IntVar()

        self.display_title()
        self.display_question()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
        self.display_timer()
        self.update_timer()

        self.data_size = len(question)

    def display_result(self):
        wrong_count = self.data_size - self.correct
        score = int(self.correct / self.data_size * 100)

        gui.destroy()

        final_window = Tk()
        final_window.title("Quiz Completed")
        final_window.geometry("500x300")
        final_window.configure(bg="white")

        Label(final_window, text="Quiz Completed!", font=("Arial", 24, "bold"), fg="#333333", bg="white").pack(pady=20)
        Label(final_window, text=f"Your Score: {score}%", font=("Arial", 18), bg="white").pack(pady=10)
        Label(final_window, text=f"Correct Answers: {self.correct}", font=("Arial", 16), bg="white").pack()
        Label(final_window, text=f"Wrong Answers: {wrong_count}", font=("Arial", 16), bg="white").pack()
        Label(final_window, text="Thank you for participating in the Python Quiz!", font=("Arial", 14), bg="white").pack(pady=20)

        Button(final_window, text="Exit", command=final_window.destroy,
               font=("Arial", 14), bg="#555555", fg="white").pack(pady=10)

        final_window.mainloop()

    def check_ans(self, q_no):
        return self.opt_selected.get() == answer[q_no]

    def next_btn(self):
        if self.check_ans(self.q_no):
            self.correct += 1
        self.q_no += 1
        if self.q_no == self.data_size:
            self.display_result()
        else:
            self.display_question()
            self.display_options()
            self.remaining_time = self.time_per_question  # reset timer

    def buttons(self):
        next_button = Button(gui, text="Next", command=self.next_btn,
                             width=10, bg="#4a90e2", fg="white", font=("Arial", 16, "bold"))
        next_button.place(x=350, y=380)

        quit_button = Button(gui, text="Quit", command=gui.destroy,
                             width=5, bg="#777777", fg="white", font=("Arial", 16, "bold"))
        quit_button.place(x=700, y=50)

    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    def display_question(self):
        gui.configure(bg="white")
        q_no = Label(gui, text=question[self.q_no], width=60, bg="white",
                     font=('Arial', 16, 'bold'), anchor='w')
        q_no.place(x=70, y=100)

    def display_title(self):
        title = Label(gui, text="Python Quiz Challenge",
                      width=50, bg="#4a90e2", fg="white", font=("Arial", 20, "bold"))
        title.place(x=0, y=2)

    def radio_buttons(self):
        q_list = []
        y_pos = 150
        while len(q_list) < 4:
            radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("Arial", 14), bg="white")
            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 40
        return q_list

    def display_timer(self):
        self.timer_label = Label(gui, text=f"Time left: {self.remaining_time} seconds",
                                 font=("Arial", 14), fg="#b22222", bg="white")
        self.timer_label.place(x=600, y=100)

    def update_timer(self):
        self.timer_label.config(text=f"Time left: {self.remaining_time} seconds")
        if self.remaining_time > 0:
            self.remaining_time -= 1
            gui.after(1000, self.update_timer)
        else:
            self.next_btn()

def start_quiz():
    welcome_frame.destroy()
    Quiz()

gui = Tk()
gui.geometry("800x450")
gui.title("Python Quiz Application")

welcome_frame = Frame(gui, bg="white")
welcome_frame.pack(fill="both", expand=True)

welcome_label = Label(welcome_frame, text="Welcome to the Python Quiz Challenge!",
                      font=("Arial", 24, "bold"), fg="#333333", bg="white")
welcome_label.pack(pady=100)

start_button = Button(welcome_frame, text="Start Quiz", command=start_quiz,
                      font=("Arial", 18, "bold"), bg="#4a90e2", fg="white", width=12)
start_button.pack()

with open('data.json') as f:
    data = json.load(f)

question = data['question']
options = data['options']
answer = data['answer']

gui.mainloop()
  