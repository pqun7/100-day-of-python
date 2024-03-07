#Add one for all numbers iin list
numbers = [1, 2, 3]
new_list = [item + 1 for item in numbers]
#print(new_list)
name = "Angle"
letters = [letter for letter in name]
#print(letters)

in_range = [number * 2 for number in range(1, 5)]
#print(in_range)
names = ["Ali", "Ahmed", "Bob", "Carol", "David"]
short_name = [name for name in names if len(name) < 5]
long_name = [name.upper() for name in names if len(name) >= 5]
print(long_name)