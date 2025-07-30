class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      for i , valor_i in  enumerate(nums):
          for n ,valor_n in enumerate(nums):
        
            if i != n:
                soma = valor_i + valor_n
            
                if soma == target:
                    return [i,n]   