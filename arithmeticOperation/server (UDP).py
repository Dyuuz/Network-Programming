import socket

def mak(num1, num2, num3):
    if num1 > num2:
        larger = num1
    else:
        larger = num2
    if larger > num3:
        largest = larger
    else:
        largest = num3
    return largest

def minNum(num1, num2, num3):
    if num1 < num2:
        smaller = num1
    else:
        smaller = num2
    if smaller < num3:
        smallest = smaller
    else:
        smallest = num3
    return smallest

def divNum(num1, num2, num3):
    if num2 != 0 and num3 != 0:
        div = num1 / num2 / num3
    else:
        div = print("Division by Zero is not allowed")
    return div

def subNum(num1, num2, num3):
    diff = num1 - num2 - num3
    return diff

def avgNum(num1, num2, num3):
    avg = (num1 + num2 + num3) / 3
    return avg

def modulo(num1, num2, num3):
    if num2 != 0 and num3 != 0:
        mod1 = num1 % num2
        mod2 = mod1 % num3
    else:
        mod2 = print("Modulo by Zero is not allowed")
    return mod2

def powNum(num1, num2, num3):
    pow1 = num1 ** num2
    pow2 = pow1 ** num3
    return pow2


def lcm1(a, b):
    x = a
    y = b
    ll = a * b
    while( y != 0):
        z = x % y
        x = y
        y = z
    hcf = x
    print('hcf is ', x)
    lcm = ll / hcf
    print('lcm is ',lcm)
    return lcm


def opera(num1, op1, num2, op2, num3):
    re = ''

    if op1 == '+':
        sum = num1 + num2 + num3
        re = re+' '+str(num1)+' + '+str(num2)+' + '+str(num3)+' is '+str(sum)

    elif op1 == '*':
        sum = num1 * num2 * num3
        re = re+' '+str(num1)+' * '+str(num2)+' * '+str(num3)+' is '+str(sum)

    elif op1 == 'l':
        rr = lcm1(num1, num2)
        ra = lcm1(rr, num3)
        re = re+' lcm  '+str(num1)+' l '+str(num2)+' l '+str(num3)+' is '+str(ra)

    elif op1 == 'm':
        k = mak(num1, num2, num3)
        re = re + 'maximum of ' + str(num1) + ' m ' + str(num2) + ' m ' + str(num3) + ' is ' + str(k)

    elif op1 == 'n':
        min = minNum(num1, num2, num3)
        re = re + 'minimum of ' + str(num1) + ' n ' + str(num2) + ' n ' + str(num3) + ' is ' + str(min)

    elif op1 == 'd':
        div = divNum(num1, num2, num3)
        re = re + 'division of ' + str(num1) + ' d ' + str(num2) + ' d ' + str(num3) + ' is ' + str(div)

    elif op1 == 's':
        diff = subNum(num1, num2, num3)
        re = re + 'subtraction of ' + str(num1) + ' s ' + str(num2) + ' s ' + str(num3) + ' is ' + str(diff)

    elif op1 == 'a':
        avg = avgNum(num1 + num2 + num3)
        re = re + 'average of ' + str(num1) + ' a ' + str(num2) + ' a ' + str(num3) + ' is ' + str(avg)

    elif op1 == 'b':
        mod2 = modulo(num1, num2, num3)
        re = re + 'modulo of ' + str(num1) + ' % ' + str(num2) + ' % ' + str(num3) + ' is ' + str(mod2)

    elif op1 == 'p':
        pow2 = powNum(num1, num2, num3)
        re = re + 'power of ' + str(num1) + ' ^ ' + str(num2) + ' ^ ' + str(num3) + ' is ' + str(pow2)

    return re

ss = socket.socket(family = socket.AF_INET,type = socket.SOCK_DGRAM)
print('start server.... ')
host = '127.0.0.1'
port = 6000
ss.bind((host, port))

con, addr = ss.recvfrom(1024)
print('address client connected %s: '%str(addr))

print('message bf decoding : ', con)
data = con.decode()
print('message after decoding : ',data)

msg = input('message to client---->  ')
msg = str.encode(msg)
ss.sendto(msg, (addr))

con, addr = ss.recvfrom(1024)
print('message bf decoding ', con)

data = con.decode()
print('message after decoding ',data)

data = data.split()
print('message after splitting : ', data)
num1 = int(data[0])
op1 = data[1]
num2 = int(data[2])
op2 = data[3]
num3 = int(data[4])
sum = num1 + num2 + num3
print('addition of number sent by client is ', sum)
res = opera(num1, op1, num2, op2, num3)
msg = str.encode(res)
print('message to client on request ',msg)
ss.sendto(msg, (addr))





