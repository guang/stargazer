1/20/2015 Tuesday
=================
Schema for the Raw Data (simple/extended match details from GGtracker API)

## Schema

### Notes
When tracking on basic stats that can be averaged (apm, wpm, resources unspent), there are
three levels:
- in-match snapshots
- average for the match
- average over player history

### Match-Invariant Data
Here we split the schema into two portions, one that tracks game-invariant information (data
that remain unchanged during a specific game, from the simple match details part of the API):

  **About the Match**

1. `match_id (simple_matches['id'])`

  Integer

1. `replay_id (simple_matches['replays']['id'])`

  Integer

1. `replay_url (simple_matches['replays']['url'])`

  String

1. `release_string (simple_matches['release_string'])`

  String

1. `expansion (simple_matches['expansion'])`

  Integer *What does this mean*

1. `map_name (simple_matches['map']['name'])`

  String

1. `map_id (simple_matches['map']['id'])`

  Integer

1. `map_url (simple_matches['map_url'])`

  String

1. `game_type (simple_matches['game_type'])`

  String

1. `game_category (simple_matches['category'])`

  String

1. `duration_seconds (simple_matches['duration_seconds'])`

  Integer

1. `winning_team (simple_matches['winning_team'])`

  Boolean

1. `ended_at (simple_matches['ended_at'])`

  Datetime

  **About Player 0**

1. `player0_id (simple_matches['entities'][0]['identity']['id'])`

  Integer

1. `player0_bnet_id (simple_matches['entities'][0]['identity']['bnet_id'])`

  Integer

1. `player0_name (simple_matches['entities'][0]['identity']['name'])`

  String

1. `player0_current_league_1v1 (simple_matches['entities'][0]['identity']['current_league_1v1'])`

  - 0: bronze
  - 1: silver
  - 2: gold
  - 3: plat
  - 4: diamond
  - 5: master
  - 6: grandmaster

1. `player0_current_rank_1v1 (simple_matches['entities'][0]['identity']['current_rank_1v1'])`

  Integer

1. `player0_matches_count (simple_matches['entities'][0]['identity']['matches_count'])`

  Integer

1. `player0_season_games (simple_matches['entities'][0]['identity']['season_games'])`

  Integer

1. `player0_career_games (simple_matches['entities'][0]['identity']['career_games'])`

  Integer

1. `player0_profile_url (simple_matches['entities'][0]['identity']['profile_url'])`

  String

1. `player0_apm_minute (simple_matches['entities'][0]['minutes'][minute])`

  Float *How to use the dictionary sad face*

1. `player0_apm_match (simple_matches['entities'][0]['apm'])`

  Float

1. `player0_apm_career (simple_matches['entities'][0]['identity']['stats']['apm']['avg'])`

  Float

1. `player0_wpm_career (simple_matches['entities'][0]['identity']['stats']['wpm']['avg'])`

  Float

1. `player0_most_played_race (simple_matches['entities'][0]['identity']['most_played_race'])`

  - p: Protoss
  - t: Terran
  - z: Zerg
  - r: Random

1. `player0_hours_played (simple_matches['entities'][0]['identity']['hours_played'])`

  Float

1. `player0_win (simple_matches['entities'][0]['win'])`

  Boolean

1. `player0_race (simple_matches['entities'][0]['race'])`

  - P: Protoss
  - T: Terran
  - Z: Zerg
  - R: Random

1. `player0_avg_unspent_resources (simple_matches['entities'][0]['average_unspent_resources'])`

  need to change naming here
*NOTE* cleared ['entities'][0]['identity'], still have alot that need parsed, need to change
naming style to get all 3 layers for basic stats being tracked.


  **About Player 1**

1. `player1_id (simple_matches['entities'][1]['identity']['id'])`
1. `player1_bnet_id (simple_matches['entities'][1]['identity']['bnet_id'])`
1. `player1_name (simple_matches['entities'][1]['identity']['name'])`
1. `player1_current_league_1v1 (simple_matches['entities'][1]['identity']['current_league_1v1'])`
1. `player1_current_rank_1v1 (simple_matches['entities'][1]['identity']['current_rank_1v1'])`
1. `player1_matches_count (simple_matches['entities'][1]['identity']['matches_count'])`
1. `player1_season_games (simple_matches['entities'][1]['identity']['season_games'])`
1. `player1_career_games (simple_matches['entities'][1]['identity']['career_games'])`
1. `player1_profile_url (simple_matches['entities'][1]['identity']['profile_url'])`
1. `player1_apm_minute (simple_matches['entities'][1]['minutes'][minute])`
1. `player1_apm_match (simple_matches['entities'][1]['apm'])`
1. `player1_apm_career (simple_matches['entities'][1]['identity']['stats']['apm']['avg'])`
1. `player1_wpm_avg (simple_matches['entities'][1]['identity']['stats']['wpm']['avg'])`
1. `player1_most_played_race (simple_matches['entities'][1]['identity']['most_played_race'])`
1. `player1_hours_played (simple_matches['entities'][1]['identity']['hours_played'])`
1. `player1_win (simple_matches['entities'][1]['win'])`
1. `player1_race (simple_matches['entities'][1]['race'])`

  **Match-Specific Data**

  **About Player 0**

  **Snapshot Every 10s**

1. `player0_vespene_collection_rate (extended_matches['VespeneCollectionRate'][player0_id])`

  Integer

1. `player0_vespene_current (extended_matches['VespeneCurrent'][player0_id])`

  Integer

1. `player0_minerals_collection_rate (extended_matches['MineralsCollectionRate'][player0_id])`

  Integer

1. `player0_minerals_current (extended_matches['MineralsCurrent'][player0_id])`

  Integer

1. `player0_supply_current (extended_matches['SupplyUsage'][player0_id][first column])`

  Integer

1. `player0_supply_max (extended_matches['SupplyUsage'][player0_id][second column])`

  Integer

1. `player0_workers_active_count (extended_matches['WorkersActiveCount'][player0_id])`

  Integer

1. `player0_lost (extended_matches['Lost'][player0_id])`

  Integer

  **By Frame**

1. `player0_upgrades (extended_matches['upgrades'][player0_id])`

  String

1. `player0_scouting (extended_matches['scouting'][player0_id])`

  Boolean

1. `player0_num_bases (extended_matches['num_bases'][0])`

  *Need to look up how this is coded up*

1. `player0_armies_by_frame (extended_matches['armies_by_frame'][player0_id])`

  String (name of the unit being made)

1. `player0_aggressions (extended_matches['aggressions'][player0_id])`

  *Need to look up how this is coded up*

  **About Player 1**

  **Snapshot Every 10s**

1. `player1_vespene_collection_rate (extended_matches['VespeneCollectionRate'][player1_id])`
1. `player1_vespene_current (extended_matches['VespeneCurrent'][player1_id])`
1. `player1_minerals_collection_rate (extended_matches['MineralsCollectionRate'][player1_id])`
1. `player1_minerals_current (extended_matches['MineralsCurrent'][player1_id])`
1. `player1_supply_current (extended_matches['SupplyUsage'][player1_id][first column])`
1. `player1_supply_max (extended_matches['SupplyUsage'][player1_id][second column])`
1. `player1_workers_active_count (extended_matches['WorkersActiveCount'][player1_id])`
1. `player1_lost (extended_matches['Lost'][player1_id])`

  **By Frame**

1. `player1_upgrades (extended_matches['upgrades'][player1_id])`
1. `player1_scouting (extended_matches['scouting'][player1_id])`
1. `player1_num_bases (extended_matches['num_bases'][1])`
1. `player1_armies_by_frame (extended_matches['armies_by_frame'][player1_id])`
1. `player1_aggressions (extended_matches['aggressions'][player1_id])`
