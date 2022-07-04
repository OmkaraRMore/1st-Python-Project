#g@g.in
email = input("Enter the mail :")
k,j,d=0,0,0
if (len(email)>=6):
    if(email[0].isalpha()):
        if('@' in email) and (email.count('@') == 1):
            if(email[-4]=='.') or (email[-3]=='.'):
                for i in email:
                    if (i == i.isspace()):
                        k=1
                    elif(i.isalpha()):
                        if (i == i.upper()):
                            j=1
                    elif(i.isdigit()):
                        continue
                    elif(i == '@' or i == '_' or i == '.'): 
                        continue
                    else:
                        d = 1 
                if(k == 1 or j == 1 or d ==1 ):
                    print("error:5 (email entered contains space, try again)")# error :5 is represented by error containing 'space' in mail id 
            else:
                print(" error:4 (Email entered is not containing '.' in it, try again;)")# error :4 is represented by error not containing '.' in mail id           
        else:
            print(" error:3 (Email entered is not containing '@', try again;)")# error :3 is represented by error not containing '@' in mail id 
    else:
        print(" error:2 (Email entered is containing int variable at first, try again;)")# error :2 is represented by error in first variable of mail id
else:
    print(" error:1 (Email entered is too short, try again;)")# error :1 is represented by error in length of mail id 
