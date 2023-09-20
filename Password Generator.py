import secrets
import string
l= string.ascii_letters
d=string.punctuation
s=string.digits
p=l+d+s
num=int(input("eenter the length of password:"))
passw=' '
for i in range(num):
    passw+=' '.join(secrets.choice(p))
print(passw)
