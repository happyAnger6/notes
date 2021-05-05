def find_media_sorted_arrays(nums1, nums2):
    m, n = len(nums1), len(nums2)

    def find_kth(nums1, nums2, k):
        m, n = len(nums1), len(nums2)
        if m < n:
            return find_kth(nums2, nums1, k)

        if n == 0:
            return nums1[k-1] 

        if k == 1:
            return min(nums1[0], nums2[0])

        m2 = min(n, (k+1)//2)
        m1 = k - m2
        if nums1[m1-1] < nums2[m2-1]:
            return find_kth(nums1[m1:], nums2, k - m1)
        else:
            return find_kth(nums1, nums2[m2:], k - m2)
        

    total = m + n
    if total % 2 != 0:
        return find_kth(nums1, nums2, total//2 + 1)
    else:
        return (find_kth(nums1, nums2, total//2) + find_kth(nums1, nums2, total//2 + 1))/2

    
if __name__ == "__main__":
    print(find_media_sorted_arrays([1, 3], [2]))
    print(find_media_sorted_arrays([1, 2], [3, 4]))
    