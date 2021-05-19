#import  
import smtplib 
  
# SMTP session creator
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# TLS for security 
s.starttls() 
  
# Authentication 
s.login("From", "Password") 

#Subject 
subject = "Subject Here"  

# message to be sent 
message = "Message here"
  
# sending the mail 
s.sendmail("From", "To" , subject, message) 
  
# terminating the session 
s.quit() 

print("sent")
