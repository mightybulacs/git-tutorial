fruits = ["mango", "banana", "guava", "banana"]
print(len(fruits))
print(fruits.count("banana"))
for fruit in fruits:
	print(fruit)
print(fruits[2])
fruits.append("apple")
print(fruits)
#fruits.pop(3)
#print(fruits)
fruits.remove("banana")
print(fruits)
fruits.insert(0, "guyabano")
print(fruits)
fruits.insert(len(fruits), "chico")
print(fruits)
fruits.sort(reverse=True)
print(fruits)
print(fruits.index("apple"))
index = fruits.index("apple")
fruits.remove("apple")
print(fruits)
fruits.insert(index, "watermelon")
print(fruits)
vegetables = ["radish", "cucumber"]
fruits.extend(vegetables)
print(fruits)
things_i_hate = fruits[:]
things_i_hate.insert(0, "xxx")
print(fruits)
print(things_i_hate)
things_i_eat = fruits
things_i_eat.insert(0, "yyy")
print("-" * 16)
print(fruits)
print(things_i_eat)
del things_i_eat[:]
print(fruits)