# n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
#
# def flatten(lists):
#     results =[]
#     for numbers in lists:
#         for number in numbers:
#             results.append(number)
#     return results
# print(flatten(n))

# board = [['O' for j in range(5)] for i in range(5)]

board = [['O'] * 5 for i in range(5)]

def b(board_in):
    for row in board_in:
        print(row)

b(board)

