from pydrive2.auth import GoogleAuth
gauth = GoogleAuth
authurl = gauth.GetAuthUrl().replace("online", "offline")
print(auth
