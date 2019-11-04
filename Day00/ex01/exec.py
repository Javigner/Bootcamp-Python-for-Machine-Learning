import sys

x = 2
string = sys.argv[1][::-1]
while(x < len(sys.argv)):
    string = string + " " + sys.argv[x][::-1]
    x = x + 1
print(string)