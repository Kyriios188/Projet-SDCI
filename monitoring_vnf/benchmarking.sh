n_total=100
n=0

while [ "$n" -le "$n_total" ];

do
   OUTPUT=$(curl -s http://10.0.0.21:5001/report | tr \' \")
   health=$(echo "$OUTPUT" | jq .health)
   latency=$(echo "$OUTPUT" | jq .latency)
   echo "$health $latency" | sed 's/\"//g'
   sleep 1
   let n=n+1
done


