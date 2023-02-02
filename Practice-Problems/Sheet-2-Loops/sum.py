"""Write a program to compute the following sum:
1 + (1+2) +  (1+2+3) + (1+2+3+4) + .....  .....   ....  up to 10 terms."""




n=10
add=0
for i in range(1,11):
    for j in range(1,i+1):
        add+=j
        # print(f"i = {i} j = {j}")
print(add)