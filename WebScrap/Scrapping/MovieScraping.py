import urllib
import urllib.request

from bs4 import BeautifulSoup
import logging


class movieClass:

    def parseBoxOffice(self, BoxOffice):
        BoxOffice = BoxOffice.replace("$", "")
        BoxOffice = BoxOffice.replace(",", "")
        BoxOffice = BoxOffice.partition("[")[0]         # delete [1]
        BoxOffice = BoxOffice.split(" ")                # split numbers and unit
        BoxOfficeNum = BoxOffice[0]                     # get digits in boxoffice

        try:
            grosses = float(BoxOfficeNum)
        except ValueError:
            grosses = None
            return grosses

        if(len(BoxOffice) > 1):
            unit = BoxOffice[1]
            if(unit == 'million'):
                grosses *= 1e6
            if(unit == 'billion'):
                grosses *= 1e9

        return grosses
    # end of parse BoxOffice



### Movie Scraping Function ###
    def movieScrap(self, weburl):

        MOV_LOG = 'movieLogFile.log'
        logging.basicConfig(filename=MOV_LOG)

        #time.sleep(1)
        webPage = urllib.request.urlopen(weburl)
        movieWeb = BeautifulSoup(webPage, "lxml")

        Cast = []
        CastLink = []
        CastValue = []
        BoxOffice = ""

#Finding Information of the Movie
        for tr in movieWeb.findAll('tr'):
            for th in tr.findAll('th'):
                # find Staring Table
                if(th.text == 'Starring') :
                    for actor in tr.findAll('a'):
                        Cast.append(actor.text)
                        string = "https://en.wikipedia.org" + actor.get('href')
                        CastLink.append(string)

                # find Box Office
                if(th.text == 'Box office'):
                    box = tr.findAll('td')
                    BoxOffice = box[0].text

# log check starring is avaliable or not

        maxValue = len(Cast)
        if (maxValue < 1):
            logging.error(weburl + ' was not able to be parsed because Starring section was not found.')
            return None

# set value for actors
        for i in range(1,maxValue+1):
            CastValue.append(maxValue-i)

# parse boxoffice
        grossed = 0
        if(len(BoxOffice) != 0):
            grossed = self.parseBoxOffice(BoxOffice)
            #print(grossed)

        if(grossed == 0 or grossed == None):
            logging.warning(weburl + ' was not able to be found BoxOffice Information.')
            grossed = None

        name = movieWeb.findAll('h1')


        CastArr = []
        for a in range(len(Cast)):
            tempActor = {
                        "aName": Cast[a],
                        "aValue": CastValue[a],
                        "aLink": CastLink[a],
                        }
            CastArr.append(tempActor)

# get year of movie
        bYear = 0

        year = movieWeb.findAll('span', {"class": "bday dtstart published updated"})
        if (len(year) > 0):
            bday = year[0].text
            bday = bday.split("-")
            bYear = int(bday[0])


        if (len(year) == 0):
            logging.warning('Unable to find brithday.')
            bYear = None

        print(bYear)

        movieJSON = {
        "A_MoviesName": name[0].text,
        "B_BoxOffice": grossed,
        "C_Cast": CastArr,
        "D_Year": bYear,

        }


        return movieJSON
### End of MovieScrap Function ###

#movieScrap("https://en.wikipedia.org/wiki/Now_You_See_Me_2")




#<h2><span class="mw-headline" id="Filmography">Filmography</span></h2>
#<li><i><a href="/wiki/Brubaker" title="Brubaker">Brubaker</a></i> (1980)</li>