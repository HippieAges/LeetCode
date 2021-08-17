class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # brute-force solution O(n^2) time, O(1) space
        
#         tank = 0
#         travel_cost = 0
#         gas_len = len(gas)
#         for idx in range(gas_len):
#             tank = gas[idx]
#             if tank - cost[idx] < 0:
#                 continue
#             for station_idx in range(idx, idx + gas_len + 1):
#                 if (travel_cost := tank - cost[station_idx % gas_len]) < 0:
#                     break
#                 elif station_idx != idx and station_idx % gas_len == idx:
#                     return idx
#                 tank = travel_cost + gas[ (station_idx + 1) % gas_len]
        
#         return -1
    
        # LeetCode optimized solution (couldn't come up with the solution myself)
        # O(n) time and O(1) space
        if sum(gas) < sum(cost):
            return -1
        
        curr_tank = 0
        starting_station = 0
        for idx in range(len(gas)):
            curr_tank += gas[idx] - cost[idx]
            if curr_tank < 0:
                curr_tank = 0
                starting_station = idx + 1
        return starting_station