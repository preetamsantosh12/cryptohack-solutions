from pwnlib.util.fiddling import unhex, xor
data = unhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')
for i in range(0,255):
    if xor(data,i).startswith(b'crypto{'):
        print(xor(data,i))
    