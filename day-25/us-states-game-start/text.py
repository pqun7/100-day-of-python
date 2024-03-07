from turtle import Turtle

import pandas


class Text(Turtle):
    def __init__(self):
        super().__init__()
        pandas = __import__('pandas')
        self.file = pandas.read_csv(
            r"C:\Users\egtea\OneDrive\سطح المكتب\my projects\100 Day\day-25\us-states-game-start\50_states.csv")
        self.state_names_lower = self.file['state'].str.lower()
        self.state_has_print = []
        self.dict = {}
        #self.miss_list = []

    def printStates(self, answer):
        self.hideturtle()
        self.penup()
        self.speed(0)
        answer_lower = answer.lower()
        state_data = self.file[self.state_names_lower == answer_lower]
        if not state_data.empty:
            x_value = int(state_data['x'].iloc[0])
            y_value = int(state_data['y'].iloc[0])
            self.goto(x_value, y_value)
            if answer not in self.state_has_print:
                self.write(state_data.state.item())
            self.state_has_print.append(state_data.state.item())

    def MissState(self):
        # for st in self.state_names_lower:
        #     title_state = st.title()
        #     if title_state not in self.state_has_print:
        #         miss_list = [title_state]
        #         #self.miss_list.append(title_state)
        missing_list = [st.title() for st in self.state_names_lower if st not in self.state_has_print]
        print(self.state_has_print)
        print(missing_list)

        self.dict["missing state"] = missing_list

    def dic_to_csv(self):
        dic = pandas.DataFrame(self.dict)
        dic.to_csv(r"missing_state.csv")


