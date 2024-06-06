def backtrace(v,m,wt,val,n):
    selcted_item = []

    i = n
    w = m

    while i > 0 and w > 0:
        if v[i][w] != v[i-1][w]:
            selcted_item.append(i)
            w = w- wt[i-1]
            i = i-1
        else:
            i = i -1 
    return selcted_item

def knapsack(m,wt,val,n,sel_item):
    v = [[0 for w in range(m+1)] for i in range(n+1)]
    for i in range(n+1):
        for w in range(m+1):
            if i == 0 or w == 0:
                v[i][w] = 0
            elif wt[i-1] <= w:
                v[i][w] = max(v[i-1][w],val[i-1] + v[i-1][w - wt[i-1]])
            else:
                v[i][w] = v[i-1][w]

    selec_item = backtrace(v,m,wt,val,n)     
    for i in selec_item: sel_item.append(i)        
    return v[n][m]

items = [1,2,3,4]
values = [100,20,60,40]
weights = [3,2,4,1]
capacity = 5
selected_items = []
max_val = knapsack(capacity,weights,values,len(values),selected_items)
print(f"Max Value = {max_val} Selected Items are : {selected_items}")