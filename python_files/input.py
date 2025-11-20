name = input("Enter your name: ") #use input for user inputs
print("Hello", name)

try: #use try-except blocks for when user inputs incorrect input type
    num = int(input("Enter a number: ")) #use int() to ensure input in an integer
    print(num)
    num = num * 2
    print(num)
except:
    print("You did not enter a number.")

#use print(___, end = " ") to continue printing on same line

print(f"Hello, my friend {name}") #f string to format exactly how string will print; uses curly braces

#reading files
with open("movies.txt") as file:
    for line in file:
        print(line.strip()) #if you use the .strip(), it will remove the space after each line

with open("heights.txt") as file:
    for line in file:
        print(line.strip())
        info = line.strip().split() #splits data in each line
        print(info)
        print(f"{info[0]} {info[1]} is {int(info[2])}      inches tall") #could use f string to put more spaces
        print(info[0], info[1], "is", int(info[2]), "inches tall")