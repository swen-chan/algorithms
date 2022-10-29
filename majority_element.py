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
