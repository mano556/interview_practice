# a=[
#     [1,2,3],
#     [1,2,3],
#     [4,5,6]
# ]
# b=[
#     [2,3,4],
#     [5,6,7],
#     [5,6,7]
# ]
# add=[
#     [0,0,0],
#     [0,0,0],
#     [0,0,0]
# ]
# for x in range(len(a)):
#     for y in range(len(b)):
#         add[x][y]=a[x][y]*b[x][y]
# for z in add:
#     print(z)

add=[[0 for x in range(3)] for x in range(3)]
print(add)                                                                                                                                                                       