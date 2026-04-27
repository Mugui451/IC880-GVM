n = 3
v = {}
#tamanho do bloco = 2^(v-i)
for i in range(1,n+1):
    for j in range(1,2**(n-1)+1):
        v[(i,j)] = 1 - ((round(j / (2**(n-i)))) % 2)

print(v)