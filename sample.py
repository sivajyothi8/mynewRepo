# Python program to find sum of elements in list

total = 0

# creating a list
list1 = [11, 5, 17, 18, 23]

# Iterate each element in list
# and add them in variable total
for ele in range(0, len(list1)):
	total = total + list1[ele]

# printing total value
print("Sum of all elements in given list: ", total)
l2= lambda x:x**3
list2 = [l2(a) for a in list1]
print("Cube of list1 using lambda and comprehension;List2:",list2)
list2 = list(map(lambda x:x**3,list1))
print("Cube of list1 using list and map;List2:",list2)
list3=[x for x in list2 if x%5==0]
print("list2 comprehension that are divisible by 5; List3:",list3)
list3 = list(filter(lambda x:x%12==0,list2))
print("list2 divisible by 3 or 4 or both using list and filter;List3:",list3)
