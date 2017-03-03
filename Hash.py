import sys
import hashlib
import ssdeep

def Hash_mix(temp):
    d = {}
    m = hashlib.md5()
    d['md5'] = m.hexdigest()
    m.update(temp)
    m = hashlib.sha1()
    d['sha1'] = m.hexdigest()
    m = hashlib.sha256()
    d['sha256'] = m.hexdigest()
    d['ssdeep'] = ssdeep.hash(temp)
    return d
    
def main():
    d = {}
    f = open('test2.py', 'r')
    temp = f.read()
    d = Hash_mix(temp)
    print d
if __name__ == '__main__':
    main()
