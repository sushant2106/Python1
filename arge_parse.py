import argparse

#We can add it in this way also and learn more varietys

def add(num1,num2):
    return num1+num2

# def add(args):
#     print(args.x+args.y)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description="This is Simple Argparse")
    parser.add_argument('-x','--num1',required='True',type=int,help="Only int val")
    parser.add_argument('-y','--num2',required='True',type=int,help="Only int value 2")
    group=parser.add_mutually_exclusive_group()
    group.add_argument('-q','--quite',action='store_true',help='print quite')
    group.add_argument('-v','--verbose',action='store_true',help='print verbose')
    args=parser.parse_args()
    sum=add(args.num1,args.num2)

    if args.quite:
        print(sum)
    elif args.verbose:
        print("Sum of two number num1 %s & num2 %s is="%(args.num1,args.num2,sum))
    else:
        print("Sum of Number=%s" % (sum))
    #add(args) 


