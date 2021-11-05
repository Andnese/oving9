class Question:
    # constructor
    def __init__(self, questions, answers, right_answer):
        self.question = questions
        self.answer = answers
        self.right_answer = right_answer

    def __str__(self):
        spm = self.question + "\n"
        for i, string in enumerate(self.answer):
            spm += str(i + 1) + ": " + string + "\n"
        return spm

    def check_answer(self, your_answer):
        answer = your_answer - 1
        if answer == int(self.right_answer):
            return "correct"

        else:
            return "incorrect"

    def correct_answer_text(self):
        right_answer_nr = int(self.right_answer)
        answers = self.answer
        return "The correct answer is: " + answers[right_answer_nr]

if __name__ == "__main__":

    options = []
    points_player1 = 0
    points_player2 = 0

    with open('sporsmaalsfil.txt', "r", encoding="UTF8") as read_file:
        for row in read_file:
            words = row.replace(",", ":").replace("[", "").replace("]", "").split(":")
            question = words[0]
            right_answer = words[1]
            lenth = len(words)
            for i in range(2, lenth):
                options.append(words[i])
            Q = Question(question, options, right_answer)
            print(Q)
            player1_answer = int(input("Player one, choose your answer: "))
            player2_answer = int(input("Player two, choose your answer: "))
            print(Q.correct_answer_text())
            print(f"Player one: {Q.check_answer(player1_answer)}")
            print(f"Player two: {Q.check_answer(player2_answer)}")
            options.clear()
            print("")
