print("Exercise 1")
for i in range(1,21):
   if i % 3 == 0:
        print(i)

print()
print("Exercise 2")
count = 0
num = 1
while num <= 50:
    if num % 2 == 0:
        count = count + num
    num = num + 1
print(count)

print()
print("Exercise 3")
numbers = [5,8,2,15,10,3,7]
for num in numbers:
    if num > 5:
        print(num)

print()
print("Challenge")
lst = [1,2,3,4,5]
lst2 =[]
lst2.append(lst[0])
for i in range(1,len(lst)):
    lst2.append(lst2[i-1]+lst[i])
print(lst2)

print()
print("Functions")
lst = [0,3,8,4,5]

def swap(lst):
    tmp = lst[0]
    lst[0] = lst[len(lst)-1]
    lst[len(lst)-1] = tmp

swap(lst)
print(lst)