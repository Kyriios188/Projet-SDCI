curl -X POST -d '{
    "dpid": 1,
    "cookie": 1,
    "cookie_mask": 1,
    "table_id": 0,
    "idle_timeout": 3000,
    "hard_timeout": 3000,
    "priority": 100,
    "flags": 1,
    "match":{
        "eth_type": 2048,
        "ipv4_dst": "10.0.0.2"
    },
    "actions":
        {
            "type":"SET_FIELD",
            "field":"ipv4_dst",
            "value":"10.0.0.30"
        }
    ]
}' http://localhost:8080/stats/flowentry/add

