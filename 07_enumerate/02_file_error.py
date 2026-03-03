#------------------------------------------
# file = open('youtube.txt','w')
# try:
#     file.write("hello")             #that syntax also work

# finally:
#     file.close()

#-------------------------------------------

with open("youtube.txt","w") as file:
    file.write("hello")             #this is easier syntax
