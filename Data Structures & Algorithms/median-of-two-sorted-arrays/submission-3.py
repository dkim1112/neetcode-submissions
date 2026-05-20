class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # safe to assume that both arrays are sorted.
        len1, len2 = len(nums1), len(nums2)
        
        # 2 pointer - each iterates ind. arrays
        # we are simulating merging of two arrays by moving 2 pointers together
        i, j = 0, 0
        median1 = median2 = 0

        tot_num_of_iteration = (len1 + len2) // 2 + 1

        for cnt in range(tot_num_of_iteration):
            median2 = median1
            # at each step, choose the smaller of two current elements
            if i < len1 and j < len2: # both in valid range
                if nums1[i] > nums2[j]:
                    median1 = nums2[j]
                    j += 1
                else:
                    median1 = nums1[i]
                    i += 1
            elif i < len1: # j is not < len2
                median1 = nums1[i]
                i += 1
            else:
                median1 = nums2[j]
                j += 1
            
        # if total size = odd, choose last picked val
        if (len1 + len2) % 2 == 1:
            return float(median1)
        # else, find average of last two vals
        else:
            return (median1 + median2) / 2.0