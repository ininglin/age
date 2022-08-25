driving = input('請問你有沒有開過車?')
if driving != '有' and driving != '沒有':
	print('請輸入有或沒有')
	raise SystemExit #直接結束對話

age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗囉')
	else:
		print('不可能吧')
elif driving == '沒有':
	if age >= 18:
		print('可以考駕照囉')
	else:
		print('之後再去考吧~')
