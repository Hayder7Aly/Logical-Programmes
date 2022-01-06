t=(1,2.4,True,False,None,2,2.3,3+4j,4,2-2j,'haider',3,'jutt')
t_int,t_float,t_complex,t_bol,t_none,t_str=[],[],[],[],[],[]
for item in t:
    t_int.append(item) if type(item) == int else t_float.append(item) if type(item)==float else t_complex.append(item) if type(item)==complex else t_bol.append(item) if type(item)==bool else t_str.append(item) if type(item)==str else t_none.append(item) 
print(f"{tuple(t_int)}\n{tuple(t_float)}\n{tuple(t_str)}\n{tuple(t_complex)}\n{tuple(t_none)}\n{tuple(t_bol)}")
input()