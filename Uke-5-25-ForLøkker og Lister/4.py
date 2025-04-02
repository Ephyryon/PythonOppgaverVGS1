nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
par = "Partall: "
odd = "Oddetall: "
num = 0
for i in nums:
    if nums[num] % 2 == 0:
        par += f"{nums[num]}, "
        num += 1
    else:
        odd += f"{nums[num]}, "
        num += 1
print(par)
print(odd)