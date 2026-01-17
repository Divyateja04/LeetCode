class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        n = len(bottomLeft)
        bestSide = 0

        for a in range(n):
            leftA, bottomA = bottomLeft[a]
            rightA, topA = topRight[a]

            if rightA - leftA <= bestSide or topA - bottomA <= bestSide:
                continue

            for b in range(a + 1, n):
                leftB, bottomB = bottomLeft[b]
                rightB, topB = topRight[b]

                overlapLeft = max(leftA, leftB)
                overlapBottom = max(bottomA, bottomB)
                overlapRight = min(rightA, rightB)
                overlapTop = min(topA, topB)

                if overlapLeft < overlapRight and overlapBottom < overlapTop:
                    width = overlapRight - overlapLeft
                    height = overlapTop - overlapBottom
                    side = min(width, height)
                    bestSide = max(bestSide, side)

        return bestSide * bestSide