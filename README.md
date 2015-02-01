Stargazer: Map Analytics in Starcraft II
====================
Project for Data Engineering Fellowship at Insight Data Science '15A
Questions and Comments welcome at gy8 [AT] berkeley [DOT] edu

## Table of Contents





## Background
Starcraft II is a real-time strategy game released by Blizzard Entertainment in 2010.
In addition to having a large user base with **XXX** active players world wide, Starcraft II
has an exciting competitive scene - Just this last year, the finals of one of the top
tournaments, the World Champion Series, were broadcasted live on ESPN (not to mention
the $1.6 million total prize pool).

Gameplay centers around 1v1 matches: where each player builds bases to gather resources
in order to produce armies to eliminate his/her opponent. Players compete on the ladder
system for higher ranks. Many professional gamers (most play for sponsored teams) were
discovered for very high ranking on the ladder.

## Motivation
Map is an integral part of the Starcraft II gaming experience. All ranked ladder games are
played on a different set of maps each season. Many of these ladder maps are used in
international tournaments.

Designing a great map is inherently difficult: on one hand it has to offer
complexity with features that give an advantage to skilled players who really understands
the game dynamics; on the other hand it needs to be balanced across different play styles,
such as:
- races (every player can choose to be either Terran, Protoss, or Zerg, each race with its
  unique units and strategies)
- strategies (some players opt for early rush, some aim to out last their opponent in long, dragged out games)

It is especially difficult to measure how balanced a map is - rounds and rounds of beta testing
simply does not capture the whole picture. Currently, selecting which maps to be kept for the
new season is largely a *qualitative* process, where users vote on the maps that they like.
This naturally led to the question that I attempt to address with this project:
**What does game data reveal about maps?**
