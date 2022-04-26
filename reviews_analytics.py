data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:  #因為每次都是讀取一行,所以把變數命名為line
		data.append(line)  #把line append進去第一行
		count = count + 1
		if count % 1000 == 0:  # % 求餘數
			print(len(data))  #每讀1000筆印一次

print(len(data))
print(data[0]) #印出list的第一筆
print('---------------------')
print(data[1]) #印出list的第二筆
