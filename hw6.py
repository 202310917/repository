def display_multiplication_table(n) :
    for i in range(1,10) :
        print(f'{n} x {i} = {n * i:2d}    {n+1} x {i} = {(n+1) * i:2d}    {n+2} x {i} = {(n+2) * i:2d}    {n+3} x {i} = {(n+3) * i:2d}')
display_multiplication_table(2)
print('')
display_multiplication_table(6)