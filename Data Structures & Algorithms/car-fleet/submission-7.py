class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:        
        # 차 뭉텡이들 (같이 움직이니까) - Fleet
        # (target - position) / speed 를 통해서 "time" 이라는 개념 파생.

        # pair each (postion, speed) and sort descending by position (closeset to farthest from target)
        # this is bc close한얘가 먼저 도착할거임. (think of this as "one road")
        # = list of (p,s)
        pair = [(p,s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)


        # first car forms the first fleet
        fleets = 1
        # = keep track of fleet's time - the time of car closest to target
        fleetPrevTime = (target - pair[0][0]) / pair[0][1]

        # for cars that follow after...
        for i in range(1, len(pair)):
            # currCar = (p,s) => currCar[0] = position, currCar[1] = time
            currCar = pair[i]
            # compute time to reach target
            currTime = (target - currCar[0]) / currCar[1]

            # if currTime < fleetPrevTime, it will catch up and merge.
            if currTime > fleetPrevTime: # = will never catch up to one in front
                fleets += 1
                fleetPrevTime = currTime
        
        return fleets
