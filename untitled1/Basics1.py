my_first_list = [1,2,3,4,5,3,15,12,-8,5.5]
my_first_list.sort()
print(my_first_list)
print(type(my_first_list))
#print(help(my_first_list))
a_mixed_list = [1,2,"Ciao"]
print(a_mixed_list)
my_first_list = [1,2,3,4,5]
def fibo(number):
    if(number>2):
        return fibo(number-1)+fibo(number-2)
    return 1
#print(fibo(36))
def fibo2(number):
    low=1
    big=1
    if(number>2):
        for x in range (2,number):
            k=big
            big=low+big
            low=k
        return big
    else:
        return 1
#print(fibo2(36))
def fibo3(number):
    if(number>2):
        return fibo3(number-1)+fibo3(number-2)
    return 1


def fibo4(number):
    if(number>2):
        big=1
        small=1
        for x in range (2,number):
            k=big
            big=big+small
            small=k
        return big
    return 1
#print(fibo3(36))
#print(fibo4(36))


def area(begin, end):
    k = (end - begin) / 1024
    area=0
    for l in range(0, 1024):
        x = (pow(begin, 2))
        begin += k
        area += ((begin**2)+x)*k/2
    return area


print(area(0,1))

def bubblesort(listt):
    for x in range(0,len(listt)-1):
        for y in range(0,len(listt)-x-1):
            if (listt[y]<listt[y+1]) :
                listt[y], listt[y+1]=listt[y+1],listt[y]
    return listt

listOfNumbers = [4,5,6,1,2]
print(listOfNumbers)
print(bubblesort(listOfNumbers))
print(listOfNumbers)
