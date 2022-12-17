class Solution:
    def relativeSortArray(self, arr1, arr2):
        dict={}
        nums,ans = [], []
        
        for val in arr2:
            dict[val] = 0
        
        for val in arr1:
            if val not in dict:
                nums.append(val)
            else: 
                dict[val] += 1
        print(dict)
        for key, val in dict.items():
            print(key,val)
            ans.extend([key]*val)
        
        ans.extend(sorted(nums))
        return ans