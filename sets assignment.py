# store multiple items in a single variable
# unordered so can't be accessed using indeces
#  unchangeable but one can remove and add new items


# print(set1)
# duplicates in sets
set1 = {"matooke","fish","potato","potato"}
print(set1)
# exercise find the length of your set,data type,accessing items in a set ,add items,add two sets together
# getting the size of your set
print(len(set1))
# getting the type of set
print(type(set1))
this_set = {"pineapple", "pawpaw", "grapes"}
# acessing items in a set
for x in set1:
  print(x)
# adding items to a set
set1.add("oranges")
print(set1)
# for adding many items to the set
this_set.update(["guava","jackfruit","passion"])
print(this_set)
# adding two sets together
# union and update includes all duplicates
set3 = set1.union(this_set)
print(set3)
"""
  set3 = {"jelly","jonath","joan"}
  set4 = {"judith","jolly","hillary"}
  set5 = set(("enoch","rollings","elly")) #using a constructor to create a set
  #empties the set
  #set5.clear()
  print(set5)
  #deletes the set completely
  del set5
  print(set5)
  z = set3.difference(set4)
print(z)
"""
