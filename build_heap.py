# python3

swaps = []
def build_heap(data,i):
    # print(i)
    
    def check(data,j):
        
        
        if 2*i+1 >= len(data):
            build_heap(data,j-1)

        elif 2*j+1 < len(data) and 2*j+2 >=len(data):
            if data[2*j+1] < data[j]:
                swaps.append(j)
                swaps.append(2*j+1)
                data[j], data[2*j+1] = data[2*j+1], data[j]
                check(data,j//2)
            else:
                build_heap(data,j-1)

        elif 2*j+1 < len(data) and 2*j+2 < len(data):
            if data[2*j+1] < data[j] and data[2*j+1] < data[2*j+2]:
                swaps.append(j)
                swaps.append(2*j+1)
                data[j], data[2*j+1] = data[2*j+1], data[j]
                check(data,j//2)

            if data[2*j+2] < data[j] and data[2*j+1] > data[2*j+2]:
                swaps.append(j)
                swaps.append(2*j+2)
                data[j], data[2*j+2] = data[2*j+2], data[j]
                check(data,j//2)
            else:
                build_heap(data,j-1)
    
    j=i
    if i<0:
        return swaps
    check(data,j)
    i-=1
    
    build_heap(data,i)


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    text=input()
    data=0
    if text == "I":
        n = int(input())
        data = list(map(int, input().split()))

    if text == "F":
        text1="/workspaces/convert-array-into-heap-egilskalns/tests/"
        text2=input()
        file=open(text1+text2,"r")
        text3=file.read()
        file.close()
        text3=text3.replace("\n"," ")
        text3=text3.strip()
        data=[int(i) for i in text3.split(' ')]
        n=data[0]
        data=data[1:]
        # print(data,n)
    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    build_heap(data,n//2)
    
    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    print(len(swaps)//2)
    
    # output all swaps
    for i in range(0,len(swaps)-1,2):
        print(swaps[i],swaps[i+1])

if __name__ == "__main__":
    main()

