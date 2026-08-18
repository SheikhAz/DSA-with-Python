intervals = [[1,2],[2,3],[3,4],[1,3]]

def removeover(intervals):
    intervals.sort()
    result = 0
    prevEnd = intervals[0][1]

    for start,end in intervals[1:]:
        if start >= prevEnd:
            prevEnd = end
        else:
            result += 1
            prevEnd = min(end,prevEnd)
    return result