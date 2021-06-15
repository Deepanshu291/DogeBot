# import the module
from prsaw import RandomStuff

# initiate the object
api_key = "RAy26xdL9jdL"
rs = RandomStuff(api_key=api_key) # You can avoid this step if you don't have an api key

# get a response from an endpoint
while True:
   user = input(">")
   if user =="q":
       exit()
   else:    
     response =  rs.get_ai_response(user)
     print(response)
    #  img = rs.get_image(user)
    #  print(img)

# joke =  rs.get_joke()
    #  print(joke)

# close the object once done (recommended)
rs.close()




# rules = [":one: Be respectful.",
# ":two: Sending/Linking any harmful material such as viruses, IP grabbers or harmware results in an immediate and permanent ban.",
# ":three: Use proper grammar and spelling and don't spam.",
# ":four: (Definetely optional) 4) Usage of excessive extreme innapropriate langauge is prohibited",
# ":five: mentioning @everyone, the Moderators or a specific person without proper reason is prohibited.",
# ":six: (Definetely optional) 6) Act civil in Voice Chat.",
# ":seven: Post content in the correct channels.",
# ":eight: Don't post someone's personal information without permission.",
# ":nine: Listen to what Staff says.",
# ":ten: Do not post graphic pictures of minors (<18yo)."]