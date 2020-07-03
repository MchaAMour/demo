import sys

def default():
    print("M7ma meshaa")
def dog():
    print("Grrrrrrr")

def main():
    if sys.argv[1] == 'dog':
        dog()
        else:
            default()

if  __name__ == '__main__':
    main()