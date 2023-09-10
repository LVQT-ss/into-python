class Solution(object):
    def twoSum(self, nums, target):
        prevMap = {}  # Một từ điển sẽ lưu trữ giá trị và chỉ mục của chúng

        for i, n in enumerate(nums):
            diff = target - n  # Tìm giá trị cần thiết để đạt được mục tiêu
            if diff in prevMap:  # Kiểm tra xem giá trị cần thiết đã xuất hiện trước đó trong mảng hay chưa
                return [prevMap[diff], i]  # Trả về chỉ mục của giá trị cần thiết và chỉ mục hiện tại
            prevMap[n] = i  # Lưu trữ giá trị hiện tại và chỉ mục của nó trong từ điển

        return None  # Trường hợp không tìm thấy cặp số nào thỏa mãn

# Example usage:
# nums = [2, 7, 11, 15], target = 9
# twoSum(nums, target) sẽ trả về [0, 1] vì nums[0] + nums[1] = 2 + 7 = 9

    

# https://leetcode.com/problems/two-sum/submissions/