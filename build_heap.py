# python3
def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    for i in range (n//2, -1, -1):
        min_heapify(data, n, i, swaps)

    return swaps
    #try to find smallest and then swap them places
def min_heapify(data, n, i, swaps):
    i=smallest
    leftChild= 2*i+1
    rigthChild=2*i+2
       

    if leftChild< len(data) and data[leftChild]< data[smallest]:
        smallest= leftChild
    else:
        smallest= n
    if rigthChild <len(data) and data[rigthChild]<data[smallest]:
        smallest=rigthChild
    if smallest != i:
        data[n], data[smallest]= data[smallest], data[i]
        swaps.appen(i, smallest)
        min_heapify(data, n, i, swaps)



def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    text=input()
    text=text.upper()

    # input from keyboard
    
    if text.startswith("I"):
     n = int(input())
     data = list(map(int, input().split()))
    if text.startswith("F"):
        file_name = input()
        file_name = open('./test/'+file_name)
        n = int(file_name.readline())
        dataLasa = file_name.readline()
        data =list(map(int, dataLasa.split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    assert(len(swaps)) <= 4*n
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
