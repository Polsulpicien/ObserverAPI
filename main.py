from ObserverAPI import Observer
import asyncio

async def main():
    client = await Observer() #define the client, provide an api key (when they add it)

    # this is my UUID, Polsulpicien, I know I'm not very good :)
    lookback = await client.lookback.get("7f2996146af142948f9479d06f133874", 100)
    print(lookback.bedwars.level)

    api_stats = await client.stats.get()
    print(api_stats.trackedPlayers)

    leaderboard = await client.leaderboard.get("alltime", "bedwars", "wins", 1, 10)
    print(leaderboard.leaderboard)
    
    second_player_on_leaderboard = leaderboard.get_index(2)
    print(second_player_on_leaderboard.formatted, second_player_on_leaderboard.rank, second_player_on_leaderboard.value)

    ranking = await client.ranking.get("7f2996146af142948f9479d06f133874", "alltime", "bedwars", "wins")
    print(ranking.rank)

    formatted = await client.formatted.get("7f2996146af142948f9479d06f133874")
    print(formatted.formatted)

asyncio.get_event_loop().run_until_complete(main())