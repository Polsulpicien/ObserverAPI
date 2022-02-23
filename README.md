<div align="center">
    <a href="https://discord.gg/xm9QX3Q"><img src="https://media.discordapp.net/attachments/804945677833994240/943163642176761876/JBBQuMj.png" alt="observer logo" height="128" style="border-radius: 50%"></a>
    <h1>ObserverAPI</h1>
</div>
<div align="center">
        <a href="https://discord.gg/xm9QX3Q"><img src="https://img.shields.io/discord/761623845119328257?color=blue&label=Polsu Support Discord&logo=discord&style=for-the-badge" alt="Discord"></a>
        <a href="https://discord.gg/dcDt9j8fXf"><img src="https://img.shields.io/discord/763987695374434306?color=blue&label=Observer Discord&logo=discord&style=for-the-badge" alt="Discord"></a>  
        <br>
        <a href="https://github.com/Polsulpicien/ObserverAPI"><img src="https://img.shields.io/github/stars/Polsulpicien/ObserverAPI?style=for-the-badge" alt="Stars"></a>
        <a href="https://github.com/Polsulpicien/ObserverAPI"><img src="https://img.shields.io/github/v/release/polsulpicien/ObserverAPI?color=red&label=Version&logo=github&style=for-the-badge" alt="Version"></a>
</div>
<p align="center">
    <h3>Observer API Wrapper in Python</h3>
</p>

  - [Introduction](https://github.com/Polsulpicien/ObserverAPI/#introduction)  
  - [Installing](https://github.com/Polsulpicien/ObserverAPI/#installing)  
  - [Usage](https://github.com/Polsulpicien/ObserverAPI/#usage)  
  - [Links](https://github.com/Polsulpicien/ObserverAPI/#links)  
  - [License](https://github.com/Polsulpicien/ObserverAPI/#license) 

\
```
This is not the final version. You can find the final version on the Beta Branch of this repo. 
It will be released when all the docs will be done ;)
```
/

## Introduction  
  
This is the first [Observer API](https://discord.gg/dcDt9j8fXf) Wrapper in Python.  

If you need help please join **[Polsu Development Support Server](https://discord.gg/xm9QX3Q)**.   

## Installing  

Install the `ObserverAPI` using [`pip`](https://pypi.org/project/ObserverAPI/1.0.3/)  
**> Current Version: `1.0.3`**
```
py -m pip install ObserverAPI
```  

*This library was only tested with python 3.10 but I set it to 3.8 since I think everything should work. Please report me any issues! Thank you.*  

## Usage

A Basic Example:
```py
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
```
You can find this example in the [`tests` folder](https://github.com/Polsulpicien/ObserverAPI/tree/main/tests)

## Links

- [Documentation](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md)
- [Official Polsu Server](https://discord.gg/xm9QX3Q)
- [Observer API](https://api.invite.observer/)
- [Official Observer Server](https://discord.gg/dcDt9j8fXf)

## License
This project is under the [MIT License](https://github.com/Polsulpicien/ObserverAPI/blob/main/LICENSE).
