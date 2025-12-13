# s = "Welcome to the Python World!"
# count = 0
# for ch in s:
#     if ch == " ":
#         count = count+1
# print(f"There are {count} white spaces in {s}")

a = input("Enter any string = ")
char = input("Enter any char to find count = ")
count = 0
for ch in a:
    if ch == char:
        count = count+1
print(f"There are {count} {char}'s in {a}")

