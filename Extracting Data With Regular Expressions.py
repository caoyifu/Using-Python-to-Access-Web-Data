import re

fname = "regex_sum_2312772.txt"
fh = open(fname)
numbers = list()

for line in fh:
    line = line.strip()
    nums = re.findall('[0-9]+', line)
    numbers.extend(nums)

numbers = [int(num) for num in numbers]
print(sum(numbers))