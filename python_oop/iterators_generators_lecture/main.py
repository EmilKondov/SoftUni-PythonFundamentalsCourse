# my_list = [4, 7, 0, 3]
# # get an iterator using iter()
# my_iter = iter(my_list)
# print(next(my_iter)) # 4
# print(next(my_iter)) # 7
# print(my_iter.__next__()) # 0
# print(my_iter.__next__()) # 3
# try:
#     next(my_iter)
# except StopIteration:
#     print("No more items")
#
# iterable = input()
# iter_obj = iter(iterable)
# while True:
#     try:
#         element = next(iter_obj) # get the next item
#         print(element)
# # do something with element
#     except StopIteration:
# # if StopIteration is raised, break from loop
#         break
#


for i in range(10):
    print(i)

