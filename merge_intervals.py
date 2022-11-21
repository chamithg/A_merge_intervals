class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        output =[]
        temp = []
        i = 0
        
        while i< len(intervals):
            
            ## add the first element in temp
            if not temp and not output:
                print("hi")
                temp.append(intervals[i][0])
            elif not temp:
                print("hiww")
                if output[-1][1] < intervals[i][0]:
                    print("hidfdww")
                    temp.append (intervals[i][0])

            ## add the second element in temp
            
            
            if  i == len(intervals)-1:
                temp.append(intervals[i][1])
            else:
                if intervals[i][1] < intervals[i+1][0]:
                    temp.append(intervals[i][1])
                if intervals[i][1] > intervals[i+1][1]:
                    temp.append(intervals[i][1])
                    i += 1
            if len(temp)==2:
                output.append(temp)
                temp = []
            
            i+=1
        
        return output
        
        
        
        
        
obj = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals1 = [[1,4],[4,5]]
intervals3 = [[1,4],[0,4]]
intervals4 =[[2,3],[4,5],[6,7],[8,9],[1,10]]
intervals2 = [[1,4],[2,3]]
print(obj.merge(intervals4))