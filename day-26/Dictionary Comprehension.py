#Take value from a list or string
#new_dict = {New Key:new_value for item in list}

#Take value from a dict
#new_dict = {New Key:new_value for (key,value) in dict.items()}

#Take value from a dict and add conditional
#new_dict = {New Key:new_value for (key,value) in dict.items() if test}
import random
import pandas as pd

#Take value from a list
names = ["Alex", "Bob", "Charlie", "Ahmed"]
student_score = {student: random.randint(1, 100) for student in names}
#Take value from a dict
passd_student = {student_name: score for (student_name, score) in student_score.items() if score >= 60}
#print(passd_student)

dict_st = {"student": names, "score": [45, 96, 54, 65]}

#Loop in dict
for (kay, value) in dict_st.items():
    #print(value)
    pass

frame_dict = pd.DataFrame(dict_st)
for (kay, value) in frame_dict.items():
    #print(kay)
    pass


#Loop in dict Bast Way
for (index, row) in frame_dict.iterrows():
    #print(row.student)
    pass

#in comprehension
dict_com = {index: row for (index, row) in frame_dict.iterrows()}


