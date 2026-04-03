class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        speedMap = {}
        
        for i, car in enumerate(position):
            speedMap[car] = speed[i]

        fleets = []

        for i, car in enumerate(sorted(position)[::-1]):
            fleets.append((target-car)/speedMap[car])
            if (i > 0) and (fleets[-1] <= fleets[-2]):
                fleets.pop()
        
        return len(fleets)

