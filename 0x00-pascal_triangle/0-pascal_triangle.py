#!/usr/bin/python3
'''Module to return pascal triangle'''


def pascal_triangle(n):
    '''
    Pascal's triangle
    Args:
      n (int): The number of rows of the triangle
    Returns:
      List of lists of integers representing the Pascal’s triangle
    '''
    lists = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            lists[i][j] = lists[i - 1][j - 1] + lists[i - 1][j]
    return lists
