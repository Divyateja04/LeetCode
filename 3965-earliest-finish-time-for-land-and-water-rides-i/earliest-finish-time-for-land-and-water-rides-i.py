class Solution(object):
    def earliestFinishTime(self, landStart, landDur, waterStart, waterDur):
        earliest_end = float('inf')
        for ls, ld in zip(landStart, landDur):
            land_end = ls + ld
            for ws, wd in zip(waterStart, waterDur):
                combined_end = max(land_end, ws) + wd
                earliest_end = min(earliest_end, combined_end)
        for ws, wd in zip(waterStart, waterDur):
            water_end = ws + wd
            for ls, ld in zip(landStart, landDur):
                combined_end = max(water_end, ls) + ld
                earliest_end = min(earliest_end, combined_end)
        return earliest_end