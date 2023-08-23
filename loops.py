while True:
    try:
        print(2 == int(input("what is x?")))
    except:
        print("An exception occured") 
    else:
        print("it worked")       
        break