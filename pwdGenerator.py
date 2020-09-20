import random
s="qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()?"
passlen=8
p="".join(random.sample(s,passlen))
print(p)    