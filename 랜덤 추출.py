import random
import time
b = "그만"
c = []
while True:
    a = input("입력(그만두려면 '그만' 이라고 입력.):")
    
    if a == b:
        break
    else:
        c.append(a)



print(random.choice(c))

time.sleep(9999)
