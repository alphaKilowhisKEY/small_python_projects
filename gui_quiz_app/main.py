
"""
Quizzier - A simple quiz application using tkinter

This Python script creates a simple quiz application using the tkinter library. It displays questions one by one and allows users to answer by clicking on True or False buttons. After answering, it provides immediate feedback by changing the background color of the question area to green (for correct) or red (for incorrect). At the end of the quiz, it displays the user's final score.

Libraries Used:
- tkinter: for building the graphical user interface
- quiz_brain: for managing the quiz questions and answers

Global Variables:
- THEME_COLOR: Theme color used for the background
- FONT: Font configuration for text

Classes:
- QuizInterface: Class representing the GUI of the quiz application
- QuizBrain: manages the list of questions, keeps track of the current question number and score, 
   provides methods to retrieve the next question, check the user's answer, and determine if there are any remaining questions.
- Qestion: represents a single question in a quiz.

Usage:
- Run the script to start the quiz application: $python3 main.py
"""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")