import hashlib


def Make(passw):
    print hashlib.new('md5',passw.encode('utf-16le')).hexdigest()

Make(raw_input('>'))
