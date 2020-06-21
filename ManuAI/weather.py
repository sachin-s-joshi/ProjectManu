import requests
import asyncio


async def returnResponse(state):
    url = "https://covid-india-cases.herokuapp.com/states"
    payload = {}
    headers = {}
    response = requests.get(url, headers=headers, data=payload)
    await asyncio.sleep(5)
    response = response.json()
    for dic in response:
        if state in dic['state']:
            return(dic['noOfCases'], dic.get('cured'), dic['deaths'])
    else:
        return('I am afraid that I am not able to find {0}'.format(state))


async def returnForCountries(country):
    url = 'https://2019ncov.asia/api/country_region'
    headers = {}
    payload = {}
    response = requests.get(url, headers=headers, data=payload).json()
    response = response['results']
    for dic in response:
        if country in dic['country_region']:
            return (dic['confirmed'], dic['recovered'], dic['deaths'])
    else:
        return('I am afraid that I am not able to find {0}'.format(country))
