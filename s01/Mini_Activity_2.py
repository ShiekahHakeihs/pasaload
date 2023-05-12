start = int(input("Give a number: ")) 
end = int(input("Give a second number: "))
sk = int(input("Give a size number: "))
for i in range(start, end + 1, sk):
	print(i, end =' ')
