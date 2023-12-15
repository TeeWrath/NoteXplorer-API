import requests
import json
from datetime import datetime

class Devfolio:

    '''
    This class is used to fetch data from devfolio.co
    methods: findall()
    '''
    def __init__(self) -> None:

        self.link=  'https://api.devfolio.co/api/search/hackathons'
        self.headers={
            'authority':'api.devfolio.co',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Origin':'https://devfolio.co',
            'Referer':'https://devfolio.co/'
        }

        self.value:int=0
        
    def _getdatetime_(self,startdate:str,enddate:str) -> str:
        '''converts from str to required format'''
        
        datetime_obj = datetime.strptime(startdate, "%Y-%m-%dT%H:%M:%S%z")
        enddate_obj = datetime.strptime(enddate, "%Y-%m-%dT%H:%M:%S%z")

        time = datetime_obj.time()
        year = datetime_obj.year
        month = datetime_obj.month
        day = datetime_obj.day
        
        return f'{year} {month} {day} to {enddate_obj.year} {enddate_obj.month} {enddate_obj.day}' 

    def _getnumhackathons_(self) -> None:
        '''
        Updates the number of hackathons available in the open section
        '''
        payload={"type":"application_open","from":self.value,"size":30}
        r=requests.post(self.link,headers=self.headers,data=payload)

        if(r.status_code!=200):
            raise Exception("Error in fetching data")
        
        self.value=r.json()['hits']['total']['value']
        if(self.value==0):
            raise Warning("No hackathons available in open section of devfolio")

    def _formatdata_(self,json_data:json,writefile:bool) -> list[dict]:
        '''
        Returns a dictionary with the required data
        writefile: if True then writes the data to data.json
        '''
        hackathons:list=[]#store all the hackathons 
        if(writefile):
            with open('data.json','r',encoding='utf-8') as f:
                try:
                    hackathons:list=json.load(f)
                except json.decoder.JSONDecodeError :
                    pass
                
        for data in json_data['hits']['hits']:
            data=data['_source']

            location=data['location']
            
            if(location is None):#if location is null then it is an online event
                location='Online event'
                mode='Digital only'
            else:
                mode='In-person'

            jsonbuilder={
                "name":data['name'],
                "link":f"https://{data['slug']}.devfolio.co",
                "image":data['cover_img'],
                "date":self._getdatetime_(data['starts_at'],data['ends_at']),
                "location":location,
                "mode":mode
            }
            hackathons.append(jsonbuilder)

        if writefile:
            with open('data.json','w',encoding='utf-8') as f:
                f.write(json.dumps(hackathons,indent=4))

        return hackathons
        
    def findall(self,writefile:bool=True) -> list[dict]:
        '''
        Returns a list of all the hackathons, if writefile is True then writes the data to data.json
        and returns the list of hackathons existing in the file along with all of the hackathons in the
        open section appended to it. If  writefile is False then returns the list of hackathons
        in the open section only.
        '''
        self._getnumhackathons_()

        payload={"type":"application_open","from":0,"size":self.value}
        response=requests.post(self.link,headers=self.headers,data=payload)
        json_data=response.json()

        hackathons=self._formatdata_(json_data,writefile)
        return hackathons

if __name__ == "__main__":
    scrapper = Devfolio()
    scrapper.findall()