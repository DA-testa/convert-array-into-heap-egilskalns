# python3
import sys
import threading

swaps = []
def build_heap(data,i):
    for k in range(i,-1,-1):
        check(data,k)
def check(data,j):
    min=j
    if 2*j+1 < len(data) and data[2*j+1] < data[j]:
        min=2*j+1

    if 2*j+2 < len(data) and data[min] > data[2*j+2]:
        min=2*j+2

    if min != j:
        swaps.append(j)
        swaps.append(min)
        data[j], data[min] = data[min], data[j]
        check(data,min)

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
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()