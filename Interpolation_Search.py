#Contributed by @Hinal-Srivastava

def interpolation_search(lst,n,element):
    start = 0
    end = n-1
    while(start>=end and element>=start and element<=end):
        pos=int(start + (((end-start)/(lst[end]-lst[start])) * (element-lst[start])) )
        if(element == lst[pos]):
            print('Element Found')
        elif(element>lst[pos]):
            start=pos+1
        elif(element<lst[pos]):
            end=pos-1
        else:
            print('Element not Found')           

#Driver Program
lst=[]
n = int(input('Number of elements: '))
print('Enter elements ', end='')
for i in range(n):
    lst.append(int(input()))
lst.sort()    
element = int(input('Search element: '))    
print(interpolation_search(lst,n,element))    