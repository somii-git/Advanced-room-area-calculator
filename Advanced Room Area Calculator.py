length= float(input("What is the rooms length (in meters)? : "))
width= float(input("What is the rooms width (in meters)? : "))

area= length * width
whole_tiles= area // 1
partial_tile= area % 1

print("---------------------------------")
print(f"You need: {whole_tiles} whole tiles.")
print("The leftover area is:", round(partial_tile, 2), "square meters.")
