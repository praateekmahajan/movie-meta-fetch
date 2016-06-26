import os
import requests
import json

currentDir = os.getcwd()
print "Your current directory is : " 
print currentDir
flag = raw_input("Is this where your movies are? (y/n)")

if(flag=="n"):
	currentDir = raw_input("Please input the full address to your directory where movies are.")

dirs = os.listdir(currentDir)
print dirs
totalmovies = len(dirs)
print len(dirs)
counter = 0
errorflag = 0
finaljson = "{\n\t\"data\": \n\t\t[\n"
errorfile = open("ERRORLOG", "w")

for filename in dirs:
    if (filename=='main.py'):
	totalmovies=totalmovies-1
    if (filename=='content.txt'):
	totalmovies = totalmovies-1
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
        filename = filename.replace(".avi", "")
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
        	url = 'http://www.omdbapi.com/?t={0}'.format(moviename)
        elif(year.isdigit()  and len(year)==4):
	        url = 'http://www.omdbapi.com/?t={0}&y={1}'.format(moviename, year)
        else:
            errorfile.write(originalfile + " -- File name has error in format" + "\n")
            errorflag = 1
            # totalmovies = totalmovies - 1

        counter = counter + 1
        fetchedDetails = requests.get(url)
        details = fetchedDetails.content
        json1 = json.loads(details)
        if json1['Response'] == "False":
            errorflag = 1
            errorfile.write(originalfile + " -- API Error : " + json1['Error'] + " URL : " + url + "\n")
            # totalmovies = totalmovies - 1
            
        else:
            movieTitle = moviename
            movieYear = ''
            movieRuntime = ''
            movieGenre = ''
            moviePlot = ''
            movieMeta = ''
            movieImdb = ''
            movieAwards = ''
            if json1['Runtime'] == "N/A":
            	continue
            if json1['Year']:
                movieYear = json1['Year'].encode('utf-8').replace('"','\\"')
            if (json1['Runtime']):
                movieRuntime = json1['Runtime'].encode('utf-8').replace('"','\\"')
            if json1['Genre']:
                movieGenre = json1['Genre'].encode('utf-8').replace('"','\\"')
            if json1['Plot']:
                moviePlot = json1['Plot'].encode('utf-8').replace('"','\\"')
            if json1['Metascore'] == "N/A":
		movieMeta = 0
	    elif json1['Metascore']:
		movieMeta = json1['Metascore'].encode('utf-8').replace('"','\\"')
            if json1['imdbRating'] == "N/A":
		movieImdb = 0
	    elif json1['imdbRating']:
	        movieImdb = json1['imdbRating'].encode('utf-8').replace('"','\\"')
            if json1['Awards']:
                movieAwards = json1['Awards'].encode('utf-8').replace('"','\\"')
            
	    print originalfile + " was successful"

            jsonpart = '\t\t\t["{}","{}","{}","{}","{}","{}","{}","{}"]'.format(movieTitle, movieYear, movieRuntime, movieImdb, movieMeta, moviePlot, movieGenre, movieAwards)
            if counter != totalmovies:

                finaljson = ''.join([finaljson, jsonpart, " , \n"])
                # put coma
            else:
                finaljson = ''.join([finaljson, jsonpart])

finaljson = ''.join([finaljson, "\n\t\t]\n}"])
fh = open("content.txt", "w")
fh.write(finaljson)
fh.close()
errorfile.close()

