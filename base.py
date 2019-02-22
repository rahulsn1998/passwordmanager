import statistics
class BasePasswordManager:
    old_passwords = []
    l=len(old_passwords)
    def get_password():
            if BasePasswordManager.l!=0:
               pas=BasePasswordManager.old_passwords[BasePasswordManager.l-1]
               return pas
    
    def is_correct():
        inpas=input('Enter Password : ')
        cpass=BasePasswordManager.get_password()
        print(cpass);
        if inpas==cpass:
          print('Correct Passoword')
        else:
          print('Incorrect Passoword')


          

     

        

        




           


    
            
        
