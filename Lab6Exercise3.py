for i in range(1, 10):
    if i == 7: 
        print(f"Reached {i}, breaking outer loop")
        break
    if i == 3:
        print(f"Skippping {i} in inner loop")
        continue
    for j in range(1, 4): 
        if j == 3:
            continue
    print(i)