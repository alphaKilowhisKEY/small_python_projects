from tkinter import *
from quiz_brain import QuizBrain
from tkinter import messagebox

THEME_COLOR = "#375362"
FONT = ("Courier", 20, "bold")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzier")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        #Window with Question Text
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.quesion_text = self.canvas.create_text(150, 125, text="TEXT", width=260, font=FONT, fill="black")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        #Button Cross
        self.button_image_cross = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=self.button_image_cross, highlightthickness=0, command=self.give_false)
        self.cross_button.grid(column=0, row=2)

        #Button Check
        self.button_image_check = PhotoImage(file="images/true.png")
        self.check_button = Button(image=self.button_image_check, highlightthickness=0, command=self.give_true)
        self.check_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):  
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quesion_text, text=q_text)
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            messagebox.showinfo(title="Finish", message=f"You've completed the Quiz. Your final score is {self.quiz.score} / {self.quiz.question_number}")
            self.canvas.config(bg="white")
            self.check_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def give_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
 
    def give_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right): 
        if is_right:
            self.canvas.config(bg="green")
           
        else:
            self.canvas.config(bg="red") 

        self.window.after(1000, self.get_next_question)