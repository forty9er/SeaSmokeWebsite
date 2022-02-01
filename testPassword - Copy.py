#password test

systemPassword = '1234'
counter = 0

while counter <= 2:
        counter = counter + 1
        print()
        userPassword = input("password: ")
        print()

        if userPassword == systemPassword:
                print("Password is a match!")
                break
        else:
                if counter == 1:
                        print("--->Password does NOT match.")
                        print()
                        print("Try again")
                elif counter == 2:
                        print("--->Password does NOT match.")
                        print()
                        print("Take a deep breath.  Try again")
                        
else: 
        print("You entered the wrong password too many times.  Sorry, try again later.")


#print(systemPassword)
#print(userPassword)
#print(counter)
