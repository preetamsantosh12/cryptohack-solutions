from binascii import unhexlify

hexlist = '7c:3b:1d:53:4f:29:9b:43:c1:26:08:76:30:3c:0a:95:be:17:bf:91:a5:df:2f:1c:ac:da:7c:75:a0:23:6e:4f:81:e1:21:0d:27:c0:12:6f:b3:4d:80:f2:7a:41:a4:d7:e4:8c:a7:c5:b0:e7:88:78:b1:9f:d0:d6:c0:bf:68:30:fb:8a:44:01:b1:6d:93:8a:d5:4c:4d:0b:35:68:62:05:6c:b0:55:4e:b2:ab:83:90:ad:18:25:b3:1d:af:bf:2f:c0:5d:19:4f:38:c2:f2:24:20:d3:21:0a:da:02:30:24:26:40:ca:e0:05:eb:85:cb:c8:dc:ca:18:25:ea:74:96:d9:b1:70:c5:cb:fe:35:4f:e1:9a:63:10:2b:82:f3:8d:5d:7c:25:17:35:20:8b:83:a5:42:40:92:7f:89:98:48:c1:6a:5f:e7:0c:e9:50:da:ff:7b:f9:f4:b7:1b:59:81:01:a5:20:48:cd:30:c1:6c:b9:94:33:0b:10:59:2d:2c:95:d4:d0:e5:79:f5:28:7f:f7:4a:88:26:8d:03:89:69:8c:8f:7b:9a:e8:13:f3:92:46:89:3d:02:66:1c:f0:8d:9c:bc:ec:9f:72:2c:f7:6d:0e:96:f1:e1:77:37:e2:9e:ce:86:76:76:7c:b6:e1:df:0d:bd:2d:73:1e:d8:48:b1'

def convert(n: str) -> int:
    hex = n.replace(":", '').replace(' ', '')
    return int(hex, 16)
    
final  = convert(hexlist)
print(final)