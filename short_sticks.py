def short_sticks(first_array,second_array):
	output_array=[]
	for i in second_array:
		count=0
		for j in first_array:
			if j<i:
				count+=1
		output_array.append([i,count])

	return output_array

if __name__=="__main__":
	print("enter your first array")
	first_array=list(map(int,input().split()))
	print("enter your second array")
	second_array=list(map(int,input().split()))
	print("first array:",first_array)
	print("second array:",second_array)
	md=short_sticks(first_array,second_array)
	print(md)
