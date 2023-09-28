def executionTime(execution):
    index={}
    for i in range(len(execution)):
        
        if execution[i] in index:
            index[excution[i]].append(i)
        else:
            index[excution[i]]=[i]
    
    final=0
    for key in index.keys():
        for i in range(len(index[key]))
            final+=ceil(key/(2^i))
    
    return final 
        
    
        
            