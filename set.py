 #1
age = int(input("жасынызды енгызыныз "))

if age >= 18:
     print("You are old enough to drive.")
else:
       years_left = 18 - age
print("You need to wait for", years_left, "more years to drive.")
#2
?
#3
a = int(input("сан енгызыныз: "))
b = int(input("сан енгызыныз: "))

if a > b:
    print("a дан улкен b")
elif a < b:
    print("a дан кишкентай b")
else:
    print("a тен b")
#4
?
#5
fruits = ["яблоко", "банан", "апельсин", "груша"]

fruit = input("Введите название фрукта: ")

if fruit not in fruits:
   fruits.append(fruit)
print(fruits)
    else:
print("Этот фрукт уже существует в списке")

