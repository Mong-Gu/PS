lst = []
for i in range(5):
    lst.append(int(input()))
print(min(lst[:3]) + min(lst[3:]) - 50)