import sys

if (len(sys.argv) > 3):
    print("InputError: too many arguments")
if (len(sys.argv) != 3):
    print("Usage: run operations.py")
    print("Example:")
    print("    run operations.py 10 3")
    sys.exit()
if (sys.argv[1].isnumeric() == False or sys.argv[2].isnumeric() == False):
    print("InputError: only numbers")
    print("Usage: run operations.py")
    print("Example:")
    print("    run operations.py 10 3")
    sys.exit()

nbr1 = int(sys.argv[1])
nbr2 = int(sys.argv[2])

print("Sum : " + str(nbr1 + nbr2))
print("Difference : " + str(nbr1 - nbr2))
print("Produit : " + str(nbr1 * nbr2))
if nbr2 != 0:
    print("Quotient : " + str(nbr1 / nbr2))
    print("Reminder : " + str(nbr1 % nbr2))
else:
    print("Quotient: ERROR (div by zero)")
    print("Remainder: ERROR (modulo by zero)")