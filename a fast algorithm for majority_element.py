'''
Majority Element

Question:
Check whether a given sequence of numbers contains an element that appears more than half of the times.
Input: 
A sequence of n integers.
Output:
1,
if there is an element that is repeated more than n/2times, and 0 otherwise.
'''
def majority_element_naive(elements):
    elements.sort()
    n=len(elements)
    for i in range(0,int(n/2)+1):
        if i+int(n/2)<=n-1 and elements[i+int(n/2)]==elements[i] :
            return 1
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
