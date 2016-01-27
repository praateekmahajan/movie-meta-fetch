import os
currentDir = os.getcwd()
print "Your current directory is : " 
print currentDir
flag = raw_input("Is this where your movies are? (y/n)")

if(flag=="n"):
	currentDir = raw_input("Please input the full address to your directory where movies are.")

dirs = os.listdir(currentDir)

counter = 0
finaljson = "{\n\t\"data\": \n\t\t[\n"
errorfile = open("ERRORLOG", "w")

for filename in dirs:
    if (filename != 'main.py' and filename!='content.txt'):
    	originalfile = filename
        filename = filename.replace("(", "")
        filename = filename.replace(")", "")
        filename = filename.replace("[", "")
        filename = filename.replace("]", "")
        filename = filename.replace("1080p", "")
        filename = filename.replace("720p", "")
        filename = filename.replace("HDRiP", "")
        filename = filename.replace("DvDRiP", "")
        filename = filename.replace("BRRip", "")
        filename = filename.replace(".mp4", "")
        filename = filename.replace(".flv", "")
        filename = filename.replace(".mkv", "")
        filename = filename.replace(".txt", "")
        # print filename
        filename = filename.rstrip()
        year = filename.split(" ")[-1]

        moviename = filename.replace(year, "")       
        moviename = moviename.rstrip()
    	if(year.isalpha()):
    		moviename = moviename + " " + year    
    		moviename=moviename.rstrip()
    		print moviename + " y:N/A"
        elif(year.isdigit()  and len(year)==4):
	        print moviename + " y:" + year
        else:
        	errorfile.write(originalfile + "\n")
        # counter = counter+1


errorfile.close()