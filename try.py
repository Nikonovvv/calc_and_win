class Human:
    def __init__(self, name):
        self.name = name
        
    # ответ по умолчанию для всех одинаковый, можно 
    # доверить его родительскому классу
    
    def answer_question(self, question=None):

        print('Очень интересный вопрос! Не знаю.')

class Student(Human):
    def __init__(self, name, question):
        super().__init__(name)
        self.question = question
        
    def answer_question(self, question=None): 
        self.question = question  
        if self.question != 'Вопрос':
            print('Привет')
        else:
            return super().answer_question()

ada = Student('Мария', 'Вопрос')

ada.answer_question()
