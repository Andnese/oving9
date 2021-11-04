class Question:
    # constructor
    def __init__(self, questions, answers, right_answer):
        self.question = questions
        self.answer = answers
        self.right_answer = right_answer

    def __str__(self):
        print(self.question)
        counter = 0
        print("select one of the options: ")
        for i in self.answer:
            counter += 1
            print(f"{counter} : {i}")

    def check_answer(self, your_answer):
        if your_answer == self.right_answer:
            print("This is correct")
        else:
            print("This is in-correct")


