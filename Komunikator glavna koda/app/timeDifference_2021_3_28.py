def get_time_difference(h1, m1, h2, m2):
    hours = differenceh(h1, m1, h2, m2)
    minutes=differencem(h1, m1, h2, m2)
    return hours, minutes

def differenceh(h1, m1, h2, m2): 
    # convert h1 : m1 into
    # minutes
    t1 = h1 * 60 + m1
      
    # convert h2 : m2 into
    # minutes 
    t2 = h2 * 60 + m2
      
    # calculating the difference
    diff = t2-t1
          
    # calculating hours from
    # difference
    h = (int(diff / 60)) % 24

    return h

def differencem(h1, m1, h2, m2):
    # convert h1 : m1 into
    # minutes
    t1 = h1 * 60 + m1
      
    # convert h2 : m2 into
    # minutes 
    t2 = h2 * 60 + m2
      

          
    # calculating the difference
    diff = t2-t1 #t2: prihod trole, t1 trenutni čas
          
    # calculating minutes from 
    # difference
    m = diff % 60

    return m