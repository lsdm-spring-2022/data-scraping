# Twitter Data Scraping

## Process

Using the country list created during the Reddit data scraping research, we retrieved the list of WOEIDs for each country using the Twitter [GET trends/available](https://developer.twitter.com/en/docs/twitter-api/v1/trends/locations-with-trending-topics/api-reference/get-trends-available) API. Once we had this list of WOEIDs, we used the [GET trends/place](https://developer.twitter.com/en/docs/twitter-api/v1/trends/trends-for-location/api-reference/get-trends-place) API to retrieve the trending topics and tweet volume for each topic for the past 24 hours.

The code in this repository was run once a day to collect the data for each country. The data was saved to a `twitter/data` directory using the following naming format: `{country}-{year}-{month}-{date}-twitter-data.json`.

## Sample Data

An example of the response from the [GET trends/place](https://developer.twitter.com/en/docs/twitter-api/v1/trends/trends-for-location/api-reference/get-trends-place) API is:
```json
[
  {
    "trends": [
      {
        "name": "#GiftAGamer",
        "url": "http://twitter.com/search?q=%23GiftAGamer",
        "promoted_content": null,
        "query": "%23GiftAGamer",
        "tweet_volume": null
      },
      {
        "name": "#AskCuppyAnything",
        "url": "http://twitter.com/search?q=%23AskCuppyAnything",
        "promoted_content": null,
        "query": "%23AskCuppyAnything",
        "tweet_volume": 14504
      },
      {
        "name": "#givethanks",
        "url": "http://twitter.com/search?q=%23givethanks",
        "promoted_content": null,
        "query": "%23givethanks",
        "tweet_volume": null
      },
      {
        "name": "Carrefour",
        "url": "http://twitter.com/search?q=Carrefour",
        "promoted_content": null,
        "query": "Carrefour",
        "tweet_volume": 438616
      },
      {
        "name": "#StreamLifeGoesOn",
        "url": "http://twitter.com/search?q=%23StreamLifeGoesOn",
        "promoted_content": null,
        "query": "%23StreamLifeGoesOn",
        "tweet_volume": 179026
      },
      {
        "name": "STREAM BE PARTY",
        "url": "http://twitter.com/search?q=%22STREAM+BE+PARTY%22",
        "promoted_content": null,
        "query": "%22STREAM+BE+PARTY%22",
        "tweet_volume": 71404
      },
      {
        "name": "#TransDayOfRemembrance",
        "url": "http://twitter.com/search?q=%23TransDayOfRemembrance",
        "promoted_content": null,
        "query": "%23TransDayOfRemembrance",
        "tweet_volume": 45852
      },
      {
        "name": "Mourão",
        "url": "http://twitter.com/search?q=Mour%C3%A3o",
        "promoted_content": null,
        "query": "Mour%C3%A3o",
        "tweet_volume": 12614
      },
      {
        "name": "Taysom Hill",
        "url": "http://twitter.com/search?q=%22Taysom+Hill%22",
        "promoted_content": null,
        "query": "%22Taysom+Hill%22",
        "tweet_volume": 20311
      },
      {
        "name": "Geraldo",
        "url": "http://twitter.com/search?q=Geraldo",
        "promoted_content": null,
        "query": "Geraldo",
        "tweet_volume": 30166
      }
    ],
    "as_of": "2020-11-20T19:37:52Z",
    "created_at": "2020-11-19T14:15:43Z",
    "locations": [
      {
        "name": "Worldwide",
        "woeid": 1
      }
    ]
  }
]
```

The structure of the formatted data stored in the `twitter-data/` directory is:
```json
[
  {
    "country": "United States",
    "created_at": "2022-04-17 12:07:04", // The date the topic started trending
    "trend": "trend1",
    "tweet_volume": 68559, // The tweet volume from the past 24 hours (from the "as_of" field)
    "as_of": "2022-04-26 17:43:25"
  },
  {
    "country": "United States",
    "created_at": "2022-04-17 12:07:04",
    "trend": "trend2",
    "tweet_volume": 3319041,
    "as_of": "2022-04-26 17:43:25"
  },
  {
    "country": "United States",
    "created_at": "2022-04-17 12:07:04",
    "trend": "trend3",
    "tweet_volume": 140677,
    "as_of": "2022-04-26 17:43:25"
  },
]
```


## Running the Code
1. Install the dependencies
2. Run the code using `npm run start`