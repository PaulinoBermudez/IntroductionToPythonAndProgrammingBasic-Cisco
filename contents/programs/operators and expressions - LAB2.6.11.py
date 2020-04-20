# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))
hour=12
mins=17
dura=59
# put your code here
if dura > 60:
    mihora=int(dura / 60)
    miminuto=int(dura%60)
    # Duración de evento
    print("___Duración del evento___")
    print(mihora, " Horas", miminuto," Minutos")
    print("________________________")
    
    h0=hour
    m0=mins
    hour+=mihora
    mins+=miminuto
    
    print("______Inicialización______")
    print(h0,":", m0," Your time.")
    print("___________________________")
    
    print("______Finalización______")
    print(hour,":", mins," Your time.")
    print("___________________________")
    #############
    #  MINUTOS  #
    #############
    while mins > 59:
        if mins > 59:
            hour+=1
            mins-=60
            print("Event time: ", hour,":",mins)
        elif mins < 0:
            print("No son válidos minutos negativos")
        else:
            print("Finish time event: ", hour,":",mins)
    while hour > 23:
        ###########
        #  HORAS  #
        ###########
        # Horas menores de las 24h 
        if hour <= 23:
            print(hour, ":", mins)
        elif hour < 0:
            print("No son válidos horas negativas")
        elif hour >= 24:
            hour-=24
            print("Finish event: ", hour,":",mins)
        else:
             print("Input Error!!! - ", hour)
else:
    mihora=0
    miminuto=int(dura)
    # Duración de evento
    print("___Duración del evento___")
    print(mihora, " Horas", miminuto," Minutos")
    print("________________________")
    
    h0=hour
    m0=mins
    hour+=mihora
    mins+=miminuto
    
    print("______Inicialización______")
    print(h0,":", m0," Your time.")
    print("___________________________")
    
    # Minutos que sobran
    if mins > 59:
        hour+=1
        mins-=60
        print("Time:", hour, ":", mins)
    else:
        print("Time:", hour, ":", mins)
        
    print("______Finalización______")
    print(hour,":", mins," Your time.")
    print("___________________________")
    