from tkinter import *
from tkinter import messagebox as mb
import json

q = Tk()
q.geometry("800x450")
q.title("Quiz App")
q.configure(bg="lightblue")

class Quiz:
    def __init__(self):
        self.q_no = 0
        self.dis_question()
        self.selected = IntVar()
        self.opts = self.radio()
        self.dis_options()
        self.buttons()
        self.data_size = len(question)
        self.correct = 0
        self.y_pos = 0

    def dis_result(self):
        resbox=Text(self.r,font=("Arial",15),width=30,height=10)
        resbox.pack()
        resbox.delete('1.0',END)
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}\n"
        wrong = f"Wrong: {wrong_count}\n"
        score = int(self.correct / self.data_size * 100)
        res = f"Score: {score}%\n"
        resbox.insert(END,correct+wrong+res)
    def result(self):
        self.r=Tk()
        self.r.title("Result")
        self.r.geometry("400x400")
        self.r.configure(bg="lightblue")
        res=Button(self.r,text="Result",command=self.dis_result,bg="orange",font=("Arial",20))
        res.pack(pady=20)
        self.r.mainloop()

    def check_ans(self, q_no):
        if self.selected.get() == answer[q_no]:
            return True

    def next_btn(self):
        if self.check_ans(self.q_no):
            self.correct += 1
        
        self.q_no += 1
        
        if self.q_no == self.data_size:
            q.destroy()
            self.result()
        else:
            self.dis_question()
            self.dis_options()

    def buttons(self):
        self.next_button = Button(q, text="Next", command=self.next_btn, width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))
        self.next_button.place(x=350, y=380)
        
        self.quit_button = Button(q, text="Quit", command=q.destroy, width=5, bg="black", fg="white", font=("ariel", 16, "bold"))
        self.quit_button.place(x=700, y=50)

    def dis_options(self):
        val = 0
        self.selected.set(0)
        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    def dis_question(self):
        self.ques = Label(q, text=question[self.q_no], width=60, font=('ariel bold', 16), anchor="w", bg="lightblue")
        self.ques.place(x=70, y=100)

    def radio(self):
        q_list = []
        self.y_pos = 150
        while len(q_list) < 4:
            self.radio_btn = Radiobutton(q, text=" ", variable=self.selected, value=len(q_list) + 1, font=("ariel", 14), bg="lightblue")
            q_list.append(self.radio_btn)
            self.radio_btn.place(x=100, y=self.y_pos)
            self.y_pos += 40
        return q_list

	

def start_quiz():
    start.destroy()
    welcome.destroy()
    rule.destroy()
    rules.destroy()
    quiz = Quiz()


d = open("questions.json")
data = json.load(d)
question = data['question']
options = data['options']
answer = data['answer']

welcome = Label(q, text="Welcome", font=("Arial Bold", 20), bg="lightblue")
welcome.pack(pady=10)

rule = Label(q, text="Rules", font=("Arial", 15), bg="lightblue")
rule.pack(pady=10)

rules = Label(q, text="1. No use of external aids or search engines during the quiz\n2. Each correct answer will be awarded one(1) point.\n3. Results will be declared once you submit your quiz",
              font=("Arial", 12), bg="lightblue")
rules.pack(pady=10)

click=Label(q,text="Click start button when you are ready",font=("Arial",15),bg="lightblue")
click.pack(pady=10)

start = Button(q, text="Start", command=start_quiz, font=("Arial Bold", 15))
start.pack(pady=10)

q.mainloop()
