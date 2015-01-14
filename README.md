Insight Project
====================
Project for Data Engineering Fellowship at Insight Data Science '15A

## Table of Contents





## Project Roadmap
What each part of the pipeline looks like

### Getting Raw .SC2Replay Data
Qualitative:
- Which sources/websites to use? (how to maximize data volume while avoiding redundancy)
- What is the category by which to query for scraping (player vs tournament)
- How to unzip dumps (for tournament scraping)
- How to actually scrape the data (python beautifulsoup?)

Quantitative:
- How big is the entire available data from each source?
- How long does scraping each player/tournament take and how long total?

### Parsing Raw .SC2Replay Data
Qualitative
- Official python parser library by blizzard
- Which information to parse/extract
- How to parallelize this operation (if needed)
- What does each field in the parsed files mean
