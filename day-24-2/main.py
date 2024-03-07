with open(r"C:\Users\egtea\OneDrive\سطح المكتب\my projects\100 Day\day-24-2\name.txt", "w") as name:
    name.write("ali\n")
    name.write("nazer")

with open(r"C:\Users\egtea\OneDrive\سطح المكتب\my projects\100 Day\day-24-2\name.txt", "r") as r:
    liine = r.readlines()
    print(liine[0])