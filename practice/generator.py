# def my_generator():
#     for i in range(5):
#         yield i
#
# gen = (my_generator())
# print(next(gen))
# print(next(gen))



# fibonacci series using generator


# def fibonacci():
#     a,b = 0,1
#     while True:
#         yield a
#         a,b=b,a+b


# f1=fibonacci()
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))



def coundown_generator(start):
    while start > 0:
        yield start
        start -= 1
        
#using generator
countdown = coundown_generator(5)
for number in countdown:
    print(number)




