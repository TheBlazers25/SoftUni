# number_of_intersections = int(input())
#
# first_set = set()
# second_set = set()
#
# for i in range(number_of_intersections):
#     first_range, second_range = input().split('-')
#     first_start, first_end = first_range.split(',')
#     second_start, second_end = second_range.split(',')
#
#     first_start, first_end, second_start, second_end = int(first_start), int(first_end), int(second_start), int(second_end)
#
#     for f in range(first_start[0], first_end[1]):
#         first_set.add(i)
#
# print(first_set)