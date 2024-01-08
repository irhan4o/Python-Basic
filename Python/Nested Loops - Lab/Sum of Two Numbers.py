start=int(input())
end=int(input())
magic_number=int(input())
conbintion_is_found=False
counter_of_combination=0
for first_number in range(start,end+1):
    
    for secound_number in range(start,end+1):
        counter_of_combination+=1
        if first_number+secound_number==magic_number:
            conbintion_is_found=True
            break
    if first_number+secound_number==magic_number:
            break


if conbintion_is_found:
    print(f"Combination N:{counter_of_combination} ({first_number} + {secound_number} = {magic_number})")
else:
        print(f"{counter_of_combination} combinations - neither equals {magic_number}")