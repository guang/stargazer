#     @author:        Guang Yang
#     @mktime:        1/26/2015
#     @description:   Making API calls to GGtracker to get simple and extended match details

for match_id in {5710000..5719999}
do
  curl -o ../data/raw/match_extended/matches_${match_id}_extended.json \
    https://gg2-matchblobs-prod.s3.amazonaws.com/${match_id}
  sleep 1
  curl -o ../data/raw/match_simple/matches_${match_id}_simple.json \
    http://api.ggtracker.com/api/v1/matches/${match_id}.json
  sleep 1
done
