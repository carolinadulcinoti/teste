segundos=int(input("Por favor, entre com o número de segundos que deseja converter"))
a=segundos//86400 
resto=segundos%86400
b=resto//3600
resto2=resto%3600
c=resto2//60
d=resto2%60
print (a, "dias",b, "horas," ,c, "minutos e" ,d, "segundos.")