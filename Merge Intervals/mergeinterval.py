intervals = [[1,3],[2,6],[8,10],[15,18]]

def mergeint(intervals):
    intervals.sort(key = lambda i:i[0])
    result = [intervals[0]]
    for start , end in intervals[1:]:
        lastend = result[-1][1]
        if start <= lastend:
            result[-1][1] = max(end , lastend)
        else:
            result.append([start,end])
    return result

print(mergeint(intervals))