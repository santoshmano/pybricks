import sys                                                              
multi_line = False                                                                 
single_line = False                                                                
multi_line_continuation = False                                                    
                                                                                   
for line in sys.stdin:                                                             
    #print(line)                                                                   
                                                                                   
    single_line = line.find("//")                                                  
    multi_line = line.find("/*")                                                   
    multi_line_end = line.find("*/")                                               
                                                                                   
    if (single_line>=0) and (multi_line>=0):                                       
        if single_line < multi_line:                                               
            multi_line = -1                                                        
        else:                                                                      
            single_line = -1                                                       
                                                                                   
    if (multi_line>=0):                                                            
        multi_line_continuation = True                                             
                                                                                   
    if (multi_line_end>=0):                                                        
        if multi_line_end > multi_line and  multi_line_continuation:               
            multi_line_continuation = False                                        
              
    line = line.rstrip('\n')
    #print(single_line, multi_line, multi_line_end, multi_line_continuation)        
    if single_line >= 0:                                                           
        print(line[single_line:])                                                  
    elif multi_line >= 0:
        print(line[multi_line:])
    elif multi_line_end >= 0:                                                      
        print(line[:multi_line_end+2])                                       
    elif multi_line_continuation:                                                  
        print(line) 
