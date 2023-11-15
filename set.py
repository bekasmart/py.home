citiz= {"alvfti","astana", "aktay", "alatau" ,"povladar"}
# print(len(citiz))
citiz.add("tokyo")
print(len(citiz))

new_city =input("America")
citiz.add("new_siti")
print(citiz)

new_city=input("Enter a city:")

if new_city in citiz:
    citiz.remove(new_city)
    print(f"{new_city} was removed from the set")
else: 
    print("No such city")

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

it_companies.add("Twitter")
print(it_companies)
 
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
companies ={"avon","gugshy","raf","addidas"}
it_companies.update(companies)


#2 тапсырманын 1ыншысы
A = {1, 2, 3}
B = {3, 4, 5}
union = A.union(B)
print(union)
#2
A = {1, 2, 3}
B = {3, 4, 5}
nam = A.nam(B)
print(nam) 
#3
A = {1, 2}
B = {1, 2, 3, 4, 5}
set = A.set(B)
print(set)
#4
A = {1, 2}
B = {3, 4}
dis = A.dis(B)
print(dis)
#5
A = {1, 2, 3}
B = {3, 4, 5}
join = A + B
print(join)
#6
#7
#3тапсырма 1
age_list = [21, 39, 21, 38, 30]
set = set(age_list)
print(len(age_list)) 
print(len(set))   
#2
#3
