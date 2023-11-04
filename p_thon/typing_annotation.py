from typing import List,Dict,Set,Optional,Any,Tuple,Sequence,Callable

x:List[int]=[1,2,3]
print(x)

y:Dict[str,str]={"Roll":"23"}
print(y)

z:Set[str]=["Ram","Shyam"]
print(z)

m:Tuple[int]=(10,1,2)
print(m)

#Custom type

Vector=List[float]

def foo(v:Vector)->Vector:
    print(v)

foo([1,2])

#optional type module


def fun(output:bool=False)->None:
    print("Optional function...")

fun(Optional)


def fun2(out:Any):
    pass
fun2("Hii")


def fun3(seq:Sequence[str]):
    pass

fun3(("a","b","c"))
fun3(["a","b"])


#when you want to aceept function as a parameter



# def fun4(func:Callable[[int,int],int]):


xt:List[int | int]=[0 | 2]
print(xt)

