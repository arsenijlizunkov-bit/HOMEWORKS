ip1 = '.'.join([bin(int(i))[2:].zfill(8) for i in '95.24.2.9'.split('.')])
ip2 = '.'.join([bin(int(i))[2:].zfill(8) for i in '95.24.3.10'.split('.')])
print(ip1+'\n'+ip2)
#01011111.00011000.0000001 0.00001001
#01011111.00011000.0000001 1.00001010
# в маске 14 нулей.        ^        ^
#                          a        b
#
k = 0
for a in '01':
    for b in range(256):
        s = '01011111.00011000.0000001' + a + '.' + bin(b)[2:].zfill(8)
        if s.count('0'):
            k+=1
print(k)