from sys import argv

scr,a,b,c=argv

fil=open(a,"rb")
fil2=open(b,"a")
k=ord(c)

print fil.read()
fil.seek(0)
fil.tell(0)

try:
    bit=fil.read(1)
    while bit!="":
        bitr=ord(bit)^k
        k=bitr
        bit=fil.read(1)
        fil2.write(chr(bitr))

finally:
    print fil2.read()
    fil.close()

fil2.close()
