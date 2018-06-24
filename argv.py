import sys

print(sys.argv)
if len(sys.argv) != 2:
    print("missing command-line argument")
    exit(1)

s-=sys.argv[1]
print("hello, {}".format(s) )
exit(0)
