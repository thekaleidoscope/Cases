from sys import argv

sc,offset=argv

offset=int(offset)
print "Go ahead with a Text"
c=raw_input().replace(" ","")

final=""
for ch in c:
    t=chr((ord(ch)-ord('a')+offset)%26+ord('a'))
    final+=t

print final

print "ReTest Code to Decipher"

print "Any Key to cont or Clt-c to Exit"
raw_input()
while(True):
    print "Enter Key:"
    k=int(raw_input('>'))
    plain=""
    for che in final:
         te=chr((ord(che)-ord('a')-k)%26 + ord('a'))
         plain+=te
    print plain

    print "Is The Message Correct Or Retry ?(Clt-c TO END, any key to Retry)"

    raw_input()
