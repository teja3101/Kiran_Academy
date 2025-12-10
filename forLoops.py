s = "instagram"

#For loop manages all things internally, 'in' is the operator

# for char in s:
#     print(char)
#     print("Pune")

# i = 0 
# for char in s:
#     print(i, ">-----", char)
#     i = i+1

# find total no. of "a" in your string
count = 0
for ch in s:
    if ch=='a':
        count = count+1
print(f"Total count of 'a' in {s} = ", count)

for char in s[0:5]:
    print(char)