# // We have a set of drones that are positioned over an area they are tasked with
# // searching. Each of the drones has a mounted camera that can view a section of
# // the area below.
# //
# // Each drone's viewable section of the search area can be
# // defined as a circle centered at some (x, y) point on the ground.
# // Example viewable area: [x, y, radius] (type: List[int], size: 3)
# //
# // On the ground, there are several targets that need to be looked at by the
# // drones' mounted cameras. Each target can be defined as an (x, y) point.
# // Example target: [x, y] (type: List[int], size: 2)
# //
# // Given a vector of viewable areas and a vector of ground targets, write a
# // function or set of functions to determine how many targets are viewable by
# // each drone's camera.
# //
# //
# // Example 1:
# //
# // targets: [[1,3],[3,3],[5,3],[2,2]]
# // viewable areas: [[2,3,1],[4,3,1],[1,1,2]]
# //
# // viewable target counts: [3, 2, 2]
# //
# // Example 2:
# //
# // targets: [[1,1],[2,2],[3,3],[4,4],[5,5]]
# // viewable areas: [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
# //
# // viewable target counts: [2, 3, 2, 4]
from typing import List
def numTargets(targets: List[List[int]], viewableareas: List[List[int]]) -> List[int]:
    res = []
    for viewable in viewableareas:
        x1, y1, r = viewable[0], viewable[1], viewable[2]
        targets_viewable = 0
        for coords in targets:
            x3 = x1 - coords[0]
            y3 = y1 - coords[1]
            if (x3**2 + y3**2) <= (r**2):
                targets_viewable += 1
        res.append(targets_viewable)
    return res
     

print(numTargets([[1,3],[3,3],[5,3],[2,2]],[[2,3,1],[4,3,1],[1,1,2]])) # expected [3, 2, 2]
