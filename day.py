# print('hello world "')
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print("Hello, " + name + "!")
# print("your age is:", age)





# # conditional loop
# a =  int(input("Enter a number: "))
# b =  int(input("Enter another number: "))
# if a > b:
#     print("a is greater than b")
# elif a < b:
#     print("a is less than b")

# else:
#     print("a is equal to b")




#while loop
# list , dictionary and tupple


# countries = ["India", "USA", "UK", "Canada"]
# countries.insert(2, "Bangladesh")
# countries.append("Australia")
# print(countries)
# # countries.remove("USA")
# countries.pop(1)
# print(countries)
# del countries[3]
# print(countries)


# # countries.clear()
# print(countries)


# print(len(countries))

# print("welcome", countries[0])
# print(countries[-1])

# for desh in countries:
#     print(desh)
#     print("------")
    

# for coun in countries:
#     if coun.lower() == "uk":
#         print("beautiful country")
#         continue
#     else:
#         print("notfound")







# tupple (mutable and immutable)

names = ("Alice", "Bob", "Charlie")
print  (names)
nam = list (names)
nam.append("David")
print(nam)


print(len(nam))
numbers = (1, 2, 3, 4, 5)
print(numbers)

names1 = tuple(nam)
print(names1)

nameee = names + numbers
print(nameee)
print(len(nameee))
