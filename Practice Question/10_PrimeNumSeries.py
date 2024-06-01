# Print the Sequence of the prime numbers

start = int(input("Start the series form "))
end = int(input("Ent the series at "))

print(f"All Prime numbers between {start} and {end} : ", end=" ")
for i in range(start, end+1):
    count=0
    for j in range(2, i):
        if i%j==0:
            count = count + 1
    
    if count==0:
        print(i, end=" ")