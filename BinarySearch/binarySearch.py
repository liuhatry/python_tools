a = [x for x in range(100)]
x = 21

def midfind(a,x):
    min_index = 0
    max_index = len(a) -1
    iter = 0

    print (a)
    while True:
        mid_index =int( (min_index+max_index)/2 )
        iter += 1
        print('Times:', iter)
        print('min:', a[min_index],'max:', a[max_index],'mid:', a[mid_index])
        
        
        if x == a[mid_index]:
            print("find times:", iter)
            return x
        elif x < a[mid_index]:
            max_index = mid_index-1
        elif x> a[mid_index]:
            min_index = mid_index+1
 
midfind(a, x)
