import sys

def cat():
    print("Meow!")

def default():
    print("M7ma meshaa")

def dog():
    print("Grrrrrrr")

def main():
    if sys.argv[1] == 'dog':
        dog()
    elif sys.argv[1] == 'cat':
        cat()
    else:
        default()
    print("play ground")

if  __name__ == '__main__':
    main()