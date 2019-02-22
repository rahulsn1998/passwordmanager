import re
from base import BasePasswordManager

class PasswordManager(BasePasswordManager):
       
    def get_level(p):
        alph = 0
        num = 0
        spc = 0
        spch = re.compile('[@_!#$%^&*()<>?/\|}{~:]')     
        if spch.search(p) != None: 
         spc=1 
        for i in p:
            if i.isalpha():
                alph = 1
            elif i.isdigit():
                num = 1
        if alph==1 and num ==1 and spc == 1:           
         sec = 2
        elif alph==1 and num ==1:           
         sec = 1
        elif alph==0 or num==0:
         sec = 0
        return sec
             
    def set_password():
     newpas=input('Enter new password : ')
     if len(BasePasswordManager.old_passwords)!=0:
         a=PasswordManager.get_level(newpas)
         b=PasswordManager.get_level(BasePasswordManager.get_password())
         print(a,b)
         if a>=b and len(newpas)>5:
            BasePasswordManager.old_passwords.append(newpas)
            print('New password updated')
            BasePasswordManager.l=len(BasePasswordManager.old_passwords)
         else:
            print('Enter stronger password')
            PasswordManager.set_password()
     else:
          if len(newpas)>5:
            BasePasswordManager.old_passwords.append(newpas)
            print('New password updated')
            BasePasswordManager.l=len(BasePasswordManager.old_passwords)
          else:
            print('Enter stronger password')
            PasswordManager.set_password()
     

def main(): 
    print('\n\n\n\nWELCOME ')
    if len(BasePasswordManager.old_passwords)!=0:
        print('''
        Press
        1.Enter Password
        2.Set Password
        3.Exit
        ''')
        o=input('Select option\n')
        if o=='1':
            BasePasswordManager.is_correct()
        elif o=='2':
            PasswordManager.set_password()
        elif o=='3':
            exit()
        else:
            print('Invalid option')
    else:      
        print('There is no Password')
        PasswordManager.set_password()
            
while 1:
 main()




          




       
                
                
            

    

        
        
