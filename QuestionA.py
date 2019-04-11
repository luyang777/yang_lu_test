def order(x):
    #this function is to check if the pair is in order
    #for example x(5,3) will be changed to x(3,5)
    if x[0] > x[1]:
        return (x[1], x[0])
    return x

def isOverlap(line1,line2):
    #this function is to check if two lines overlap
    line1, line2 = order(line1),order(line2)
    if line2[1]< line1[0] or line2[0]>line1[1]:
        return False
    else:
        return True
    return False

if __name__=="__main__":
    #test case
    #if they overlap, it returns true otherwise false
    print(isOverlap([4,3],[-7,6]))
    print(isOverlap([-1,-2],[-4,-7]))
    print(isOverlap([5,8],[1,3]))
    print(isOverlap([2,6],[4,8]))
