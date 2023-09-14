from ast import List  # Import module List from ast (abstract syntax tree) for type hinting

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bước 1: Đếm tần suất xuất hiện của mỗi số trong nums
        count = {}

        # Bước 2: Tạo danh sách các danh sách con để nhóm các số theo tần suất xuất hiện của họ
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)  # Tăng số lần xuất hiện của mỗi số
        
        # Bước 3: Nhóm các số theo tần suất xuất hiện của họ
        for n, c in count.items():
            freq[c].append(n) 

        res = []  # Khởi tạo danh sách kết quả

        # Bước 4: Xây dựng danh sách kết quả bằng cách lặp qua freq từ tần suất cao đến tần suất thấp
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)  # Thêm các số vào danh sách kết quả
                if len(res) == k:
                    return res  # Trả về danh sách kết quả khi đã thu thập đủ k phần tử


        # https://leetcode.com/problems/top-k-frequent-elements/
                


            