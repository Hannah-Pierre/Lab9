############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.
Patientinfo = []
print "what is your temperature?"
usertemp = raw_input()
print "Have you been sick in the last 24 hours? 1 for no 2 for yes."
usersick = raw_input()
print "have you recently travelled to West Africa? 1 for no 2 for yes"
userafrica = raw_input()


while() :
    if usertemp in patientinfo > 105 :
        print "you're sick" 
    if usertemp in patientinfo > 102 and usersick == 2 :
        print "you're sick"
    if usertemp in patientinfo > 100 or usersick in patientinfo == 2 and userafrica in patientinfo == 2 :
        print "you're sick"
        
