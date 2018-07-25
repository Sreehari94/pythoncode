import requests
#from lxml import objectify

def getXML():

    toDate = "2017-03-05"
    fromDate = "2017-12-12"
    dateType = "gasday"

    url="http://marketinformation.natgrid.co.uk/MIPIws-public/public/publicwebservice.asmx"
    headers = {'content-type': 'application/soap+xml; charset=utf-8'}

    body ="""<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
        <soap12:Body>
            <GetPublicationDataWM xmlns="http://www.NationalGrid.com/MIPI/">
                <reqObject>
                    <LatestFlag>Y</LatestFlag>
                    <ApplicableForFlag>Y</ApplicableForFlag>
                    <ToDate>%s</ToDate>
                    <FromDate>%s</FromDate>
                    <DateType>%s</DateType>
                    <PublicationObjectNameList>
                        <string>LNG Stock Level</string>
                    </PublicationObjectNameList>
                </reqObject>
            </GetPublicationDataWM>
        </soap12:Body>
    </soap12:Envelope>""" % (toDate, fromDate,dateType)


    response = requests.post(url,data=body,headers=headers)

    return response.content

#root = objectify.fromstring(getXML())
res= getXML()

from bs4 import BeautifulSoup
soup = BeautifulSoup(res, 'html.parser')

searchTerms= ['PublicationObjectName','ApplicableAt','ApplicableFor','Value']
# LNG Stock Level,2016-03-13T15:00:07Z, 2016-03-12T00:00:00Z, 7050.42286, ...

for st in searchTerms:
    print(st+'\t')
    print(soup.find(st.lower()).contents[0])