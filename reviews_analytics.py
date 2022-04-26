data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:  # 因為每次都是讀取一行,所以把變數命名為line
		data.append(line)  # 把line append進去data的清單
		count = count + 1
		if count % 1000 == 0:  # % 求餘數
			print(len(data))  # 每讀1000筆印一次

print('檔案讀取完了，總共有', len(data),'筆資料')

# 要怎麼算這100萬筆資料的平均長度
sum_len = 0
for d in data:  # data這個清單裡面的每一筆一筆資料都叫出來，每一筆就是一個d
	# print(len(d))
	# len(d)
	sum_len = sum_len + len(d)
	# print(sum_len)
print('平均是',sum_len/len(data))

# 當一筆資料的長度小於100，就把那筆資料裝進new的清單
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new),'筆留言長度小於100')
print(new[0])
print(new[1])

# 從每一筆資料裡面篩選出有good的資料
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print(good[0])

# *****list comprehension清單快寫法*****
good = [d for d in data if 'good' in d]

bad = ['bad' in d for d in data] 
# 'bad' in d是一個True or False的運算，所以bad清單裡面不是裝True就是False
# bad = []
# for d in data:
# 	bad.append('bad' in d)




