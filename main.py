_arr = [-4,3,-9,0,4,1]

def plusMinus(arr):
    _conts = [0,0,0]
    for x in arr:
        if (x>0):
            _conts[0]+=1
        if (x<0):
            _conts[1]+=1
        if (x==0):
            _conts[2]+=1
    
    print('{:.6f}'.format(_conts[0]/len(arr)))
    print('{:.6f}'.format(_conts[1]/len(arr)))
    print('{:.6f}'.format(_conts[2]/len(arr)))

plusMinus(_arr)
