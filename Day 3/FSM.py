state=1
while(1):
    transit=input("Enter a letter: ")
    print("You have entered ",transit)
    if state==1:
        if transit=='A':
            state=2
    elif state==2:
        if transit=='B':
            state=3
        elif transit=='C':
            state=1
    elif state==3:
        if transit=='D':
            state=1
    print("Right now you are at state: ",state)
    if transit=='E':
        break