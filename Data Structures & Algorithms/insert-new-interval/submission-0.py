class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = []
        for i, interval in enumerate(intervals):
            # non overlapping before
            if interval[0] > newInterval[1]:
                newIntervals.append(newInterval)
                return newIntervals + intervals[i:]
            # non overlapping after
            elif interval[1] < newInterval[0]:
                newIntervals.append(interval)
                
            # overlapping
            else:
                newInterval = [min(interval[0], newInterval[0]), 
                    max(interval[1], newInterval[1])]
        
        newIntervals.append(newInterval)

        return newIntervals

               


                

        