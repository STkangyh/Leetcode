class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 1
        num_cnt = 1
        for i in range(1, len(nums)): ## 1. for 문으로 리스트를 탐색한다.
            if nums[cnt] in nums[:cnt] and num_cnt >= 2: ## 2. 인덱스의 원소가 인덱스 이전까지의 원소들이 포함된 리스트 안에 존재하는지 확인한다.
                del nums[cnt] ## 3. 존재한다면 중복된 원소이므로, 제거해준다.
                cnt -= 1
            elif nums[cnt] in nums[:cnt] and num_cnt < 2:
                num_cnt += 1
            else:
                num_cnt = 1
            cnt += 1