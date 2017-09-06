import hashlib

def Match(passw):
    hasher=hashlib.new('md4',passw.encode('utf-16le')).hexdigest().upper()
    return hasher


hashe=raw_input(">")
for i in range(0,100):
        if(Match(str(i).zfill(2))==hashe):
            print "Pass:",i
