data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:  #因為每次都是讀取一行,所以把變數命名為line
		data.append(line)  #把line append進去第一行
		count = count + 1
		if count % 1000 == 0:  # % 求餘數
			print(len(data))  #每讀1000筆印一次

print('檔案讀取完了，總共有', len(data),'筆資料')

#要怎麼算這100萬筆資料的平均長度

sum_len = 0
for d in data:  #每一筆資料叫d
	#print(len(d))
	#len(d)
	sum_len = sum_len + len(d)
	#print(sum_len)
print('平均是',sum_len/len(data))
