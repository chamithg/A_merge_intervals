class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) < 2: return intervals
        intervals.sort()
        output =[]
        for a,b in intervals:
            if not output:
                output.append([a,b])
            if a > output[-1][1]:
                output.append([a,b])
            elif b > output [-1][1]:
                output [-1][1] = b
            
        
        
        return output
        
        
        
        
obj = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals1 = [[1,4],[4,5]]
intervals3 = [[1,4],[0,4]]
intervals4 = [[2,3],[4,5],[6,7],[8,9],[1,10]]
intervals2 = [[1,4],[2,3]]
print(obj.merge(intervals4))