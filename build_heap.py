# python3
def min_heapify(data, size):
    n=data.len()
    leftChild=left(n)
    rigthChild=right(n)
    if leftChild< len(data) and data[leftChild]< data[n]:
        smallest= leftChild
    else:
        smallest= n
    if rigthChild <len(data) and data[rigthChild]<data[smallest]:
        smallest=rigthChild
    if smallest != n:
        data[n], data[smallest]= data[smallest], data[n]
    def left(n):
        return 2*n+1
    
    def rigth(n):
        return 2*n+2
def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    k= int((len(data)//2)-1):
    for i in range (k, -1, -1)
        min_heapify(data, n)

    return swaps


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
        data =list(map(int, dataLasa.split()))))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
