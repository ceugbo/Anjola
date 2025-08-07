my_list = []
#print('Before Append:', my_list)
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print('After Append:', my_list)
my_list.insert(1, 15)
print(my_list)
greet = [50,60,70]
my_list.extend(greet)
print(my_list)
del my_list[7]
print(my_list)
my_list.sort()
print('Sorted list', my_list)
print(my_list[3])
