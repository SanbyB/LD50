

def find(list, x, y, xMin, yMin, xRange, yRange):
    '''
    list of objects to search through
    x, y coord to search for
    range in which a subset of the list of objects will be returned
    '''
    index = iterate(list, x, xMin, 0, int(len(list)/2))
    subList = []
    i = 0
    while x - xRange < list[index+i].pos[0] < x + xRange:
        i -= 1
    j = 1
    while x - xRange < list[index+i+j].pos[0] < x + xRange:
        subList.append(list[index+i+j])
        j += 1
    
    finList = []
    for k in subList:
        if y - yRange < k.pos[1] < y + yRange:
            finList.append(k)

    return finList



def iterate(list, val, range, xy, index):
    if val - range < list[index].pos[xy] < val + range:
        return index
    elif val - range > list[index].pos[xy]:
        return iterate(list, val, range, xy, index + int(index/2))
    elif val + range < list[index].pos[xy]:
        return iterate(list, val, range, xy, int(index/2))


if __name__ == "__main__":
    from Entities.tree import Tree
    import numpy as np
    trees = []
    for i in range(-4, 5):
        for j in range(-4, 5):
            trees.append(Tree(i*500 + np.random.randint(-80, 80), j*400 + np.random.randint(-80, 80)))
    
    for tree in trees:
        print(tree.pos)

    it = iterate(trees, -1500, 500, 0, int(len(trees)/2))

    print(it)

    print(trees[it].pos)

    print("#############################")

    fnd = find(trees, -1500, 300, 100, 100, 500, 400)

    for tree in fnd:
        print(tree.pos)