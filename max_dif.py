def max_diff(input_list):
	diff_list=[]
	for i in range(1,len(input_list)):
		for j in input_list[:i]:
			if j<input_list[i]:
				diff_list.append(input_list[i]-j) 
	if diff_list==[]:
		return -1
	else:	
		return max(diff_list)

if __name__=="__main__":
	print("please enter your input with delimiter as space")
	user_input=list(map(int,input().split()))
	print("you entered :",user_input)
	md=max_diff(user_input)
	print(md)
