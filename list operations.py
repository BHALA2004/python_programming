fruits=["orange","apple"]
fruits.append("kiwi")
new_fruits=["Tomato"]
fruits.extend(new_fruits)

print(fruits)

fruits.insert(1,"banana")
print(fruits)

fruits.remove("apple")
print(fruits)

print(fruits.index("banana"))
print(fruits.pop())
fruits.sort()
print(fruits)
print(fruits[:1])
print(fruits.pop(1))

fruits.append(4)
print(fruits)

