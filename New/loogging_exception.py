import logging

logging.basicConfig(filename='log2.txt',level=logging.INFO)

logging.info("Anew request came")

try:
    x=int(input("Enter the first no:"))
    y=int(input("Enter second number:"))
    print(x/y)

except ZeroDivisionError as msg:
    print("can't divide with zero")
    logging.exception(msg)

except ValueError as msg:
    print("Enter only int values")
    logging.exception(msg)

logging.info("Request process is complted ")

# ...
# print('Hello')
# ...

# print('Hi')
# ...

