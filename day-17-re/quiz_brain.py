class Quiz_Brain:
    def __init__(self, question_list):
        self.question_number = 0
        self.ql = question_list
    
    def still_has_question(self):
        if self.question_number < len(self.ql):
            return True
        else:
            return False    
    def next_question(self):
        current_querstion = self.ql[self.question_number]
        input(f"Q.{self.question_number}: {current_querstion.text}, (True, False): ")
