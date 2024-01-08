count_group=int(input())
all_people=0
musala_count=0
monblan_count=0
kilimanjaro_count=0
k2_count=0
everest_count=0
count_pepole_all =0
for i in range(1,count_group+1):
    group=int(input())
    count_pepole_all+=group
    if group<=5:
        musala_count=musala_count+group
    elif group<=12:
        monblan_count+=group
    elif group<=25:
        kilimanjaro_count+=group
    elif group<=40:
        k2_count+=group
    else:
        everest_count+=group

musala_pr=musala_count/count_pepole_all*100
print(f"{musala_pr:.2f}%")
monblan_pr=monblan_count/count_pepole_all*100
print(f"{monblan_pr:.2f}%")
kilimindjaro_pr=kilimanjaro_count/count_pepole_all*100
print(f"{kilimindjaro_pr:.2f}%")
k2_pr=k2_count/count_pepole_all*100
print(f"{k2_pr:.2f}%")
everest_pr=everest_count/count_pepole_all*100
print(f"{everest_pr:.2f}%")