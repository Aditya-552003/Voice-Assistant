import random
import string as st

char = ""
length = int(input("Enter size of password: "))
letters = input("Include letters? (y/n): ")
numbers = input("Include numbers? (y/n): ")
symbols = input("Include symbols? (y/n): ")

if letters == "y":
    char += st.ascii_letters
if numbers == "y":
    char += st.digits
if symbols == "y":
    char += st.punctuation
 
if char: 
    password = "".join(random.choices(char, k=length))
    print("Your password is:", password)
else:
    print("You must include at least one type of character for the password!")
