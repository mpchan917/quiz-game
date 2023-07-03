class QuizBrain:

    def __init__(self,list):
        self.question_number =0
        self.question_list = list
        self.score =0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        n_quest= self.question_list[self.question_number]
        self.question_number +=1
        p_answer =input(f"Q.{self.question_number}: {n_quest.text} (True/False)?: ")
        self.check_answer(p_answer, n_quest.answer)

    def check_answer(self,p_answer, correct_answer):
        if p_answer == correct_answer:
            print("You're right!")
            self.score +=1
        else:
            print("You're wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your curent score is: {self.score}/{self.question_number}.")
        print("\n")



