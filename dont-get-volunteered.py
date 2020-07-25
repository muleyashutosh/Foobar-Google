cord = {}
no = 56
y = 0
while True:
    x = 0
    while True:
        cord[no] = (x,y)
        x += 1
        no += 1
        if x == 8:
            break
    y += 1
    no -= 16
    if y == 8:
        break

class Cell:
    def __init__(self,x = 0, y = 0, moves = 0):
        self.x = x
        self.y = y
        self.moves = moves

def isInside(x,y):
    if (x >= 0 and x <= 7) and (y >= 0 and y <= 7):
        return True
    return False


def solution(src,dest):
    sc = cord[src]
    dst = cord[dest]
    #print(sc,dst)
    dx = [2,2,-2,-2,1,1,-1,-1]
    dy = [1,-1,1,-1,2,-2,2,-2]
    
    queue = []
    
    queue.append(Cell(sc[0],sc[1],0))
    #for item in queue:
     #   print(item.x,item.y,item.moves)
        
    visited = [[False for x in range(8)] for y in range(8)]
    
    visited[sc[0]][sc[1]] = True
    # for no in visited:
    #     for no1 in no:
    #         print(no1,end = " ")
    #     print("\n")
        
    while (len(queue) > 0):
        # for item in queue:
        #     print("(",item.x,", ",item.y,")")
        # print('\n')
        t = queue[0]
        queue.pop(0)
        
        if (t.x == dst[0]) and (t.y == dst[1]):
            return t.moves
        
        for i in range(8):
            x = t.x + dx[i]
            y = t.y + dy[i]
            #print(x,y)
            if isInside(x,y) and not visited[x][y]:
                visited[x][y] = True
                queue.append(Cell(x,y, t.moves + 1))
    
print(solution(0,1))