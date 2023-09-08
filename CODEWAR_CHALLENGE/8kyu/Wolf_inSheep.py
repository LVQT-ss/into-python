def warn_the_sheep(queue):
    # Đảo ngược danh sách (queue) để bạn đứng ở cuối danh sách.
    queue = queue[::-1]
    
    # Khởi tạo biến wolf_counter để lưu vị trí của con sói, ban đầu đặt là None.
    wolf_counter = None
    
    # Duyệt qua từng phần tử (animal) và chỉ số (i) trong danh sách đảo ngược.
    for i, animal in enumerate(queue):
        # Kiểm tra nếu phần tử là con sói.
        if animal == 'wolf':
            # Lưu vị trí của con sói và thoát khỏi vòng lặp (break).
            wolf_counter = i
            break  # Thoát khỏi vòng lặp ngay khi tìm thấy con sói.

    # Kiểm tra nếu con sói đứng ngay trước bạn (vị trí cuối danh sách).
    if wolf_counter == 0:
        return 'Pls go away and stop eating my sheep'
    
    # Trả về thông báo thông báo đúng vị trí của con cừu bị sói ăn.
    return f"Oi! Sheep number {wolf_counter}! You are about to be eaten by a wolf!"

# https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15/train/python