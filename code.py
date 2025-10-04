arr = [0,1,2,2,3,0,4,2]
target = 2
j    = 0

for i in range(len(arr)):
    if arr[i] != target:
        arr[j] = arr[i]
        j+=1
    
print(arr[:j])