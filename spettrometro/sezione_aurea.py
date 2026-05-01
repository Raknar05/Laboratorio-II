#!/usr/bin/python

def sezioneAureaMin (
    g,              # funzione di cui trovare lo zero
    x0,             # estremo dell'intervallo          
    x1,             # altro estremo dell'intervallo         
    prec = 0.0001): # precisione della funzione        
    '''
    Funzione che calcola estremanti
    con il metodo della sezione aurea
    '''

    r = 0.618
    x2 = 0.
    x3 = 0. 
    larghezza = abs (x1 - x0)
     
    while (larghezza > prec):
        x2 = x0 + r * (x1 - x0) 
        x3 = x0 + (1. - r) * (x1 - x0)  
      
        # si restringe l'intervallo tenendo fisso uno dei due estremi e spostando l'altro        
        if (g (x3) > g (x2)): 
            x0 = x3
            # x1 = x1  this extreme does not change       
        else :
            x1 = x2
            # x0 = x0  this extreme does not change         
            
        larghezza = abs (x1-x0)             
                                   
    return (x0 + x1) / 2. 


# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 


def sezioneAureaMin_ricorsiva (
    g,              # funzione di cui trovare lo zero
    x0,             # estremo dell'intervallo          
    x1,             # altro estremo dell'intervallo         
    prec = 0.0001): # precisione della funzione        
    '''
    Funzione che calcola estremanti
    con il metodo della sezione aurea
    implementata ricorsivamente
    '''

    r = 0.618
    x2 = x0 + r * (x1 - x0)
    x3 = x0 + (1. - r) * (x1 - x0) 
    larghezza = abs (x1 - x0)

    if (larghezza < prec)  : return ( x0 + x1) / 2.
    elif (g (x3) > g (x2)) : return sezioneAureaMin_ricorsiva (g, x3, x1, prec)
    else                   : return sezioneAureaMin_ricorsiva (g, x0, x2, prec)   


# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 


def sezioneAureaEffMin (
    g,              # funzione di cui trovare lo zero
    x0,             # estremo dell'intervallo          
    x1,             # altro estremo dell'intervallo         
    prec = 0.0001): # precisione della funzione        
    '''
    Funzione che calcola estremanti
    con il metodo della sezione aurea,
    riutilizzando nel ciclo uno dei punti calcolati 
    nell'iterazione precedente
    '''

    r = 0.618
    x2 = x0 + r * (x1 - x0)
    g_x2 = g (x2)
    x3 = 0. 
    larghezza = abs (x1 - x0)
     
    while (larghezza > prec):

        x3 = x0 + (1. - r) * (x1 - x0)
        g_x3 = g (x3)
        # si restringe l'intervallo tenendo fisso uno dei due estremi e spostando l'altro        
        if (g_x3 < g_x2):
            # x0 = x0 this extreme does not change
            x1 = x2
            x2 = x3
            g_x2 = g_x3
        else :
            x0 = x1
            x1 = x3
            # x2 = x2 this point does not change

        larghezza = abs (x1-x0)             
                                   
    return (x0 + x1) / 2. 


# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 


def sezioneAureaEffMin_ricorsiva (
    g,              # funzione di cui trovare lo zero
    x0,             # estremo dell'intervallo          
    x1,             # altro estremo dell'intervallo   
    x2,             # punto intermedio dell'intervallo 
    g_x2,           # valore della funzione g in x2     
    prec = 0.0001): # precisione della funzione        
    '''
    Funzione che calcola estremanti
    con il metodo della sezione aurea
    implementata ricorsivamente,
    riutilizzando nel ciclo uno dei punti calcolati 
    nell'iterazione precedente.
    '''

    r = 0.618
    x3 = x0 + (1. - r) * (x1 - x0) 
    g_x3 = g (x3)
    larghezza = abs (x1 - x0)

    if (larghezza < prec)  : return (x0 + x1) / 2.
    elif g_x3 < g_x2 : return sezioneAureaEffMin_ricorsiva (g, x0, x2, x3, g_x3, prec)
    else             : return sezioneAureaEffMin_ricorsiva (g, x1, x3, x2, g_x2, prec)   


# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 


def sezioneAureaMax (
    g,              # funzione di cui trovare lo zero
    x0,             # estremo dell'intervallo          
    x1,             # altro estremo dell'intervallo         
    prec = 0.0001): # precisione della funzione        
    '''
    Funzione che calcola estremanti
    con il metodo della sezione aurea
    '''

    r = 0.618
    x2 = 0.
    x3 = 0. 
    larghezza = abs (x1 - x0)
     
    while (larghezza > prec):
        x2 = x0 + r * (x1 - x0) 
        x3 = x0 + (1. - r) * (x1 - x0)  
      
        # si restringe l'intervallo tenendo fisso uno dei due estremi e spostando l'altro        
        if (g (x3) < g (x2)): 
            x0 = x3
            # x1 = x1   this extreme does not change      
        else :
            x1 = x2
            # x0 = x0   this extreme does not change
            
        larghezza = abs (x1-x0)             
                                   
    return (x0 + x1) / 2. 



# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 


def sezioneAureaMax_ricorsiva (
    g,              # funzione di cui trovare lo zero
    x0,             # estremo dell'intervallo          
    x1,             # altro estremo dell'intervallo         
    prec = 0.0001): # precisione della funzione        
    '''
    Funzione che calcola estremanti
    con il metodo della sezione aurea
    implementata ricorsivamente
    '''

    r = 0.618
    x2 = x0 + r * (x1 - x0)
    x3 = x0 + (1. - r) * (x1 - x0) 
    larghezza = abs (x1 - x0)

    if (larghezza < prec)  : return ( x0 + x1) / 2.
    elif (g (x3) < g (x2)) : return sezioneAureaMax_ricorsiva (g, x3, x1, prec)
    else                   : return sezioneAureaMax_ricorsiva (g, x0, x2, prec)   

