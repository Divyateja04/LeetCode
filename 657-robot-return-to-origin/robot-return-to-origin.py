class Solution(object):
    def judgeCircle(self, moves):
        if moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D'):
            return True
        return False
