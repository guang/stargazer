
for match_id in {5720000..5739999}
do
  curl -o matches_${match_id}_extended.json \
    https://gg2-matchblobs-prod.s3.amazonaws.com/${match_id}
  sleep 1
  curl -o matches_${match_id}_simple.json \
    http://api.ggtracker.com/api/v1/matches/${match_id}.json
  sleep 1
done
