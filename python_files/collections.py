cart = ["apples", "bananas", "cherries"]
cart.append("donuts")
cart.append("milk")
cart.append("eggs")
print(cart)

cart.remove("bananas")
print(cart)

cart.pop(2)
print(cart)
cart.pop()
print(cart)
cart.append("bananas")
cart.append("bananas")
print(cart)
cart.sort()
print(cart)
cart.reverse()
print(cart)
cart.reverse()
print(cart)

#slicing
fruit_basket = cart[2:4]
print(fruit_basket)

count_bananas = cart.count("bananas")
print(count_bananas)

squares = []
for i in range(1,5):
    squares.append(i*i)
print(squares)

startB = [item for item in cart if item.startswith("b")]
print(startB)

inventory = [0] * 10
inventory[4] = 100
print(inventory)

book_genres = {"mystery", "science fiction", "fantasy"}
book_genres.add("romance")
print(book_genres)

nums = [1,1,2,2,3,3,4,4,5,5]
unique = set(nums)
print(unique)

fav_snacks = {"kathleen":"chips","tarik":"candy", "jon":"cake"}
k_snack = fav_snacks["kathleen"]
print(k_snack)
fav_snacks["kathleen"] = "cheese"
for key in fav_snacks:
    print(key, fav_snacks[key])

for person, snack in fav_snacks.items():
    print(person, snack)

if "jack" in fav_snacks:
    print(fav_snacks("jack"))
else:
    fav_snacks["jack"] = "pop corners"