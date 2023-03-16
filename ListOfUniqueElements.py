o_list = [1, 1, 2, 3, 3, 4, 4, 5, 6, 5, 6]
n_list = []

for i in o_list:
    if i not in n_list:
        n_list.append(i)

print(n_list)
