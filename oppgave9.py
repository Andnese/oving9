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
        if your_answer == self.right_answer:
            print("This is correct")

        else:
            print("This is in-correct")

    def correct_answer_text(self):
        right_answer_nr = int(self.right_answer)
        return "Det rette svaret er: " + words[right_answer_nr]

    def points(self, answer_user):
        point = 0
        svar = int(self.right_answer)
        if answer_user == svar:
            point = 1
        return point


if __name__ == "__main__":
    import math

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
            points_player1 += Q.points(player1_answer)
            points_player2 += Q.points(player2_answer)
            options.clear()
            print("")

    print(f"The total points racked up py player one is {points_player1}")
    print(f"The total points racked up py player two is {points_player2}")
