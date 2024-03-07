
# TODO - asking the questions
class Quiz_Brain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.final_result = 0
    
    def next_question(self):
            global ask1
            global question_number
            current_querstion = self.question_list[self.question_number]
            ask1 = input(f"Q.{self.question_number}: {current_querstion.tx} (True, False): ")
    def still_has_question(self):
            ask_lower = ask1.lower()
            current_querstion = self.question_list[self.question_number]
            if ask_lower == current_querstion.an.lower():
                self.question_number += 1
                self.final_result += 1
                print("You Got it right!")
                print(f"The Correct answer: {current_querstion.an}.")
                print(f"your correct score: {self.final_result}/{self.question_number}.")
                print("\n")
            else:
                self.question_number += 1
                print("You answered incorrectly")
                print(f"The Correct answer: {current_querstion.an}.")
                print(f"Your final result: {self.final_result}/{self.question_number}.")
                print("\n")
            if self.question_number == len(self.question_list):
                exit()
        
        




