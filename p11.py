class Solution:
    def maxArea(self, height):
        if not height or len(height) <= 1:
            return 0
        result = 0
        left_index = 0
        right_index = len(height) - 1
        result = min(height[left_index], height[right_index]) * (right_index-left_index)
        last_area = result
        while left_index < right_index:
            if height[left_index] < height[right_index]:
                for i in range(left_index+1, right_index):
                    # 如果找到的值小于最左边的值，不需要判断，直接返回
                    if height[i] <= height[left_index]:
                        continue
                    if height[i] > height[right_index]:
                        left_index = i
                        tmp_area = height[right_index] * (right_index-i)
                        last_area = tmp_area
                        if tmp_area > result:
                            result = tmp_area
                        
                        break
                    tmp_area = height[i] * (right_index - i)
                    if tmp_area > result:
                        result = tmp_area
                    if tmp_area > last_area:
                        left_index = i
                    last_area = tmp_area
                else:
                    left_index = right_index
            else:
                for i in range(right_index-1, left_index, -1):
                    # 如果找到的值小于最右边的值，不需要判断，直接返回
                    if height[i] <= height[right_index]:
                        continue
                    if height[i] > height[left_index]:
                        right_index = i
                        tmp_area = height[left_index] * (i-left_index)
                        last_area = tmp_area
                        if tmp_area > result:
                            result = tmp_area
                        
                        break
                    tmp_area = height[i] * (i - left_index)
                    if tmp_area > result:
                        result = tmp_area
                    if tmp_area > last_area:
                        right_index = i
                    last_area = tmp_area
                else:
                    right_index = left_index
        return result

if __name__ == '__main__':
    solution = Solution()
    height = [1,8,6,2,5,4,8,25,7]

    r = solution.maxArea(height)
    print(r)