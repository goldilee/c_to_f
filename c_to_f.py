name = input('請輸入名字: ')
if name == '':
	print ('您沒有輸入')
	name = input('請輸入名字: ')
	if name == '':
		print ('您又沒有輸入，幹')
	else:
		print ('Hi', name)	
else:
	print ('Hi', name)

age = input('請輸入年齡:')	
age = int(age)
if age >= 20:
	print('可以投票')
else:
	print('不能投票')	

temp_c = input ('請輸入攝氏溫度: ')
temp_c = float (temp_c)
temp_f = temp_c * 9 / 5 + 32
print('華氏溫度為: ', temp_f)