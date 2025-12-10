s = "Tejaswini Vishnu Dhanawade"

# Slicing and For loop Iteration

print("Name is", s, "and length is", len(s))

print(s[0:5])                       #Tejas
print(s[-26:-21])                   #Tejas
 
print(s[5:14])                      #wini Vish

print(s[-9: ])                      #Dhanawade

print(s[-16:-10])                   #Vishnu                    

print(s[-24:-16])                   #jaswini

print(s[ : :-1])                    #it will reverse all string

print(s[ : :2])                     #TjsiiVsn hnwd

print(s[5:16:3])                    #wiin

print(s[-1: :-2])                   #eaaaDuhi nwae


i = 0
for char in s:
    print(i, ">---", char)
    i = i+1


# Print each character in the string on a new line using a loop and skip 1 letter.
for char in s[0:len(s):2]:
    print(char)


# Count how many times the letter 'a' appears using a loop.
count = 0
for ch in s:
    if ch == "a":
        count = count+1 
print(f"Number of 'a' in above string i.e. in {s} is", count)              


# Count how many times the letter 'a' appears using a loop.
count = 0
for ch in s[10: :2]:
    if ch == "a":
        count = count+1 
print(f"Number of 'a' in above string i.e. in {s} is", count)          


# Print "Kaneri" after each letter
for char in s[17:]:
    print("Kaneri")
    print(char)


# Count how many times the letter 'i' appears using a loop.
i = 0
for ch in s[-16:-11]:
    if ch == "i":
        i = i+1
print(f"Number of 'i' in above string i.e. in {s} is", i)                


# Print the whole substring "Dhanawade" horizontally
for char in s[-9: ]:
    print(char, end=" ")  
print(">----------")
                              

# Print the string in reverse using slicing inside a loop.
for char in s[ : :-1]:
    print(char)


# Print wini Vish horizontally using loop
for char in s[-21:-12]:
    print(char, end="")