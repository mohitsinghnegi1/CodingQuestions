# QUs:https://leetcode.com/problems/task-scheduler/

# SOlution Explaination
# Sample run for understanding how heap and temp are involved in calculating the optimal number of intervals.

# Legend: '->' : heap pop operation
# '#' : idle time

#     [A A A A B B D E]
#     using most frequent first: [A ## A ## A ## A]
#     other jobs in idle time:   [A BD A BE A ## A] i.e. 10 intervals
    
#     HEAP            TEMP                    TIME
#     (-4,A)->        [(-3,A)]                  1
#     (-2,B)->        [(-3,A), (-1,B)]          2
#     (-1,D)->        [(-3,A), (-1,B)]          3
    
#     *********************COOL TIME COMPLETE************************
#     put items in TEMP back to HEAP
    
#     HEAP becomes: [(-3,A), (-1,E), (-1,B)]
    
#     HEAP            TEMP                    TIME
#     (-3,A)->        [(-2,A)]                  4
#     (-1,B)->        [(-2,A)]                  5
#     (-1,E)->        [(-2,A)]                  6
    
#     *********************COOL TIME COMPLETE************************
#     put items in TEMP back to HEAP
    
#     HEAP becomes: [(-2,A)]
    
#     HEAP            TEMP                    TIME
#     (-2,A)->        [(-1,A)]                  7
#     EMPTY                                     8
#     EMPTY                                     9
    
#     *********************COOL TIME COMPLETE************************
#     put items in TEMP back to HEAP
    
#     HEAP becomes: [(-1,A)]
    
#     HEAP            TEMP                    TIME
#     (-1,A)->                                 10
#     EMPTY           EMPTY                  break


from collections import Counter
import heapq

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # the task that are accessed put those tasks in colldown list
        # once cooldown is over , push back those task into heap so that we can access it         # again
        
        
        # this will give a dict with the count
        counter=Counter(tasks)
        heap=[]
        
        for char,count in counter.items():
            heapq.heappush(heap,(-count,char))
        
        time=0# %(n+1)
        taskInCooldown=[]
        
        while(heap or len(taskInCooldown)):
            # print heap,taskInCooldown
            if(time%(n+1)==0):
                # push task to the heap , since cooldown is over
                for count,task in taskInCooldown:
                    heapq.heappush(heap,(count,task))
                taskInCooldown=[]
                
            if(len(heap)):
                count,task=heapq.heappop(heap)
                # if task count is greater then one then only add it to cooldown list
                # otherwise time will pass 
                if(count<-1):
                    taskInCooldown.append((count+1,task))

            time+=1
        return time
                