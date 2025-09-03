"""Module for pattern programs"""
#
# # Right-angled triangle
# # *
# # **
# # ***
# # ****
# # *****
# n = 5
# for i in range(1, n + 1):
#     print("*" * i)
#
# # Left-angled triangle
# #     *
# #    **
# #   ***
# #  ****
# # *****
# n = 5
# for i in range(1, n+1):
#     print(" " * (n-i) + "*" * i)
#
# # Pyramid
# #     *
# #    ***
# #   *****
# #  *******
# # *********
# n = 5
# for i in range(1, n +1):
#     print(" " * (n - i) + "*" * (2*i-1))
#
#
# # Inverted Pyramid
# # *********
# #  *******
# #   *****
# #    ***
# #     *
# n = 5
# for i in range(n, 0, -1):
#     print(" " * (n-i) + "*" * (2*i-1))
#
#
# # Number triangle
# # 1
# # 1 2
# # 1 2 3
# # 1 2 3 4
# # 1 2 3 4 5
#
# n = 5
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end= " ")
#     print()
#
# # Inverted Left Angle Triangle
# # *****
# #  ****
# #   ***
# #    **
# #     *
# # n = 5
# for i in range(n):
#     print(" " * i + " *" * (n -i))
#
# # Inverted Right Angle Triangle
# # * * * * *
# # * * * *
# # * * *
# # * *
# # *
#
# for i in range(n, 0, -1):
#     print("* " * i)
#
# #
# # 1 2 3 4 5
# # 1 2 3 4
# # 1 2 3
# # 1 2
# # 1
# for i in range(n, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
#
# # Floyd’s Triangle
# # 1
# # 2 3
# # 4 5 6
# # 7 8 9 10
# # 11 12 13 14 15
#
# n = 5
# count = 1
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(count, end= " ")
#         count += 1
#     print()

# Pascal’s Triangle (using binomial coefficients)
#       1
#     1   1
#   1   2   1
# 1   3   3   1
n = 4
# for i in range(n):
#     # Print space for alignment
#     print(" " * (n-i), end="")
#     # First number
#     num = 1
#     for j in range(i + 1):
#         print(num, end=" ")
#         num = num * (i -j) // (j + 1)
#     print()
#
# # Diamond shape
# n = 5
# for i in range(n):
#     print(" " * (n- i) + "* " * i)
# for j in range(n, 0, -1):
#     print(" " * (n- j) + "* " * j)
#
# # Butterfly Pattern
# n = 5
# for i in range(1, n + 1):
#     print("*" * i + " " * (2 *(n-i)) + "*" * i)
# for j in range(n, 0, -1):
#     print("*" * j + " " * (2 *(n-j)) + "*" * j)

# Hollow Square
# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# X Pattern
n = 5
for i in range(n):
    for j in range(n):
        if i == j or i + j == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

