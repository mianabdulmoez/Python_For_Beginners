# More about slicing

# Right to left  -------> Positive go minimum
# Left to Right  <--------- Positive go maximum

# # Positive Slicing 
x = "ABDUL MOEEZ"
print(x[0:5])   # it exclude 5 which was space
print(x[0:10])  # it exclude 10 which was Z
print(x[0:11])  # we use 11 mean it exclude and include 10 
print(x[0:20])  # so on
print(x[6:11])
print(x[:])     # To print all string character
print(x[0:]) # To print all string character
print(x[:11])
print(x[4:0])   # It is empty because big value come on right and small on left

# Negative Slicing
print(x[-11:])      # It print all characters
print(x[-15:])      # It print all characters    
print(x[-1:-6])     # It is empty because big come on right side
print(x[-11:-1])    # It exclude last one
print(x[-5:-1])     # -1 is excluded
print(x[-11:-6])    # -6 was space

y = "I Love my country"
print(len(y))

# Positive slicing
print(y[:])
print(y[0:])
print(y[:17])
print(y[0:17])
print(y[0:9])
print(y[10:17])
print(y[0:1])
print(y[2:6])
print(y[7:9])
print(y[10:17])

# Negative slicing
print(y[:])
print(y[0:])
print(y[-17:])
print(y[0:-1])
print(y[-17:-8])
print(y[-7:-1])
print(y[-17:-16])
print(y[-15:-11])
print(y[-10:-8])
print(y[-7:-1])
print(y[-7:0])# It show empty

# Negative and Positive slicing
print(y[-17:1])
print(y[-1:1])# Wrong way and voilation of rule
print(y[-15:6])
print(y[-10:9])
print(y[-7:17])
print(y[-7:16])
print(y[-15:17])
