
def fetch_lines(filename):
    with open(filename,'r') as file:
        lines=[]
        for line in file:
            #lines.append(line)
            yield line
        #return lines


zen=fetch_lines('book.txt')
print(next(zen))