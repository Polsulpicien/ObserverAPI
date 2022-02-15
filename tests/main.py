from ObserverAPI import Observer
import asyncio

async def main():
    client = await Observer() #define the client

    # Get the stats of Technoblade (UUID: b876ec32e396476ba1158438d83c67d4) 100 days ago
    lookback = await client.lookback.get("b876ec32e396476ba1158438d83c67d4", 100)
    print(lookback.bedwars.level)
    
    # Observer API Stats
    api_stats = await client.stats.get()
    print(api_stats.trackedPlayers)
    
    # Get the Top 10 players, All-Time Bedwars Wins Leaderboard 
    leaderboard = await client.leaderboard.get("alltime", "bedwars", "wins", 1, 10)
    print(leaderboard.leaderboard)
    
    # Get the second player on the leaderboard
    second_player_on_leaderboard = leaderboard.get_index(2)
    print(second_player_on_leaderboard.formatted, second_player_on_leaderboard.rank, second_player_on_leaderboard.value)

    # Get Technoblade (UUID: b876ec32e396476ba1158438d83c67d4) leaderboard rank, in this case in the All-Time Bedwars Wins Leaderboard
    ranking = await client.ranking.get("b876ec32e396476ba1158438d83c67d4", "alltime", "bedwars", "wins")
    print(ranking.rank)
    
    # Get the formatted name of a Player, in this case, Technoblade (UUID: b876ec32e396476ba1158438d83c67d4) -> §d[PIG§b+++§d] Technoblade
    formatted = await client.formatted.get("b876ec32e396476ba1158438d83c67d4")
    print(formatted.formatted)

asyncio.get_event_loop().run_until_complete(main()) # launch the main function
