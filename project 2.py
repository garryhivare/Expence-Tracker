# Expence Tracker  


print("Welcome To Expence Tracker System")

expencelist=[]

while True:
    print("       ==Menu==     ")
    print(" 1 Adding The Expence")
    print(" 2 View The all Expence")
    print(" 3  Total Sending")
    print(" 4 Exit")
    
    
    choise = int(input("\n -----Enter the Your Choise-----:-"))
    
    # Adding The Expence
    if (choise==1):
        print(" 🙏  Thanks To Adding The Your Kharcha 🙏")
        date=input("\n Enter The Date:--")
        category=input("Enter The Category( Food | Shoping | Cloths | Rashan ):--")
        Detail=input("Entar the Deatails :--")
        amount=float(input("Enter The Amount:--"))
        
        expence={
            "date":date,
            "category":category,
            "Detail":Detail,
            "amount":amount
        }
        
        expencelist.append(expence)
        
        
        print("\n 🙏  Thank You For Adding The Expence  🙏")
        
    # View The All Expence     
    elif(choise==2):
        if(len(expencelist)==0):
            print("\n Bhai Pehele Kharcha Add Kar le ")
        else:
            print("\n ==Your All The Expence==")
            count=0
            for eachkharcha in expencelist:
                print(f"{count}-->{eachkharcha["date"]}  |  {eachkharcha["category"]}  |  {eachkharcha["Detail"]}  |  {eachkharcha["amount"]}")
                count=count+1
                
    # Your Total Spending           
    elif(choise==3):
        total=0
        for eachkharcha in expencelist:
            total=total+eachkharcha["amount"]
        print("\n The Total Kharcha Is :==",total)
        
        
        
        
        
        
    elif(choise==4):
        print("\n Thank U Hamara System yse Karne ke liye ")
        break
    
    
    else:
        print("Envalid Choise")
        
        
    
        
        
        