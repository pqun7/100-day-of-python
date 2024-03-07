# file = open("my_file.txt")
#TODO - Read The File
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
# # TODO - write in the file
# # TODO - To delete the previous text mode="w"
# with open("my_file.txt", mode="w") as file:
#     file.write("My Age is 18")
#
# # TODO - Add a new line mode="a"
# with open("my_file.txt", mode="a") as file:
#     file.write("\nMy Age is 18")
with open(r"../../../my_file.txt") as file:
     contents = file.read()
     print(contents)