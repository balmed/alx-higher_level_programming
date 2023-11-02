#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    cpt = len(sys.argv) - 1
    if cpt == 0:
        print("0 argumants.")
    elif cpt == 1:
        print("1 argumants:")
    else:
        print("{} argumants:".format(cpt))
        for i in  range(cpt):
            print("{}:{}".format(i + 1, sys.argv[i + 1]))
