# data-scraping

Data scraping repository

## Reddit

### Data Collection Process

Using an image of the most popular subreddits by country, we created a list of the top 50 most popular subreddits (for a
country) by number of subscribers. Since Reddit has a large pool of uses from the United States, the /r/popular
subreddit was used as a substitute for the United States. The country subscriber information was pulled on 2022-Mar-27.

TODO Insert table here

Using the [Pushshift API](https://pushshift.io/), we are fetching the top 500 posts on Reddit for every day of a year.
Currently, we are collecting data starting at Jan 1 2012 until the Dec 31 2021.

Documentation for the Pushshift API is located at: https://github.com/pushshift/api

All of the posts for a month will be saved in the `reddit/data` directory using the following naming
format: `{country}-{year}-{month}-reddit-data.csv`

### Sample Data

The response from the Pushshift API will be the top 500 posts. An example of a single post is:

```json
{
  "author": "man_in_the_mirra",
  "author_created_utc": 1311194415,
  "author_flair_css_class": null,
  "author_flair_text": null,
  "author_fullname": "t2_5jkrb",
  "created_utc": 1325437430,
  "domain": "i.imgur.com",
  "full_link": "https://www.reddit.com/r/pics/comments/nyo9q/just_a_drop_of_water_in_front_of_a_map/",
  "id": "nyo9q",
  "is_self": false,
  "media_embed": {},
  "num_comments": 643,
  "over_18": false,
  "permalink": "/r/pics/comments/nyo9q/just_a_drop_of_water_in_front_of_a_map/",
  "score": 5704,
  "selftext": "",
  "subreddit": "pics",
  "subreddit_id": "t5_2qh0u",
  "thumbnail": "http://b.thumbs.redditmedia.com/2GFdfsWl7IbG_0xg.jpg",
  "title": "Just A Drop Of Water In Front Of A Map",
  "url": "http://i.imgur.com/MwIvz.jpg"
}
```

### Running the Container

Build the image with the following command
```bash
docker build -t <image name> .
```

Run the container with the following command
```bash
docker run -d -v $(pwd):/app <image name>
```