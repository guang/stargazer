#     @author:        Guang Yang
#     @mktime:        1/26/2015
#     @description:   Making API calls to GGtracker to get simple and extended match details

get_json_simple ( ) {
  curl -o ../../data/raw/match_simple/matches_${1}_simple.json \
    http://api.ggtracker.com/api/v1/matches/${1}.json
}
my_ip=$(curl ident.me)


if [ "$my_ip" = "54.67.92.5" ]; then
  # master 
  for match_id in {1..5680000..100}
  do
    get_json_simple $match_id
    sleep 1
  done
elif [ "$my_ip" = "54.67.61.99" ]; then
  # brant
  for match_id in {2..5680000..100}
  do
    get_json_simple $match_id
    sleep 1
  done
elif [ "$my_ip" = "54.67.63.16" ]; then
  # cj
  for match_id in {3..5680000..100}
  do
    get_json_simple $match_id
    sleep 1
  done
elif [ "$my_ip" = "54.183.89.126" ]; then
  # ed
  for match_id in {4..5680000..100}
  do
    get_json_simple $match_id
    sleep 1
  done
else
  echo "Invalid public IP :(("
fi
