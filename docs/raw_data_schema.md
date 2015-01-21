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

#### About the Match
- match_id (simple_matches['id'])
- release_string (simple_matches['release_string'])
- expansion
- map_name (simple_matches['map']['name'])
- map_id (simple_matches['map']['id'])
- entities 

#### About Player 0
- player0_id (simple_matches['entities'][0]['identity']['id'])

  Integer

- player0_bnet_id (simple_matches['entities'][0]['identity']['bnet_id'])

  Integer

- player0_name (simple_matches['entities'][0]['identity']['name'])

  String

- player0_current_league_1v1 (simple_matches['entities'][0]['identity']['current_league_1v1'])

  - 0: bronze
  - 1: silver
  - 2: gold
  - 3: plat
  - 4: diamond
  - 5: master
  - 6: grandmaster

- player0_current_rank_1v1 (simple_matches['entities'][0]['identity']['current_rank_1v1'])

  Integer

- player0_matches_count (simple_matches['entities'][0]['identity']['matches_count'])

  Integer

- player0_season_games (simple_matches['entities'][0]['identity']['season_games'])

  Integer

- player0_career_games (simple_matches['entities'][0]['identity']['career_games'])

  Integer

- player0_profile_url (simple_matches['entities'][0]['identity']['profile_url'])

  String

- player0_apm (simple_matches['entities'][0]['apm'])

  Float

- player0_apm_avg (simple_matches['entities'][0]['identity']['stats']['apm']['avg'])

  Float

- player0_wpm_avg (simple_matches['entities'][0]['identity']['stats']['wpm']['avg'])

  Float

- player0_most_played_race (simple_matches['entities'][0]['identity']['most_played_race'])

  - p: Protoss
  - t: Terran
  - z: Zerg
  - r: Random

- player0_hours_played (simple_matches['entities'][0]['identity']['hours_played'])

  Float

- player0_win (simple_matches['entities'][0]['win'])

  Boolean

- player0_race (simple_matches['entities'][0]['race'])

  - P: Protoss
  - T: Terran
  - Z: Zerg
  - R: Random

- player0_avg_unspent_resources (simple_matches['entities'][0]['average_unspent_resources'])

  need to change naming here
*NOTE* cleared ['entities'][0]['identity'], still have alot that need parsed, need to change
naming style to get all 3 layers for basic stats being tracked.


#### About Player 1

- player1_id (simple_matches['entities'][1]['identity']['id'])
- player1_bnet_id (simple_matches['entities'][1]['identity']['bnet_id'])
- player1_name (simple_matches['entities'][1]['identity']['name'])
- player1_current_league_1v1 (simple_matches['entities'][1]['identity']['current_league_1v1'])
- player1_current_rank_1v1 (simple_matches['entities'][1]['identity']['current_rank_1v1'])
- player1_matches_count (simple_matches['entities'][1]['identity']['matches_count'])
- player1_season_games (simple_matches['entities'][1]['identity']['season_games'])
- player1_career_games (simple_matches['entities'][1]['identity']['career_games'])
- player1_profile_url (simple_matches['entities'][1]['identity']['profile_url'])
- player1_apm (simple_matches['entities'][1]['apm'])
- player1_apm_avg (simple_matches['entities'][1]['identity']['stats']['apm']['avg'])
- player1_wpm_avg (simple_matches['entities'][1]['identity']['stats']['wpm']['avg'])
- player1_most_played_race (simple_matches['entities'][1]['identity']['most_played_race'])
- player1_hours_played (simple_matches['entities'][1]['identity']['hours_played'])
- player1_win (simple_matches['entities'][1]['win'])
- player1_race (simple_matches['entities'][1]['race'])

### Match-Specific Data

#### About Player 0
##### Snapshot Every 10s
- player0_vespene_collection_rate (extended_matches['VespeneCollectionRate'][player0_id])
- player0_vespene_current (extended_matches['VespeneCurrent'][player0_id])
- player0_minerals_collection_rate (extended_matches['MineralsCollectionRate'][player0_id])
- player0_minerals_current (extended_matches['MineralsCurrent'][player0_id])
- player0_supply_usage (extended_matches['SupplyUsage'][player0_id])
- player0_workers_active_count (extended_matches['WorkersActiveCount'][player0_id])
- player0_lost (extended_matches['Lost'][player0_id])
##### By Frame
- player0_upgrades (extended_matches['upgrades'][player0_id])
- player0_scouting (extended_matches['scouting'][player0_id])
- player0_num_bases (extended_matches['num_bases'][0])
- player0_armies_by_frame (extended_matches['armies_by_frame'][player0_id])
- player0_aggressions (extended_matches['aggressions'][player0_id])

