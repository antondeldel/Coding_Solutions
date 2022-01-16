
class Point:
    def __init__(self,id,value,sum,before,after):
         self.id = id
         self.value = value
         self.sum = sum
         self.before = before
         self.after = after


test = [3,-1,1,2]


def brute_force(l):
    l = [ x * (1 if i % 2 == 0 else -1) for i,x in enumerate(l)]
    res = l[0] # initially put to 0, but cannot prove the answer would always be positive
    z = len(l)
    for i in range(z):
        s = 0 
        factor = 1 if i % 2 == 0 else -1
        for ii in range (i, z):
            s +=l[ii]
            if s * factor > res:
                res = s * factor
    return res


print (brute_force(test))
print (brute_force([2,2,2,2,2]))
print (brute_force([1]))

def intelligent (l):
    l = [ x * (1 if i % 2 == 0 else -1) for i,x in enumerate(l)]
    z = len(l)
    vals = z * [0]
    vals [0] = l[0]
    for i in range (1,z):
        vals[i] = vals[i-1] + l[i]
    indexes = sorted(range(z), key=vals.__getitem__,reverse=True)
    largest = None
    smallest = None
    points = []
    for i in range(z):
        p = Point(i,l[i],vals[i],indexes[i] - 1,indexes[i]+1)
        points.append(p)
        if indexes[i] == 0:
            largest = i
        if indexes[i] == z - 1:
            smallest = i
    res = points[largest].sum
    # print(vals)
    # print(largest, smallest)
    amendment = 0
    for i in range(z-1): # no need to remove last one, as subarray canot be empty
        p = points[i]
        amendment += p.value
        if p.before !=-1:
            q = points[p.before]
            q.after = p.after
        else:
            largest = p.after
        if p.after != z:
            q = points[p.after]
            q.before = p.before
        else:
            smallest = p.before
        
        # Seeing if we need to update global total
        if i %2 == 0:
            #take the largest
            q = points[largest]
            if q.sum - amendment > res:
                res = q.sum - amendment
        else:
            #take the smallest, flip sign
            q = points[smallest]
            if (q.sum - amendment) * (-1) > res:
                res = (q.sum - amendment) * (-1)
        
    # Loop will remove 1 item from the chain, then check what
    # the residual will be, and flip larget, smallest
    return res

print(intelligent(test))

print (intelligent([2,2,2,2,2]))
print (intelligent([1]))