#但逻辑上似乎不大对：
#from random import*
#TIMES = 10000
#my_first_choice_n=0	#初始化不改选择的次数
#my_change_choice_n=0	#初始化更改选择的次数
#for i in range(TIMES):
#	car_inDoor=randint(0,2)
#	my_guess=randint(0,2)
#	if car_inDoor==my_guess:
#		my_first_choice_n+=1
#	else:
#		my_change_choice_n+=1
#print("不改选择:{}".format(my_first_choice_n/TIMES))
#print("更改选择:{}".format(my_change_choice_n/TIMES))
#

import random
Y=0
N=0

for i in range(100000):
    car=random.randint(1,3)
    try1=random.randint(1,3)
    
    if car==try1:
        tryN=random.randint(1,3)
        while tryN==try1:
            tryN=random.randint(1,3)
        N=N+1
    else:
        tryN=-1       #int("123".split(str(car),str(try1)))
        Y=Y+1
    print("{}but{}not{}".format(try1,car,tryN))

print("Y={:%},N={:%}".format(Y/100000,N/100000))
