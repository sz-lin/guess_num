#產生一個隨機整數1~100(不要印出來)
#讓使用者重複輸入數字去猜
#猜對 印出 "終於答對了"
#猜錯的話 要印出 比答案大或小
#-------本章節----指令教學-------------
#import random  #(先載入 random 模組)
#random.randint(1,100) #(使用函式-產生隨機整數)
#-----------------------------------

import random
ace = random.randint(1,100)
count = 0

while True:
	count += 1 #count = count+1 快寫法
	guess_num = input('請猜猜數字')
	guess_num =int(guess_num)
	if ace == guess_num :
		print('恭喜你猜中了')
		break # 逃出迴圈
	elif guess_num < ace: #(另外如果)
		print('比答案小')
	elif guess_num > ace :
		print('比答案大')
print('這是你猜的第',count,'次')


