#Nicholas Norman Tutoring Code Example
#Goal: Check username and password and check for fails 5 times
#Input: Username and Password
#Output: Login successful, login failed

#Notice how my algorithm has become my comments

correctUsername = "npnorman"
correctPassword = "mypassword"

tries = 0 #number of tries
loginAttempt = False #has the user successfully logged in
keepGoing = True #does the loop keep going

#Check if username and password are correct and return a successful login
#while the user has not failed an attempt
while (keepGoing):
    #get username
    username = input("Input username: ")
    #get password
    password = input("Input password: ")
	
    #if username is correct
    if (username == correctUsername):
	    #if password is correct
	    if (password == correctPassword):
	    	#login was successful
        	loginAttempt = True
        	#stop the loop
            keepGoing = False
    else:
        #If failed all five attempts fail, return a false login attempt
        #we need a counter to count to five
        #Increase counter by 1 for every loop (keeps track of tries)
        tries = tries + 1
        #If the counter is greater than or equal to 5, we’ve gone over the allotted tries
        if (tries >= 5):
            #Set login attempt to unsuccessful
            loginAttempt = False
            #Stop the loop
            keepGoing = False

#Finally, return the login attempt success or failure
print("Your login attempt was: ", loginAttempt)
