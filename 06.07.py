# ################ Написати скрипт, який з двох введених чисел визначить, яке з них більше, а яке менше.
# num1=int(input("Enter number 1:"))
# num2=int(input("Enter number 2:"))
# if num1 > num2:
#     print("%d > %d" % (num1, num2))
# else:
#     print("{} > {}".format(num2, num1))
# ################ Написати скрипт, який перевірить чи введене число парне чи непарне і вивести відповідне повідомлення.
# number=int(input("Enter number: "))
# if number%2==0:
#     print(number, "is even")
# else:
#     print(number, "is odd")
# ################ Написати скрипт, який обчислить факторіал введеного числа.
# number=int(input("Enter number: "))
# fact=1
# for i in range(1,number+1):
#     fact*=i
# print("Factorial: ", fact)
# ################ Роздрукувати всі парні числа менші 100 (написати два варіанти коду: один використовуючи цикл while, а інший з використанням циклу for).
# # i=0
# # while i<100:
# #     print(i)
# #     i+=2

# print(list(range(0,100,2)))
# ################ Роздрукувати всі непарні числа менші 100. (написати два варіанти коду: один використовуючи оператор continue, а інший без цього оператора).
# # for i in range(1,100,2):
# #     print(i)

# i=0
# while i<100:
#     i+=1
#     if i%2==0:
#         continue
#     else:
#         print(i)
# ################ Перевірити чи список містить непарні числа.
# list=[2,3,4,6,8]
# for i in list:
#     if not i%2 == 0:
#         print(i, "is the odd number")
#         break
# print("The end")
