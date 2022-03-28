import calendar
import os
import time
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import requests

MONTHS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
YEARS = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

START_HOUR = 0
START_MINUTE = 0
START_SECOND = 0
START_MICROSECOND = 0

END_HOUR = 23
END_MINUTE = 59
END_SECOND = 59
END_MICROSECOND = 999999

COUNTRIES = [
    'canada',
    'australia',
    'brasil',
    'Philippines',
    'france',
    'india',
    'unitedkingdom',
    'mexico',
    'thenetherlands',
    'HongKong',
    'de',
    'singapore',
    'ireland',
    'turkey',
    'polska',
    'sweden',
    'italy',
    'argentina',
    'china',
    'romania',
    'newzealand',
    'japan',
    'austria',
    'denmark',
    'korea',
    'malaysia',
    'chile',
    'portugal',
    'czech',
    'suomi',
    'belgium',
    'switzerland',
    'hungary',
    'norge',
    'vietnam',
    'colombia',
    'israel',
    'southafrica',
    'croatia',
    'taiwan',
    'egypt',
    'greece',
    'pakistan',
    'spain',
    'indonesia',
    'thailand',
    'vzla',
    'peru',
    'saudiarabia'
]


def create_log_file(log_name):
    log_file = Path(f'reddit/{log_name}/data-scraping-{log_name}.txt')
    log_file.touch(exist_ok=True)


def write_to_log(message, log_dir):
    with open(f'reddit/{log_dir}/data-scraping-{log_dir}.txt', 'a') as log_file:
        log_file.write(f'{message}\n')


def create_dir(dir_name):
    if not os.path.exists(f'reddit/{dir_name}'):
        os.makedirs(f'reddit/{dir_name}')


def get_start_epoch(year, month, day):
    return int((datetime(year, month, day, hour=START_HOUR, minute=START_MINUTE, second=START_SECOND,
                         microsecond=START_MICROSECOND, tzinfo=timezone.utc) - datetime(1970, 1, 1,
                                                                                        tzinfo=timezone.utc)).total_seconds())


def get_end_epoch(year, month, day):
    return int((datetime(
        year, month, day, hour=END_HOUR, minute=END_MINUTE, second=END_SECOND, microsecond=END_MICROSECOND,
        tzinfo=timezone.utc) - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds())


def get_pushshift_data(start, end, country):
    """
    Retrieve 500 submissions for a particular start and end window of time
    :param start: Epoch value
    :param end: Epoch value
    :param country: Country subreddit
    :return:
    """
    uri = f'https://api.pushshift.io/reddit/search/submission?&subreddit={country}&sort_type=score&sort=desc&after={start}&before={end}&size=500'
    try:
        response = requests.get(uri)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'{response.reason}')
    except Exception as e:
        print(e)
        write_to_log(e, 'error')
        return None


def main():
    create_dir('log')
    create_dir('error')
    create_dir('data')
    create_log_file('log')
    create_log_file('error')
    print('Starting data scraping process...')
    write_to_log('Starting data scraping process...', 'log')
    start_time = time.time()
    for country in COUNTRIES:
        for year in YEARS:
            for month in MONTHS:
                df_list = []
                cal = calendar.monthcalendar(year, month)
                for week in cal:
                    for day in week:
                        if day != 0:
                            print(f'Year: {year}, Month: {month}, Day: {day}')
                            write_to_log(f'Year: {year}, Month: {month}, Day: {day}', 'log')
                            start_epoch = get_start_epoch(year, month, day)
                            end_epoch = get_end_epoch(year, month, day)
                            print(f'StartEpoch: {start_epoch}, EndEpoch: {end_epoch}')
                            print('Getting Pushshift data...')
                            write_to_log('Getting Pushshift data...', 'log')
                            data = get_pushshift_data(start_epoch, end_epoch, country)
                            if data is not None:
                                print('Got Pushshift data. Creating dataframe...')
                                write_to_log('Got Pushshift data. Creating dataframe...', 'log')
                                df = pd.json_normalize(data['data'])
                                df_list.append(df)
                                print('Dataframe creation complete. Sleeping for 10 seconds...')
                                write_to_log('Dataframe creation complete. Sleeping for 10 seconds...', 'log')
                                time.sleep(10)
                print(f'Concatenating dataframes for month {month}...')
                write_to_log(f'Concatenating dataframes for month {month}...', 'log')
                month_df = pd.concat(df_list)
                print(f'Writing dataframe to CSV ({country}-{year}-{month}-reddit-data.csv)', 'log')
                month_df.to_csv(f'reddit/data/{country}-{year}-{month}-reddit-data.csv', sep='\t', encoding='utf-8')
    end_time = time.time() - start_time
    print(f'--- Data scraping process complete! Took {end_time} seconds ---')
    write_to_log(f'--- Data scraping process complete! Took {end_time} seconds ---', 'log')


if __name__ == "__main__":
    main()
