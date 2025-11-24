import sys

def add(a, b):
    return a + b

if __name__ == "__main__":
    if len(sys.argv) == 3:      # If user gives command-line values
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:                       # Default values
        x = 10
        y = 20

    print("sum:", add(x, y))
