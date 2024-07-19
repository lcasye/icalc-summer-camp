from tkinter import *
from tkinter import messagebox

class Quiz:
    def __init__(self):
        self.questions = [
            {'questions':'Capital of France','options':['Paris','London','Ottawa','Moscow'],'answer':'Paris'},
            {'questions':'2+2','options':['6','4','8','10'],'answer':'4'},
            {'questions':'Color of Water','options':['Yellow','No Color','Red','Green'],'answer':'No Color'},
            {'questions':'What is Sand made of','options':['S','Si','SiO2','Ti'],'answer':'SiO2'},
            {'questions':'4^2','options':['15','16','17','18'],'answer':'16'},
            {'questions':'Which is a Snake?','options':['Hedgehog','Python','Rabbit','Silver'],'answer':'Python'}
        ]
        self.score = 0
        self.current_question = 0

    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_question]['answer']
        if selected_option == correct_answer:
            self.score = self.score + 1
            return True
        else:
            return False

    def next_question(self):
        self.current_question = self.current_question + 1
        if self.current_question < len(self.questions):
            return True
        else:
            return False



class App(Tk):
    def __init__(self,quiz):
        Tk.__init__(self)
        self.title('quiz')
        self.my_quiz = quiz
        self.config(bg='lightblue')
        self.geometry('600x400')
        #title
        self.title = Label(self,text='Quiz Moment')
        self.title.config(font=('Corbel',15))
        self.title.pack(pady=10)
        #question
        self.question_label = Label(self,text='',wraplength=400)
        self.question_label.config(font=('Ubuntu',12))
        self.question_label.pack(pady=20)
        #options
        self.option_list = StringVar(value='')
        self.option_button = []

        for i in range(4):
            rb = Radiobutton(self,text='',variable=self.option_list,value='')
            rb.pack(anchor=W,padx=20,pady=5)
            self.option_button.append(rb)
        #submit
        self.submit_button = Button(self,text='do it', command=self.submit_answer)
        self.submit_button.config(font=('Arial',12))
        self.submit_button.pack(pady=20)
        #answer
        self.answer_label = Label(self,text='')
        self.answer_label.config(font=('Courier',12))
        self.answer_label.pack(pady=20)
        #score
        self.score_label = Label(self,text='Score: 0')
        self.score_label.config(font=('Courier',12))
        self.score_label.pack(pady=10)
        self.load_question()

    def load_question(self):
        question_data = self.my_quiz.questions[self.my_quiz.current_question]
        self.question_label.config(text=question_data['questions'])
        self.option_list.set('')

        for index,option in enumerate(question_data['options']):
            self.option_button[index].config(text=option, value=option)

    def submit_answer(self):
        selected_option = self.option_list.get()
        correct = self.my_quiz.check_answer(selected_option)
        if correct:
            self.answer_label.config(text='Correct', fg='green')
        else:
            correct_answer = self.my_quiz.questions[self.my_quiz.current_question]['answer']
            self.answer_label.config(text=f'Wrong, Correct Answer is {correct_answer}', fg='red')

        self.score_label.config(text=f'Score: {self.my_quiz.score}')

        if self.my_quiz.next_question():
            self.load_question()
        else:
            self.end_quiz()

    def end_quiz(self):
        messagebox.showinfo('Quiz Completed',f'Your Score: {self.my_quiz.score}/{len(self.my_quiz.questions)}')
        self.submit_button.config(state=DISABLED)

#launch
my_quiz = Quiz()
App(my_quiz)
mainloop()

