listA = ['a','e','i','o','u']

iter_list=iter(listA)

# try:
#     print(next(iter_list))

#     print(next(iter_list))

# except:
#     pass


# class Custom:
#     def __init__(self,start,end):
#         self.start=start
#         self.end=end

#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.start<self.end:
#             result=self.start
#             self.start+=2
#             return result
#         else:
#             raise StopIteration
        
# iterator = Custom(1, 10)
# for num in iterator:
#     print(num)

# def custom_iterator(start,end):
#     current=start
#     while current<end:
#         yield current
#         current+=2

# it=custom_iterator(1,10)

# for x in it:
#     print(x)
