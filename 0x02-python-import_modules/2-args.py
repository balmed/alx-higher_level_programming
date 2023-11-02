#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    cpt = len(sys.argv)
    if cpt == 1:
        print("{} arguments.".format(cpt - 1))
    elif cpt == 2:
        print("{} argument:".format(cpt - 1))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(cpt - 1))
        for i in range(1, cpt):
            print("{}: {}".format(i, sys.argv[i]))
