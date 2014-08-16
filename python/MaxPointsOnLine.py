# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

'''
WA Reason: 
1. Didn't consider the situation about when the list is empty or only has one point. 
2. Didn't consider to use Fractional expression to avoid the precision problem
3. Have some difficulty in writing a succinct gcd
'''
class Solution:
    def gcd(self, a, b):
        return (a if b == 0 else self.gcd(b, a%b))

    # @param pt1 & pt2, two points
    # @return an tuple(a1,a2,b1,b2,c) to represent the line such as $y = a1/a2*x + b1/b2$ or $x = c$   
    def parameters(self, pt1, pt2):
        if pt1.x == pt2.x:
            c = pt1.x
            return (0,0,0,0,c)
        else:
            a1, a2 = pt1.y-pt2.y, pt1.x-pt2.x
            gcd = self.gcd(a1,a2)
            a1, a2 = a1 / gcd, a2 / gcd
            b1, b2 = a2*pt1.y - a1*pt1.x, a2
            gcd = self.gcd(b1,b2)
            b1, b2 = b1 / gcd, b2 / gcd
            return (a1,a2,b1,b2,0)


    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points) <= 1:
            return len(points)
        lineDict = dict()
        for i in xrange(len(points)):
            for j in xrange(i+1,len(points)):
                pt1,pt2 = points[i],points[j]
                params = self.parameters(pt1, pt2)
                if params not in lineDict:
                    lineDict[params] = set()
                lineDict[params].add(i)
                lineDict[params].add(j)

        maxSum = 0
        for (key,value) in lineDict.items():
            if len(value) > maxSum:
                maxSum = len(value)
        
        return maxSum






