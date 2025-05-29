import json
import pandas as pd
from espn_api.basketball import League


def fetch_all_player(league):
    # Fetch all players (team rosters + free agents)
    all_players = []
    for team in league.teams:
        all_players.extend(team.roster)
    all_players.extend(league.free_agents(size=500))

    # Extract relevant data
    player_data = [
        {
            "name": player.name,
            "position": player.position,
            "team": player.proTeam,
            "total_points": player.total_points
        }
        for player in all_players
    ]

    # Save data to a JSON file
    with open("all_players.json", "w") as file:
        json.dump(player_data, file, indent=4)

    print("All player data has been saved to 'all_players.json'.")


def save_historical_data(league, total_weeks=10):
    historical_data = []
    for week in range(1, total_weeks + 1):
        box_scores = league.box_scores(matchup_period=week)
        for box in box_scores:
            for player in box.home_lineup + box.away_lineup:
                stats = player.points_breakdown or {}
                historical_data.append({
                    "Week": week,
                    "Player": player.name,
                    "Position": player.position,
                    "Team": player.proTeam,
                    "3PM": stats.get('3PM', 0),
                    "REB": stats.get('REB', 0),
                    "AST": stats.get('AST', 0),
                    "STL": stats.get('STL', 0),
                    "BLK": stats.get('BLK', 0),
                    "TO": stats.get('TO', 0),
                    "PTS": stats.get('PTS', 0),
                    "Fantasy_Points": player.points
                })

    historical_df = pd.DataFrame(historical_data)
    historical_df.to_csv('historical_player_data.csv', index=False)
    print("Historical data saved to 'historical_player_data.csv'.")