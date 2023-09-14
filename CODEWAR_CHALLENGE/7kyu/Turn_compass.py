def direction(facing, turn):
    # Danh sách các hướng có thể.
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

    # Số lần quay hướng (45 độ/lần).
    turns = turn // 45

    # Tìm chỉ số của hướng ban đầu trong danh sách.
    start_idx = directions.index(facing)

    # Tính chỉ số của hướng sau khi đã quay, bao gồm việc quay vòng nếu cần.
    end_idx = (start_idx + turns) % len(directions)

    # Trả về hướng mới sau khi quay.
    return directions[end_idx]

# https://www.codewars.com/kata/61a8c3a9e5a7b9004a48ccc2/train/python
