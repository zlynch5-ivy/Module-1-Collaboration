class Solution:
    def firstSearch(arr, k):
        lower = 0
        higher = len(arr) - 1
        ans = -1
        
        while lower <= higher:
            middle = lower + (higher - lower) // 2
            
            if arr[middle] == k:
                ans = middle
                higher = middle - 1
            elif arr[middle] < k:
                lower = middle + 1
            else:
                higher = middle - 1
        
        return ans
    
    
arr = [1, 2, 3, 4, 5]
k = 4

print(f"First Occurrence: {Solution.firstSearch(arr, k)}")