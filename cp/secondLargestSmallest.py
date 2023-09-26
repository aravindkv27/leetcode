def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
   

    largest = a[0]
    smallest = a[0]

    secondLargest = a[0]
    secondSmallest = n ** 10

    for ele in a:

        if ele > largest:
            secondLargest = largest
            largest = ele
        
        elif ele < largest and ele > secondLargest:
            secondLargest = ele

        if ele < smallest:
            secondSmallest = smallest
            smallest = ele
        
        elif ele > smallest and ele < secondSmallest:
            secondSmallest = ele

    return [secondLargest, secondSmallest]