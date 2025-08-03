import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington?\n").strip().lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid input. Please enter Chicago, New York City, or Washington.")


    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Which month? January, February, March, April, May, June or 'all'?\n").strip().lower()
        if month in months:
            break
        else:
            print("Invalid month. Try again.")



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("Which day? Monday, Tuesday, ..., Sunday or 'all'?\n").strip().lower()
        if day in days:
            break
        else:
            print("Invalid day. Try again.")


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
        dataframe - Pandas DataFrame containing city data filtered by month and day
    """

    dataframe = pd.read_csv(CITY_DATA[city])
    dataframe['Start Time'] = pd.to_datetime(dataframe['Start Time'])
    dataframe['month'] = dataframe['Start Time'].dt.month
    dataframe['day_of_week'] = dataframe['Start Time'].dt.day_name()
    dataframe['hour'] = dataframe['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        dataframe = dataframe[dataframe['month'] == month]

    if day != 'all':
        dataframe = dataframe[dataframe['day_of_week'].str.lower() == day]

    return dataframe


def time_stats(dataframe):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most Common Month:', dataframe['month'].mode()[0])


    # TO DO: display the most common day of week
    print('Most Common Day of Week:', dataframe['day_of_week'].mode()[0])


    # TO DO: display the most common start hour
    print('Most Common Start Hour:', dataframe['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(dataframe):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most Common Start Station:',dataframe['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print('Most Common End Station:', dataframe['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    dataframe['Start-End Combo'] = dataframe['Start Station'] + " to " + dataframe['End Station']
    print('Most Frequent Combination:', dataframe['Start-End Combo'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(dataframe):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Travel Time:',dataframe['Trip Duration'].sum())


    # TO DO: display mean travel time
    print('Average Travel Time:', dataframe['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(dataframe):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth
    print('Counts of User Types:')
    print(dataframe['User Type'].value_counts())

    if 'Gender' in dataframe.columns:
        print('\nCounts of Gender:')
        print(dataframe['Gender'].value_counts())
    else:
        print('\nNo gender data available.')

    if 'Birth Year' in dataframe.columns:
        print('\nBirth Year Stats:')
        print('Earliest:', int(dataframe['Birth Year'].min()))
        print('Most Recent:', int(dataframe['Birth Year'].max()))
        print('Most Common:', int(dataframe['Birth Year'].mode()[0]))
    else:
        print('\nNo birth year data available.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(dataframe):
    """Ask the user if they want to see 5 lines of raw data, then show more if requested."""
    i = 0
    while True:
        raw = input("\nWould you like to see 5 rows of raw data? Enter yes or no: ").strip().lower()
        if raw != 'yes':
            break
        print(dataframe.iloc[i:i+5])
        i += 5

def main():
    while True:
        city, month, day = get_filters()
        dataframe = load_data(city, month, day)

        time_stats(dataframe)
        station_stats(dataframe)
        trip_duration_stats(dataframe)
        user_stats(dataframe)
        display_raw_data(dataframe)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
