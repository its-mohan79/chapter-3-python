#problem 1
name=input("enter your name:")
print(f"good afternoon,{name}")

#problem 2
letter='''Dear<|name|>,
You are selected!
Date:<|date|>, post:<|manager|>'''

print(letter.replace("<|name|>","Mohan").replace("<|date|>","5th june 2023").replace("<|manager|>","HR"))

#problem 3

name1="mohan is a good  boy and he is a student"

print(name1.find("  "))

#problem 4

name2="mohan is a good  boy and he is a student"

print(name2.replace("  "," ")) # string are immutable which means that you cannot change them by running function on them


#problem 5

letter2="Dear mohan,\n\t this is python course is nice.\nThanks!"
print(letter2)
