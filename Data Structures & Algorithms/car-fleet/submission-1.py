class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1: 
            return 1 

        
        cars = sorted(zip(position, speed), reverse=True)  
        slowestAhead = 0 
        fleets = 0 

        for car in cars: 
            timeToTarget = (target - car[0]) / car[1]
            if timeToTarget > slowestAhead: 
                slowestAhead = timeToTarget 
                fleets += 1 
        
        return fleets