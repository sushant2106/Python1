def sample_decorator(func):
    def wrapper(*args,**kwargs):
        print("<b>"+func(*args,**kwargs)+"</b>")

    return wrapper


@sample_decorator
def bold_div(html):
    return html


bold_div("<div>Helllo!</div>")


#Higher order Fns

def apply_operation(func,x,y):
    return func(x,y)

def add(x,y):
    return x+y

result1=apply_operation(add,2,3)

print(result1)


def sum(start,end):
    current=start
    while current<end:
        yield current
        current+=2


x=sum(1,10)

for i in x:
    print(i)
