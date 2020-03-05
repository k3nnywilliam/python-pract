'''
Segment problem:
We define a subarray of size x in n-element array to be a contiguous block
of elements in the inclusive range from index i to index j, where j 
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