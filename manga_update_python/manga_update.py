import requests
from bs4 import BeautifulSoup

class MangaUpdate:
    base_url = 'http://fanfox.net/manga/'


    def __customURL(self):
        self.manga = input("What manga do you want to check? ").lower()
        self.manga = self.manga.replace(" ","_")
        #self.url = MangaUpdate.base_url + self.manga
        return MangaUpdate.base_url + self.manga

    def __init__(self):
        self.url = self.__customURL()
        self.updated = False
        #self.rate_limit = 1

    def __getUpdate(self): #private method
        try:
            response = requests.get(self.url)
            parser = BeautifulSoup(response.text, 'html.parser')
            class_container = parser.find_all('span', class_ = "detail-main-list-title-right")
            updateDate = class_container[0].text
            #print(updateDate)
            return updateDate
        except Exception as ex:
                    print(str(ex))

    def checkForUpdate(self):
        update = self.__getUpdate().lower()
        if "minute" in update:
            self.updated = True
        elif "hour" in update:
            self.updated = True
        elif "today" in update:
            self.updated = True
        else:
            self.updated = False
        #print(self.updated)
        return self.updated


obj = MangaUpdate()
print(obj.checkForUpdate())