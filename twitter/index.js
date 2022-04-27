const axios = require('axios')
const fs = require('fs')
require('dotenv').config()

const countryIds = require('./country-ids.json')

const BASE_DIR = './twitter-data'

const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

const formatDateString = (dateString) => {
  return dateString.replace(/T/, ' ').replace(/\..+/, '').replace('Z', '')
}

const createDataFile = async (country, dataArr) => {
  const countryDirectory = `${BASE_DIR}/${country}-twitter-data`
  createDirectory(countryDirectory)
  
  const date = new Date()
  const filename = `${countryDirectory}/${country}-${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}-twitter-data.json`

  fs.writeFile(filename, JSON.stringify(dataArr), err => (err ? console.log(err) : console.log(`Created ${filename}`)))
}

const createDataArray = (country, data) => {
  const dataArr = []
  if (data.length > 0 && data[0].trends.length > 0) {
    for (const trend of data[0].trends) {
      dataArr.push({
        country,
        created_at: formatDateString(data[0].created_at),
        trend: trend.name.replace(new RegExp('\'', 'g'), ''),
        tweet_volume: trend.tweet_volume || 0,
        as_of: formatDateString(data[0].as_of)
      })
    }
  }
  return dataArr
}

const fetchTrendingData = async (id) => {
  try {
    const response = await axios.get(`https://api.twitter.com/1.1/trends/place.json?id=${id}`, {
      headers: {
        'authorization': `Bearer ${process.env.TWITTER_BEARER_TOKEN}`
      }
    })
    return response.data
  } catch (err) {
    console.error(err)
    return undefined
  }
}

const createDirectory = (name) => {
  if (!fs.existsSync(name)){
    fs.mkdirSync(name);
  }
}

const main = async () => {
  // Create directory to store results
  createDirectory(BASE_DIR)

  // Iterate over each country and call the Twitter API to fetch trending data, create the data object, then write to a file
  for (const data of countryIds) {
    console.log(`Fetching data for ${data.country}`)
    const apiData = await fetchTrendingData(data.id)
    const dataObject = createDataArray(data.country, apiData)
    const formattedCountryName = data.country.toLowerCase().replace(' ', '-')
    await createDataFile(formattedCountryName, dataObject)
    await sleep(5000)
  }
}

main();