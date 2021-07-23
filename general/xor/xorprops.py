from pwn import *
KEY1 = unhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
COM1 = unhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
COM2 = unhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
COM3 = unhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
FLAG = xor(KEY1, COM2, COM3)
print(FLAG.decode())