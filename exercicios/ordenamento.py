vetA = list([3,5,6,8,0,3])
for i in range (len(vetA)-1):
    print(f'i = {i}')
    for j in range (len(vetA)-1-i):
        print(f'j = {j}')
        if vetA[j] > vetA[j+1]:
            vetA[j], vetA[j+1] = vetA[j+1], vetA[j]
print(vetA)