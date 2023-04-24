import re
email = input("What's your email:").strip()

username , domain = email.split("@")

if re.search("@", email):
    # username and domain.endwith and( ".com")
    print ("valid")
    print(email)
  
else:
    print ("invalid")