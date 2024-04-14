# Using a while loop to control the repetition
counter = 0
while counter < 3:
    print("Outer loop iteration:", counter)
    
    # Using a for loop for iteration within the while loop
    for i in range(2):
        print("    Inner loop iteration:", i)
    
    counter += 1