canyon_length = int(input())
height_rocks = []
for i in range(canyon_length):
    height_rocks.append(int(input()))

def calculate_trapped_water(heights):
    if len(heights) <= 2: #no water can be trapped if only 2 rocks
        return 0
    
    left = 0
    right = len(heights) - 1
    left_max = 0 #left max and right max track the highest rocks seen so far
    right_max = 0
    water_trapped = 0
    
    while left < right: #we're gonna use 2 pointers to track the heights
        if heights[left] < heights[right]: 
            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                # if the current height is < max height on the left, we know we can trap 
                # (leftmax - current height) amounts of water
                water_trapped += left_max - heights[left]
            left += 1
        else:
            if heights[right] >= right_max:
                right_max = heights[right]
                # if the current height is > max height on the right, we know we cna trap
                # (rightmax - current height) amounts of water
            else:
                water_trapped += right_max - heights[right]
            right -= 1
    
    return water_trapped

result = calculate_trapped_water(height_rocks)
print(result)
