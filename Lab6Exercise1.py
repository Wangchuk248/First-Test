num = int(input("Enter the number for which you want multiplication table: "))
limit = int(input(f"Enter the limit up to which table you want to generate: "))

i = 1
while i <= limit: 
    product = num * i
    print(f"{num} * {i} = {product}")
    i += 1