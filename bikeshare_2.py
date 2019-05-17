import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    # get user input for city (chicago, new york, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter the city:.\n 1.Chicago , 2.New York , 3.Washington\n ").lower()
        if city in CITY_DATA:
            break
        else:
            print('\n'*10+'_'*20+'\n Wrong Input Please Try Again.')

    # get user input for month (all, january, february, ... , june)
    months=['january','february','march','april','may','june','july','august','september','october','november','december']
    while True:
        month = input("Type the month:.\n1.January , 2.February , 3.March , 4.April\n5.May , 6.June , 7.July, 8.August\n9.September , 10.October, 11.November, 12.December,\n\t\tAll ").lower()

        if month in months or month =='all':
            break
        else:
            print('\n'*10+'_'*20+'\n Wrong Input Please Try Again.')



    # get user input for day of week (all, monday, tuesday, ... sunday)
    days=['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
    while True:
            day = input("Type the day:.\n1.Saturday , 2.Sunday , 3.Monday , 4.Tuesday , 5.Wednesday , 6.Thursday , 7.Friday , All):.\n").lower()
            if day in days or day == 'all':
                break

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
    # read city csv file.
    df=pd.read_csv(CITY_DATA[city])

    # convert to pd date so we can extract all col we need
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['month'] = df['Start Time'].dt.month

    # convert date from string to numrical value and make it in col.
    if month !='all':
        months={'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,'july':7,'august':8,'september':9,'october':10,'november':11,'december':12}
        df[df['month'] == months[month]]

    # convert day from string to numrical date.
    if day !='all':
        df= df[df['day_of_week'] == day.title()]

    #print 5 col at a time
    i = 0
    while i < df.size:
        print(df.loc[i])
        i += 1
        if i % 5 == 0:
            ino = input("Enter no to exit or press Enter to continue").lower()
            if ino == 'no':
                break
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months=['january','february','march','april','may','june','july','august','september','october','november','december']
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # display the most common month
    print('Most common month = {}'.format(months[df["Start Time"].dt.month.mode()[0] - 1]))

    # display the most common day of week
    print('Most common day of week = {}'.format(df["Start Time"].dt.weekday_name.mode()[0]))

    # display the most common start hour
    print('Most common start hour = {}'.format(df["Start Time"].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most commonly start station = {}'.format(df["Start Station"].mode()[0]))

    # display most commonly used end station
    print('commonly_end_station = {}'.format(df["End Station"].mode()[0]))

    # display most frequent combination of start station and end station trip
    df["Station Combination"] = df["Start Station"] + " - " + df["End Station"]
    print('Most frequent combination station = {}'.format(df["Station Combination"].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("total travel time = {}".format(total_travel_time))

    # display mean travel time
    mean_travel_time = df["Trip Duration"].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of user type = '.format(df["User Type"].value_counts()))

    # Display counts of gender
    if ("Gender" in df.columns):
        print('Count of gender = {}'.format(df["Gender"].value_counts()))
    else:
        print("\n There is no gender in the file")

    # Display earliest, most recent, and most common year of birth
    if ("Birth Year" in df.columns):
        print('earliest birth year = {}'.format(df["Birth Year"].min()))
        print('Most recent birth year = {}'.format(df["Birth Year"].max()))
        print('common birth year = {}'.format(df["Birth Year"].mode()[0]))
    else:
        print("\n There is no Birth Year")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
