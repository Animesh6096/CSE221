file1 = open('Lab3/input3.txt','r')
file2 = open('Lab3/output3.txt','w')

def swapi(arr,idx1,idx2):
    check=arr[idx1]
    arr[idx1]=arr[idx2]
    arr[idx2]=check
def pivot(arr,start,end):
    element=arr[end]


    for i in range(start,end):
        if arr[i]<element:
            swapi(arr,i,start)
            start+=1
    swapi(arr,end,start)
    return start

def quick_sort(arr,start,end):
    if start<end:
        pivot_idx=pivot(arr,start,end)
        quick_sort(arr,start,pivot_idx-1)
        quick_sort(arr,pivot_idx+1,end)
    return arr

n=file1.readlines()
n1=int(n[0])
n2=n[1].split()

arr=[int(i) for i in n2]
file2.write(str(quick_sort(arr,0,n1-1)))


file1.close()
file2.close()