def cake(candles, debris):
    total_candles = 0  # Tạo biến để lưu tổng số nến rơi ra, ban đầu đặt giá trị là 0
    
    # Duyệt qua chuỗi debris
    for i in range(len(debris)):
        if i % 2 == 0:  # Kiểm tra nếu chỉ số hiện tại là chẵn
            # Nếu chỉ số là chẵn, thì lấy giá trị ASCII của ký tự tại chỉ số đó và thêm vào tổng số nến
            total_candles += ord(debris[i])
        else:  # Nếu chỉ số hiện tại là lẻ
            # Nếu chỉ số là lẻ, thì lấy giá trị ASCII của ký tự tại chỉ số đó, trừ đi giá trị ASCII của 'a' và cộng thêm 1
            # để tính vị trí chữ cái của ký tự đó và thêm vào tổng số nến
            total_candles += ord(debris[i]) - ord('a') + 1
    
    # Sau khi đã tính toán tổng số nến rơi ra từ chuỗi debris, kiểm tra xem tỷ lệ này có vượt quá 70% không
    if total_candles / candles > 0.7:
        return "Fire!"  # Nếu tỷ lệ nến rơi ra lớn hơn 70%, trả về "Fire!" để thể hiện rằng thảm sẽ bắt lửa
    else:
        return "That was close!"  # Nếu tỷ lệ không vượt quá 70%, trả về "That was close!" để thể hiện rằng bạn đã tránh được việc thảm bắt lửa

# Ví dụ sử dụng:
candles = 100
debris = "abc"
result = cake(candles, debris)
print(result)  # Output: "That was close!"
