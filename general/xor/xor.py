final = ''
for x in 'label':
    final += (str)(chr((ord(x) ^ 13)))

print("crypto{"+final+'}')
