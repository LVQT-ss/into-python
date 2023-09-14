
# https://leetcode.com/problems/group-anagrams/solutions/3687735/beats-100-c-java-python-beginner-friendly/

from ast import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Tạo một defaultdict (dictionary mở rộng) với giá trị mặc định là một danh sách rỗng.
        # defaultdict cho phép bạn truy cập một khóa mà không cần kiểm tra xem khóa đó đã tồn tại hay chưa.
        res = defaultdict(list) # Map charCount to a list of anagrams

        # Duyệt qua từng chuỗi trong danh sách đầu vào strs
        for s in strs:
            # Khởi tạo một danh sách count chứa 26 phần tử ban đầu đều là 0,
            # đại diện cho số lần xuất hiện của mỗi chữ cái trong tiếng Anh.
            count = [0] * 26

            # Duyệt qua từng ký tự trong chuỗi s
            for c in s:
                # Tính chỉ số của chữ cái c trong bảng chữ cái tiếng Anh
                # và tăng giá trị tại vị trí đó trong danh sách count lên 1.
                count[ord(c) - ord("a")] += 1

            # Chuyển danh sách count thành một tuple để sử dụng làm khóa cho defaultdict.
            # Tại đây, mỗi tuple sẽ biểu diễn một tập hợp các chữ cái và số lần xuất hiện tương ứng trong chuỗi s.
            # Ví dụ: ("a", "b", "c") sẽ biểu diễn một chuỗi có 1 "a", 1 "b", và 1 "c".
            # ("a", "a", "b", "c") sẽ biểu diễn một chuỗi có 2 "a", 1 "b", và 1 "c".
            # Sau đó, thêm chuỗi s vào danh sách giá trị tương ứng với khóa tuple này trong defaultdict.
            res[tuple(count)].append(s)

        # Trả về giá trị của defaultdict, là danh sách các danh sách từ "anagrams".
        return res.values()

# cách làm khác dùng for và sorted 

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        # Tạo một defaultdict (dictionary mở rộng) với giá trị mặc định là một danh sách rỗng.
        # defaultdict cho phép bạn truy cập một khóa mà không cần kiểm tra xem khóa đó đã tồn tại hay chưa.
        anagram_map = defaultdict(list)
        
        # Duyệt qua từng từ trong danh sách đầu vào strs
        for word in strs:
            # Sắp xếp lại các chữ cái của từ và nối chúng lại thành một chuỗi mới.
            # Ví dụ: từ "eat" sau khi sắp xếp sẽ trở thành "aet".
            sorted_word = ''.join(sorted(word))
            
            # Thêm từ gốc vào danh sách giá trị tương ứng với khóa sorted_word trong defaultdict.
            # Nếu khóa sorted_word chưa tồn tại, defaultdict sẽ tạo mới nó và gắn với danh sách rỗng.
            anagram_map[sorted_word].append(word)
        
        # Trả về danh sách các danh sách từ "anagrams".
        return list(anagram_map.values())
