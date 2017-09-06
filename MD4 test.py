import hashlib


def Pass(passw):
    #print hashlib.new('md4',passw)
    print passw,hashlib.new('md4',passw.encode('utf-16le')).hexdigest().upper()

for i in range(0,100):
    Pass('%02d' %i)
