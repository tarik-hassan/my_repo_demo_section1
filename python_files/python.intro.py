print("hello world!")

# single line comment

'''
multi line comment uses triple quotes
and is placed between them.
'''

x = 100 # don't need to declare data types in Python
y = 10.1
x = "hello" # can change variable type
print(x)

# Math operators
x = 100
y = 10
z = x // y # floor division keeps variable as an integer
print(z)
# z = int(z)
# print(z)

min_val = min(10,1) # finds minimum value
print(min_val)
raised = pow(2,4) # raises first number to power of the second
raised = 2**4 # alternate way of doing powers
print(raised)

if x < 0:   # if statements end with a colon
    print("negative")   #code should be indented 
else:
    print("positive")

if x < 0 and y < 0: # directly write 'and' or 'or'
    print("negative")
if x < 0 or y < 0:
    print("one negative")

if x < 0:
    print("negative")
elif y < 0:
    print("negative")
else:
    print("positive")

counter = 0
while counter < 10:
    print(counter)
    counter = counter + 1 # or can put counter += counter

# range(start,end,inc):

a_list = [1,2,3,4,5]

for i in range(5):
    print(i, a_list[i])

for i in range(len(a_list)):
    print(i, a_list[i])

for i in range(len(a_list)-1,-1,-1):
    print(i, a_list[i])

for i, val in enumerate(a_list):
    print(i, val)

for value in a_list:
    print(value, end = " ")

print()
#creating fucntions using def, followed by name and parameters
def hello_world():
    print("hello world")
hello_world()

def hello(name = "Jack"):
    print("Hello", name)
    #can combine by using a + instead of a ,
    #use ="" to give a default if no parameter is given

hello("Bob")
hello()

full_name = "Tarik Hassan"
first = full_name[0]
last = full_name[-1]

#to slice a string str[start.index: end.index]

first_name = full_name[0:5] #can omit first number, will assume starting at beginning of string
print(first_name)
last_name = full_name[6:12] #can omit last number, will assume go til end of string
print(last_name)