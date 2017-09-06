import hashlib

def Match(passw):
    return hashlib.new('md4',passw.encode('utf-16le')).hexdigest().upper()

hasher=raw_input('>')
for i in range(0,100):
    if(Match('CCSF-Ming-'+(str(i).zfill(2)))==hasher):
        print "Pass:",i
