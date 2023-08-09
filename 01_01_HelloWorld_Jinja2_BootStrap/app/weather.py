import asyncio

import aiohttp

import pynws

import pgeocode

nomi = pgeocode.Nominatim('us')
mydata =nomi.query_postal_code("06437")

print(mydata.latitude)



#CT =(41.3083, -72.9279)
CT =(mydata.latitude, mydata.longitude)
USERID = "test@address.yyy"


async def example():
    async with aiohttp.ClientSession() as session:
        nws = pynws.SimpleNWS(*CT, USERID, session)
        await nws.set_station()
        await nws.update_observation()
        await nws.update_forecast()
        await nws.update_alerts_forecast_zone()
        print(nws.observation)
        print(nws.forecast[0])
        print(nws.alerts_forecast_zone)


loop = asyncio.get_event_loop()
loop.run_until_complete(example())
