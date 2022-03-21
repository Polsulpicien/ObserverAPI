from ObserverAPI import Observer
import asyncio

async def main():
    # Start the Client
    # Note: Don't forget to provide your Observer API Key!
    client = await Observer(key="INSERT YOUR OBSERVER API KEY HERE") 
    

    player = await client.daily.get("b876ec32e396476ba1158438d83c67d4")
    print(player.bedwars.wins)


    uuids = ["b876ec32e396476ba1158438d83c67d4"] 


    players = await client.daily.post(uuids)
    for player in players:
        print(player.bedwars.wins)


asyncio.get_event_loop().run_until_complete(main())
