while True :
    min=0
    max=100
    avg=int((max-min)/2)
    
    x=input("press 'y' for start (q:quit) : ")
    if x=='y':

        
        while True: 
            z=input(f"Your Num Greather Than {avg} (y,n)(r:restart)?")
            
            if z=='y':
                min=avg
                avg=int((max+min)/2)     
            elif z=='n':
                max=avg
                avg=int((max+min)/2)
                
            elif z=='r':
                min=0
                max=100
                avg=50
                
            else:
                print("pls answer by 'y' or 'n' !")

     
            if max-min <= 1 :
                c=input(f"your num is : {max} (y or n)? ")
                if c=='y':
                    print(f"\n    >> Your Nnm is: {max} <<\n")
                    break
                else:
                    print(f"\n    >> Your Nnm is: {min} <<\n")
                    break

                
                
    elif x=='q':
        break
    
    else:
        print("pls answer by 'y' !")
