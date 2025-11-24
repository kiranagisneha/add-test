import sys

def add(a, b):
    return a + b

if name == "main":
    if len(sys.argv) == 3:  
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:  
        x = 10
        y = 20

    print("sum", add(x, y))
