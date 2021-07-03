import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june']

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
        'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    time.sleep(1.5)

    city = input("Would you like to see data for Chicago, New York City, or Washington?\n").lower()
    while city not in CITY_DATA:
        city = input('\nSorry champ, looks like we don\'t have any data for that place. Try again.\nWould you like to see data for Chicago, New York City, or Washington?\n').lower()

    filter = input('\nWould you like to filter by month, day, or not at all? Type "none" for no time filter.\n').lower()
    while filter != 'month' and filter != 'day' and filter != 'none':
        filter = input('\nSadly, we cannot filter for that. Try again.\nWould you like to filter by month, day, or not at all? Type "none" for no time filter.\n').lower()

    if filter == 'none':
        print('\nWe will not filter by month or day!')
        day = 'all'
        month = 'all'

    else:
        print("\nWe will be sure to filter by {}!".format(filter))

        if filter == 'month':
            month = input("What month? January, February, March, April, May or June.\n").lower()
            while month not in months:
                month = input("Your input did not work. Try again. Do you want to see data for January, February, March, April, May or June.\n").lower()
            day = 'all'

        else:
            day = input("What day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n").lower()
            while day not in days:
                day = input("What day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n").lower()
            month = 'all'
    print()
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    time.sleep(3)

    print('The most common month is: ', (months[df['month'].mode().iloc[0] - 1].title())
    month_counts = df['month'].value_counts()
    print('Total counts: ', month_counts.iloc[0])
    time.sleep(1.5)

    print('\nThe most common day of the week is: ', df['day_of_week'].mode().iloc[0])
    time.sleep(1.5)
    print('Total counts: ', df['day_of_week'].value_counts().iloc[0])
    time.sleep(1.5)

    print('\nThe most common start hour is: ', df['hour'].mode()[0])
    time.sleep(1.5)
    print('Total counts: ', df['hour'].value_counts().iloc[0])
    time.sleep(1.5)

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    time.sleep(1.5)

    print("The most commonly used start station: ", df['Start Station'].mode().iloc[0])
    time.sleep(0.5)
    print('Total counts: ', df['Start Station'].value_counts().iloc[0])
    time.sleep(1.5)

    print("\nThe most commonly used end station: ", df['End Station'].mode().iloc[0])
    time.sleep(0.5)
    print('Total counts: ', df['End Station'].value_counts().iloc[0])
    time.sleep(1.5)

    groups = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False)
    print("\nThe most frequent combination of start and end station: {} and {}".format(groups.index[0][0], groups.index[0][1]))
    time.sleep(1.5)

    print('Total combinations: ', groups.iloc[0])
    time.sleep(1)

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    time.sleep(3)

    print('Total travel time (secs): ', round(df['Trip Duration'].sum(), 2))
    time.sleep(0.5)
    print('Total travel time (mins): ', round(df['Trip Duration'].sum() / 60, 2))
    time.sleep(0.5)
    print('Total travel time (hours): ', round(df['Trip Duration'].sum() / 3600, 2))
    time.sleep(1.5)

    print('\nMean travel time (secs): ', round(df['Trip Duration'].mean(), 2))
    time.sleep(0.5)
    print('Mean travel time (mins): ', round(df['Trip Duration'].mean() / 60, 2))
    time.sleep(0.5)
    print('Mean travel time (hours): ', round(df['Trip Duration'].mean() / 3600, 2))
    time.sleep(0.5)

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    time.sleep(3)

    print('User data by types:')
    time.sleep(1.5)
    types = df['User Type'].value_counts().keys().tolist()
    print('{} user counts: {}'.format(types[0], df['User Type'].value_counts().iloc[0]))
    time.sleep(0.5)
    print('{} user counts: {}'.format(types[1], df['User Type'].value_counts().iloc[1]))
    time.sleep(1.5)

    try:
        genders = df['Gender'].value_counts().keys().tolist()
        print('\nUser data by gender: ')
        time.sleep(1.5)
        genders = df['Gender'].value_counts().keys().tolist()
        print('{} counts: {}'.format(genders[0], df['Gender'].value_counts().iloc[0]))
        time.sleep(0.5)
        print('{} counts: {}'.format(genders[1], df['Gender'].value_counts().iloc[1]))
        time.sleep(1.5)
    except:
        print('\nThere is no gender data for this city!')
        time.sleep(1.5)

    try:
        birth_data = df['Birth Year']
        print('\nUser data by birth year:')
        time.sleep(1.5)
        print('Earliest user year of birth: ', int(birth_data.sort_values().iloc[0]))
        time.sleep(0.5)
        print('Most recent user year of birth: ', int(birth_data.sort_values(ascending=False).iloc[0]))
        time.sleep(0.5)
        print('Most common user year of birth: ', int(birth_data.mode().iloc[0]))
    except:
        print('\nThere is no birth data for this city!')
        time.sleep(1.5)
    finally:
        print("\nThis took %s seconds.\n" % (time.time() - start_time))
        print('-'*40)


def raw_data_viewer(df):
    view_data = input('\nWould you like to view 5 lines of raw data? (yes or no)\n').lower()
    while view_data != 'yes' and view_data != 'no':
        view_data = input('\nNot sure what you mean. Try again.\nWould you like to view 5 lines of raw data? (yes or no)\n').lower()

    start_loc = 0
    while view_data == 'yes':
        print()
        print(df.iloc[start_loc : start_loc + 5])
        start_loc += 5
        view_data = input('\nWould you like to view 5 more lines? (yes or no)\n').lower()
        while view_data != 'yes' and view_data != 'no':
            view_data = input('\nNot sure what you mean. Try again.\nWould you like to view 5 more lines? (yes or no)\n').lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data_viewer(df)

        restart = input('\nThat is all! Would you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
