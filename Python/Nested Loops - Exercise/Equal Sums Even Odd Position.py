start_num=int(input())
end_num=int(input())

for i in range(start_num,end_num+1):
    current_num_str=str(i)
    even_sum=0
    odd_sum=0
    for symbol in range(0,len(current_num_str)):
        digit=int(current_num_str[symbol])
        if symbol%2==0:
            even_sum+=digit
        else:
            odd_sum+=digit
    if even_sum==odd_sum:
        print(current_num_str,end=" ")



