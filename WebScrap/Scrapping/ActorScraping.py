import urllib
import urllib.request

from bs4 import BeautifulSoup
import json
import logging
import time


class actorClass:

### Actor Scraping Function###
    def actorScarp(self, weburl):

        ACT_LOG = 'actorLogFile.log'
        logging.basicConfig(filename=ACT_LOG)
        #time.sleep(1)
        webPage = urllib.request.urlopen(weburl)
        actorWeb = BeautifulSoup(webPage, "lxml")

        Filmography = []
        FilmLink = []
        FilmSection = False

#find Filmography Table

        for Film in actorWeb.findAll('h2'):
            if (Film.text == 'Filmography[edit]' or Film.text == 'Filmography'):
                FilmSection = True

        if (FilmSection == False):
           logging.error(weburl + ' was not able to be parsed because Filmography section was not found.')
           return None

        table = actorWeb.findAll('table',{"class":"wikitable sortable"})

        if (len(table) == 0):
            table = actorWeb.findAll('table', {"class":"wikitable"})
            if(len(table) == 0):
                # check out side link
                logging.error(weburl + ' was not able to be parsed because Filmography Table was not found.')
                return None

        table = table[0]
        for movie in table.findAll('i'):
            for link in movie.findAll('a'):
                Filmography.append(link.get('title'))
                string = "https://en.wikipedia.org" + link.get('href')
                FilmLink.append(string)


        MovieArr = []
        for a in range(len(Filmography)):
            tempActor = {
                "mName": Filmography[a],
                "mLink": FilmLink[a],
            }
            MovieArr.append(tempActor)


        name = actorWeb.findAll('h1')

        year = actorWeb.findAll('span',{"class":"bday"})
        if (len(year) > 0):
            bday = year[0].text
            bday = bday.split("-")
            bYear = int(bday[0])

        if (len(year) == 0):
            logging.warning('Unable to find brithday.')
            bYear = None


        actorJSON = {
                    "ActorName": name[0].text,
                    "B_year": bYear,
                    "Movies": MovieArr,
                    }

        return actorJSON
### End of ActorScrap Function ###



# "https://en.wikipedia.org/" + FilmLink[0]

#actorScarp("https://en.wikipedia.org/wiki/Jesse_Eisenberg")

#Source Cite: https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/
#Source Cite: http://stackoverflow.com/questions/4362981/beautifulsoup-how-do-i-extract-all-the-lis-from-a-list-of-uls-that-contains