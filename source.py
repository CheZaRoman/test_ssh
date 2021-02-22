# a = [1,2,3,4,5,6,7,8,9]
#
# for item in a:
#     print(item)
#
# range(10) # 0 - 9
#
# for i in range(10+1):
#     print(i)
#
# range(1,10)
#
# for i in range(1,10,2):
#     print(i)
#
# range(1,10,2)

# import random
# for i in range(11):
#     print(random.randint(1,25))
#
# a = 0
# while True:
#     a += 1
#     print(a)


number = int(input())
result = 1
# for i in range(1, number+1):
#     result *= i
#
# print(result)

# while number > 0:
#     result *= number
#     number -= 1
# print(result)


for i in range(100):
    if i == 56:
        break
    print(i)
