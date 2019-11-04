import sys 

if sys.argv[1].isnumeric() == False or len(sys.argv) != 2:
    print("ERROR")
else:
    if (int(sys.argv[1]) % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")
    