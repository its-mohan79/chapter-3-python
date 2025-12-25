name="mohan kumar"

print(len(name))

print(name.endswith("mar")) #  its used to find the string end with same string value given by the user and output is given true and false

print(name.startswith("moha"))

print(name.capitalize())

print(name.upper() )  # 'MOHANKUMAR'
print(name.lower() )  # 'mohankumar'
print(name.title() )   # 'Mohan Kumar'

print(name.casefold()) # 'mohankumar' it is used to convert the characters into lowercase for caseless matching
print(name.center(20,"#"))  # '#######mohan kumar#######'it is used to align the text in the center
print(name.count("mohan")) #it is used to find the number of same terms repeated
print(name.count("mohan",7,10))  # it is used to fined the value a specfic index
print(name.find("mohan",7,10)) # it is used to find the position of the string


str = "m\to\th\ta\tn"
print(str.expandtabs())  # it is used to replace the tab space with spaces
print(str.expandtabs(2))
print(str.expandtabs(3)) # change the size of spacing through the tab 


#python index() method

str1 ="this is first text"
print(str1.index('i'))
print(str1.index('i',3,10)) # it is used to find the index of the string value in a specific index range


#isalunum() method in python
str2 ="mohan123"
print(str2.isalnum())  # it is used to check whether the string contains only alphanumeric characters (letters and numbers) or not

#isalpha() method in python
str3 ="mohan"
print(str3.isalpha())  # it is used to check whether the string contains only alphabet

#isdecimal() method in python
str4 ="12345"
print(str4.isdecimal())  # it is used to check whether the string contains only decimal characters

#isdigit() method in python
str5 ="12345"
print(str5.isdigit())  # it is used to check whether the string contains only digits

#isidentifier() method in python
str6 ="mohan_kumar"
print(str6.isidentifier())  # it is used to check whether the string is a valid identifier or not

#islower() method in python
str7 ="mohankumar"
print(str7.islower())  # it is used to check whether the string contains only lowercase letters

#isupper() method in python
str8 ="MOHANKUMAR"  
print(str8.isupper())  # it is used to check whether the string contains only uppercase letters

# isnumeric() method in python
str9 ="12345"
print(str9.isnumeric())  # it is used to check whether the string contains only numeric

#isprintable() method in python
str10 ="mohannkumar"   
print(str10.isprintable())  # it is used to check whether all characters in the string are printable or not

#isspace() method in python
str11 ="  "    
print(str11.isspace())  # it is used to check whether the string contains only whitespace characters

#istitle() method in python
str12 ="Mohan Kumar"        
print(str12.istitle())  # it is used to check whether the string follows the title case format or not

#isupper() method in python
str13 ="MOHANKUMAR"
print(str13.isupper())  # it is used to check whether the string contains only uppercase letters

#python join() method
str14 = ("mohan","kumar","is","a","good","boy")
sep="$$"
print(sep.join(str14))  # it is used to join the elements of an iterable (like a

#lower() method in python
str15 ="MOHANKUMAR" 
print(str15.lower())  # it is used to convert the string into lowercase letters

#lstrip() method in python
str16 ="   mohan kumar   "      
print(str16.lstrip())  # it is used to remove the leading whitespace characters from the string

#replace() method in python
str17 ="mohan kumar"    
print(str17.replace("mohan","kumar"))  # it is used to replace a specified substring with another substring in the string

#rfind() method in python
str18 ="mohan kumar mohan"  
print(str18.rfind("mohan"))  # it is used to find the last occurrence of a specified substring in the string

#rindex() method in python
str19 ="mohan kumar mohan"
print(str19.rindex("mohan"))  # it is used to find the last occurrence of a specified substring in the string

#rjust() method in python
str20 ="mohan kumar"
print(str20.rjust(20,"#"))  # it is used to align the text to the right

#rsplit() method in python
str21 ="mohan,kumar,is,a,good,boy"
print(str21.rsplit(",",1))  # it is used to split the string from the right side 

#rstrip() method in python
str22 ="mohan kumar#####"
print(str22.rstrip("#"))  # it is used to remove the trailing whitespace characters from the string

#split() method in python
str23 ="mohan#kumar#is#a,good,boy"
print(str23.split("#",2))  # it is used to split the string into a list of substrings based on a specified delimiter

#splitlines() method in python
str24 ="mohan\nkumar\nis\na\ngood\nboy"
print(str24.splitlines(True))  # it is used to split the string at line breaks and return a list of lines
print(str24.splitlines(False))  # it is used to split the string at line breaks and return a list of lines

#startswith() method in python
str25 ="mohan kumar"
print(str25.startswith("mohan",20,25))  # it is used to check whether the string starts with a specified substring

#swapcase() method in python
str26 ="MoHaN KuMaR"
print(str26.swapcase())  # it is used to swap the case of all characters in the string

#title() method in python
str27 ="mohan kumar"
print(str27.title())  # it is used to convert the first character of each word in the string to uppercase

#upper() method in python
str28 ="mohan kumar"
print(str28.upper())  # it is used to convert the string into uppercase letters



#zfill() method in python
str29 ="mohan"  
print(str29.zfill(10))  # it is used to pad the string with zeros on the left side to fill a specified width
print(str29.zfill(8))  # it is used to pad the string with zeros on the left side to fill a specified width
print(str29.zfill(5))  # it is used to pad the string with zeros on the left side to fill a specified width

#strip() method in python
str30 ="   mohan kumar   "      
print(str30.strip())  # it is used to remove the leading and trailing whitespace characters from the string

