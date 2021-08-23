# a^2 = x mod p
p = 29
ints = [14, 6, 11]

##Looping through 1 to p-1 , and checkin for the qudratic residue
flag = [a for a in range(p) if pow(a, 2, p) in ints]
print(min(flag))
