nums = [1, 2, 2, 3, 3, 3]

counts = {}

for n in nums:
    if n in counts:
        counts[n] += 1
    else:
        counts[n] = 1

print(nums)
print(counts)
