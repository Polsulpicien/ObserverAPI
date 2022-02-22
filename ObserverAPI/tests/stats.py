from ObserverAPI import Observer
import asyncio

async def main():
    client = await Observer() #define the client, provide an api key (when they add it)
    
    api_stats = await client.stats.get()
    print(api_stats.trackedPlayers)
    print(api_stats.commandsExecuted)
    print(api_stats.verifiedUsers)

asyncio.get_event_loop().run_until_complete(main())
