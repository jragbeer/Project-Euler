with open('C:/Users/J_ragbeer/PycharmProjects/other/p096_sudoku.txt', 'r') as file:
    # row-wise
    rows = [list(x) for x in file.read().splitlines()[1:10]]
    print(rows)
    # col-wise
    cols=[[x[y] for x in rows] for y in range(9)]
    print(cols)
    # middle of each box
    boxes_middles = [[x,y] for y in [1,4,7] for x in [1,4,7]]
    # each box
    boxes = []
    for u,i in boxes_middles:
        boxes.append([rows[x][y] for y in [u-1,u,u+1] for x in [i-1,i,i+1]])
    print(boxes)
