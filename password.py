# 密碼重試程式
# 1. 密碼為:'a123456'
# 2. 讓使用者最多輸入3次密碼
# 3. 不對的話就印出'密碼錯誤! 還有__次機會'
# 對的話就印出'登入成功'

password = 'a123456'
x = 3
while x > 0:
	pwd = input('請輸入密碼: ')
	if pwd == password:
	    print('登入成功!')
	    break
	else:
	    print('密碼錯誤! 還有', x-1, '次機會')
	x = x-1

