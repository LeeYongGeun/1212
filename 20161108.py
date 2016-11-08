# def max_number(n):  #재기용법은 될 수 있으면 지양하라
#     x= n//10
#     if x>=10:
#         x=max_number(x)
#     return x
# print(max_number(1234))

# def f(d):
#     k=1
#     if d >1:
#         k = d * f(d-1)
#     return k
# print (f(5))

# def f(d):
#     if d==0:
#         return 1
#     k = d*f(d-1)
#     return k
# print(f(5))

# def quicksort(x):
#     if len(x) <= 1:
#         return x
#
#     pivot = [x[0]]  #x[0:1]
#     left = []
#     right = []
#
#     for i in x[1:]:
#         if i < pivot[0]:
#             left.append(i)
#         elif i > pivot[0]:
#             right.append(i)
#         else :
#             pivot.append(i)
#
#     return quicksort(left) + pivot + quicksort(right)
#
# x=[7,9,5,6,3,4,2]
# print(quicksort(x))
