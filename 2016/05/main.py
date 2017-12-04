import hashlib

# doorId = 'abc' -> gives '18f47a30'
doorId = 'ojvtpuvg'
password = []
# for idx in range(8):
i = 0
# while len(password) < 8:
#     m = hashlib.md5()
#     m.update(doorId+str(i))
#     m.hexdigest()
#     result = m.hexdigest()
#     if result[:5] == '00000':
#         password.append(result[5])
#         print(password)
#     i += 1

print(''.join(password)) # gives 4543c154

# part 2

password = [' ']*8
# for idx in range(8):
i = 0
while ' ' in password:
    m = hashlib.md5()
    m.update(doorId+str(i))
    m.hexdigest()
    result = m.hexdigest()
    if result[:5] == '00000' and result[5] in '01234567' and password[int(result[5])] == ' ':
        password[int(result[5])] = result[6]
        print("[{}]".format(password))
    i += 1

print(''.join(password)) # gives 4543c154