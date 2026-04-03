class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # speedMap = {}
        
        # for i, car in enumerate(position):
        #     speedMap[car] = speed[i]

        pairs = [(p, s) for p, s in zip(position, speed)]

        fleets = []

        for p, s in sorted(pairs)[::-1]:
            fleets.append((target-p)/s)
            if len(fleets) >= 2 and (fleets[-1] <= fleets[-2]):
                fleets.pop()
        
        return len(fleets)

