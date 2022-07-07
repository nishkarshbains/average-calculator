#program that finds average
l = []
print("how much number do you want to get the average of")
num = int(input())
for i in range(0,num):
    element = int(input("enter the numbers"))
    l.append(element)

#function for calculating average
def average():
    sum = 0
    for i in l:
        sum = sum+i
        end = sum/len(l)
        
    print(end)

        

    
average()