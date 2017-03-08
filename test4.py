from Hash import Hash_mix

def main():
    d = {}
    f = open('test2.py', 'r')
    temp = f.read()
    d = Hash_mix(temp)
    print d
    temp = '123.451.411.456 +dfvzxcbvxzcv36f.dfa'
    temp2 = '1.2.3.4'
if __name__ == '__main__':
    main()
