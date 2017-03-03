from Hash import Hash_mix

def main():
    d = {}
    f = open('test2.py', 'r')
    temp = f.read()
    d = Hash_mix(temp)
    print d
if __name__ == '__main__':
    main()
