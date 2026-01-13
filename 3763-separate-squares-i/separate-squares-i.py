class Solution(object):
    def separateSquares(self, squares):
        total_area = 0.0
        events = []
        for _, y, l in squares:
            total_area += float(l) * l
            events.append((y, l))
            events.append((y + l, -l))
        events.sort(key=lambda x: x[0])
        target = total_area / 2.0
        current_area = 0.0
        current_width = 0.0
        prev_y = events[0][0]
        for y, delta in events:
            if y > prev_y:
                height = y - prev_y
                area = current_width * height
                if current_area + area >= target:
                    return prev_y + (target - current_area) / current_width
                current_area += area
                prev_y = y
            current_width += delta
        return float(prev_y)