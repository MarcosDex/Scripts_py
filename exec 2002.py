list1 = ['a','b','c']
list2 = ['1','2','3']

list1.extend(list2)
print(list1)

list3 = ['a','b','c']
list4 = [1, 2, 3]

for y in list4:
    list3.append(y)

    print(list3)

    list5 = ['a', 'b','c']
    list6 = [1, 2 ,3]
    list7 = list5 + list6
    print(list7)
