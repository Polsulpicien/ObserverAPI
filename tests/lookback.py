from ObserverAPI import Observer
import asyncio

async def main():
    client = await Observer() #define the client

    # Get the stats of Technoblade (UUID: b876ec32e396476ba1158438d83c67d4) 100 days ago
    lookback = await client.lookback.get("b876ec32e396476ba1158438d83c67d4", 100)
    print(lookback.wins)
    print(lookback.karma)
    
    print(lookback.bedwars.level)
    print(lookback.bedwars.four_v_four.wins)
    
    print(lookback.turbokart.wins)
    print(lookback.turbokart.trophies.gold)


asyncio.get_event_loop().run_until_complete(main()) # launch the main function
