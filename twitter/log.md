```bash
# Test Request
curl -X GET -H "Authorization: Bearer AAAAAAAAAAAAAAAAAAAAAHWrbwEAAAAAqwi5bd4ugk0QcZ97zyBrxzSATPI%3D9M0K2QqM99rFCyytgVRfLYV5GE53lfoWj24lDtPnD1oIJLOQ1R" "https://api.twitter.com/2/tweets/20"
```

```bash
# GET trends/available
curl -X get -H "Authorization: Bearer AAAAAAAAAAAAAAAAAAAAAHWrbwEAAAAAqwi5bd4ugk0QcZ97zyBrxzSATPI%3D9M0K2QqM99rFCyytgVRfLYV5GE53lfoWj24lDtPnD1oIJLOQ1R" "https://api.twitter.com/1.1/trends/available.json"
```

```bash
# GET trends/place
curl -X get -H "Authorization: Bearer AAAAAAAAAAAAAAAAAAAAAHWrbwEAAAAAqwi5bd4ugk0QcZ97zyBrxzSATPI%3D9M0K2QqM99rFCyytgVRfLYV5GE53lfoWj24lDtPnD1oIJLOQ1R" "https://api.twitter.com/1.1/trends/place.json?id=23424977"
```