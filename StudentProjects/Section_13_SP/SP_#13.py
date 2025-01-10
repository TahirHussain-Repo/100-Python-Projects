nums = input("Enter a series of numbers separated by spaces for analysis: \n")

nums = [int(num) for num in nums.split()]
print("The numbers are: ", nums)

number_frequency = {}

for num in nums:
    if num not in number_frequency:
        number_frequency[num] = 1
    else:
        number_frequency[num] += 1

total_nums = len(nums)
nums_sum = sum(nums)
range_nums = max(nums) - min(nums)
most_frequent_number = max(number_frequency, key=number_frequency.get)
average_nums = round(nums_sum / total_nums,2)


print("Number Analysis Results:")
print("-" * 20)
print(f"Total Numbers: {total_nums}")
print(f"Sum of Numbers: {nums_sum}")
print(f"Range of Numbers: {range_nums}")
print(f"Most Frequent Number: {most_frequent_number} (appears {number_frequency[most_frequent_number]} times)")
print(f"Average Number: {average_nums}")