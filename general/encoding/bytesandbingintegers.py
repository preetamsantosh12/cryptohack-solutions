import Crypto.Util.number

val = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

valBytes = Crypto.Util.number.long_to_bytes(val)
print(valBytes.decode())