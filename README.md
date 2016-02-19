# Movie Metadata fetch
Fetch metadata of your movies easily with this script and save them in a html file to view/search for movies according to genre, awards, imdb rating. 


### How to use?
Just run the python file, feed in the directory where all your movies are listed and kaboom! You will get a txt file with json data of all details related to the movie. Upload the *content.txt* and *index.html* in the same folder to view your movie metadata online. For the movie folders/files it coulnd't process it will add the details to the ERRORLOG file.

### How does it work?
This script will not work for everyone, I made it for my personal use and I have a habit of keeping my folders tidy. Generally all the movie files/folder in my hardrive are saved in this format *MOVIE NAME [YEAR]*, in some cases even *MOVIE NAME* would do.
Eg. of dummy folder
[Screenshot of Dummy Movie Folder](http://i.imgur.com/6NcRoiQ.png)

### What details will it fetch?
*   Name
*   Year
*   Time (mins)
*   Rating
*   Metascore
*   Plot
*   Genre
*   Awards

### Technical Details
Gets all the meta data from [OMDB API](www.omdbapi.com)
