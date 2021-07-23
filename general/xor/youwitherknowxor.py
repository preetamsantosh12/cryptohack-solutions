from pwnlib.util.fiddling import unhex, xor

data = unhex(
    '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')


def function(data, hint):
    output = b''
    for c1, c2 in zip(data, hint):
        output += xor(c1, c2)
    return(output.decode('utf-8'))


# based on the hint, trying to find part of the secret key
key = function(data[:7], "crypto{".encode())
print("{}".format(key))
# output now is myXORke
# assuming its myXORkey
key = (key + "y").encode()
# filling up the remaining length  of key
key += (key) * (int)((len(data) - len(key))/len(key))
key += (key)[:((len(data)-len(key)) % len(key))]

print("{}".format(key.decode()))

# final solution
final = function(data, key)
print("{}".format(final))