# python3

swaps = []
def build_heap(data,i):
    # print(i)
    
    def check(data,j):
        # print(len(swaps))
        
        # if 2*i+1 >= len(data):
        #     build_heap(data,j-1)
        if 2*j+1 < len(data) and 2*j+2 < len(data) and data[2*j+1] > data[j] and data[j] < data[2*j+2]:
            build_heap(data,j-1)
        if 2*j+1 < len(data) and 2*j+2 >=len(data) and data[2*j+1] < data[j]:
            swaps.append(j)
            swaps.append(2*j+1)
            data[j], data[2*j+1] = data[2*j+1], data[j]
            check(data,j//2)

        if 2*j+1 < len(data) and 2*j+2 < len(data) and data[2*j+1] < data[j] and data[2*j+1] < data[2*j+2]:
            swaps.append(j)
            swaps.append(2*j+1)
            data[j], data[2*j+1] = data[2*j+1], data[j]
            check(data,j//2)

        if 2*j+1 < len(data) and 2*j+2 < len(data) and data[2*j+2] < data[j] and data[2*j+1] > data[2*j+2]:
            swaps.append(j)
            swaps.append(2*j+2)
            data[j], data[2*j+2] = data[2*j+2], data[j]
            check(data,j//2)
        
        build_heap(data,j-1)
    
    j=i
    if i<0:
        return swaps
    check(data,j)
    i-=1
    
    build_heap(data,i)


def main():
    
    text=input()
    data=[]
    n=0
    text1=[]
    text2=[]

    for i, next in enumerate(text):
        if next in "I":
            n = int(input())
            data = list(map(int, input().split()))

    for i, next in enumerate(text):
        if next in "F":
            text1="tests/"
            text2=input()
            file=open(text1+text2,"r")
            text1=file.read()
            file.close()
            text1=text1.replace("\n"," ")
            text1=text1.strip()
            data=[int(i) for i in text1.split(' ')]
            n=data[0]
            data=data[1:]
            print(data)

    assert len(data) == n

    # calls function to assess the data 
    build_heap(data,n//2)
    
    # output how many swaps were made
    print(len(swaps)//2)
    
    # output all swaps
    for i in range(0,len(swaps)-1,2):
        print(swaps[i],swaps[i+1])

if __name__ == "__main__":
    main()
