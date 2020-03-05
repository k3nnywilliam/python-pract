'''
Segment problem:
We define a subarray of size x in n-element array to be a contiguous block
of elements in the inclusive range from index i to index j, where
j -i + 1 = x and 0 <= i <= j < n.

For example, given array arr=[8,2,4], the subarrays of size x=2 would be
[8,2] and [2,4]. The minimum values of the two subarrays are [2,2]. The maximum
of those two minimum values is 2. This is the value you want to determine.

Sample input:
x = 1
arr = [1,2 ,3, 1, 2]

Sample output:
3

The subarrays of size x = 1 are [1], [2], [3], [1] and [2].
Because each subarray only contains 1 element, each value is minimal
with respect to the subarray it is in. We return the maximum of these values,
which is 3.
'''


def segment(x, arr):

    if(x == 0 or arr == None):
        return 0

    sublists = []
    i = 0

    while (x <= len(arr)):
        '''
        First we convert the list into sublists
        that start from the i-th element up to the subarray of size x
        and then increment the step by 1 as we go through the list
        '''
        sublists.append(arr[i:x])
        i += 1
        x += 1

        '''
        then we find the minimum values from the sublists.
        Finally, we return the maximum value of those minimum values
        '''
        minvalues = [min(sublist) for sublist in sublists]
    
    return max(minvalues)



if __name__ == '__main__':
    x = 1
    arr = [1, 2, 3, 1, 2]
    print(segment(x, arr)) #answer should be 3