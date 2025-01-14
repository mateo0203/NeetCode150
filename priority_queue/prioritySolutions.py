import heapq
class Solutions:
    def meetingRoomsTwo(self, intervals: list[tuple]):
        #store end times in queue, to keep track of the meeting which ends sooner
        #process the list of intervals in order, to process new meetings that arrive
        heap = []
        intervals.sort()

        for interval in intervals:
            #new meeting needs room
            if heap == [] or heap[0] > interval[0]:
                heapq.heappush(heap, interval[1])
            #new meeting can use the room of the meeting that last ended
            else:
                heapq.heapreplace(heap, interval[1])
        return len(heap)
    
    #Time Complexity: O(nlogn)[sorting intervals] + O(nlogn)[iterating intervals and pushing to heap] = O(nlogn)
    #Space Complexity: O(n)[heap]