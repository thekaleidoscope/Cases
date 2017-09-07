from sys import argv

scr,a,b,c=argv;

d=open(a,"rb")
e=open(b,"a")
f=ord(c)

try:
    byte=d.read(1);
    while byte !="":
        byter=ord(byte)^f
        e.write(chr(byter))
        byte=d.read(1)

finally:
    d.close()

e.close()
