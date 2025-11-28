n, k, m = map(int, input().split())
if n == k or n < k:
    time = 2 * m
elif n % k == 0:
    group_of_child = n // k
    time_of_1_group = m * 2
    time = time_of_1_group * group_of_child
else:
    group_of_child = n // k + 1
    time_of_1_group = m * 2
    time = time_of_1_group * group_of_child

print(time)