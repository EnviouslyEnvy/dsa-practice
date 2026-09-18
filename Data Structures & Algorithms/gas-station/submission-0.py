class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # So we need to see if there exists a starting gas station that can make it in a circle.
        # For all stations on a traversal, if we at the very least have or gain enough gas that is equivalent to starting at that same station.
        # On a successful run visting a station we can cache all visited stations as also being successful? Not necessarily because a run is successful if they meet loop back to the start. But if they loop back to the start they can repeat their steps to visit the same stations as the original run, (once again they have at least as much gas as if they were starting on that space)
        
        # If at some point on the trip you run out of gas, every start point between the start and end is an infeasible starting point.
        # However starting points before can still be viable as you can save up more gas.
        # THERE IS ONLY ONE SOLUTION.
        if sum(gas) < sum(cost):
            return -1
        tank = 0
        start = 0

        for i in range(len(gas)):

            tank += gas[i]-cost[i]
            
            if tank < 0:
                tank = 0
                start = i + 1
        # We don't need any condition if it's impossible in here, that's already covered. We just need to iteratively find one.
        return start