# ################ Створити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число.
# # n=int(input("Enter number of elements on list:"))
# # my_list=[input("Enter element: ") for i in range(n)]
# # print(my_list)
# # print(max(my_list), "is the max element")
# # print(min(my_list), "is the min element")

# # my_list=[input("Enter element: ") for i in range(int(input("Enter number of elements on list:")))]
# # print("{} is the max element, {} is the min element".format(max(my_list),min(my_list)))

# my_list=[input("Enter element: ") for i in range(int(input("Enter number of elements on list:")))]
# max_el=my_list[0]
# min_el=my_list[0]
# for i in range(len(my_list)):
#     if my_list[i]>max_el:
#         max_el=my_list[i]
#     if my_list[i]<min_el:
#         min_el=my_list[i]

# print("{} is the max element, {} is the min element".format(max_el,min_el))
# ################В інтервалі від 1 до 10 визначити числа -парні, які діляться на 2, -непарні, які діляться на 3, -числа, які не діляться на 2 та 3.
# list1=[]
# list2=[]
# list3=[]
# for i in range(10):
#     if i%2 == 0:
#         list1.append(i)
#     if i%2!=0 and i%3==0:
#         list2.append(i)
#     if i%2!=0 and i%3!=0:
#         list3.append(i)

# print("Even numbers: {} \nOdd numbers divisible by 3: {} \nNumbers that are not debisible by 2 and 3: {}".format(list1,list2,list3))
# ################ Факторіал
# number=int(input("Enter number: "))
# fact=1
# if number<0:
#     print("The factorial does not exist")
# elif number==0:
#     print("0!=1")
# else:
#     for i in range(1,number+1):
#         fact*=i
# print(number, "!=", fact)
# ################ Напишіть скрипт, який перевіряє логін, який вводить користувач. 
# start=False
# while not start:
#     log=input("Enter login: ")
#     if log=="First":
#         print("Welcome!")
#         start=True
#     else:
#         print("Error, {} is incorrect login".format(log))
# ################ Написати програму, яка буде зчитувати числа поки не зустріне від’ємне число.
# start=True
# while start:
#     i=int(input("Enter number: "))
#     if i<=0:
#         print("The end")
#         start=False