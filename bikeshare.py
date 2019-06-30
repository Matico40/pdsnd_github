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
    print('Hellow! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city_valid = False
    while city_valid == False:
      city_valid = True

      city = input('\nWhere would you like to see data for: Chicago, New York City, or Washington?\n').lower()

      if city.lower() == 'chicago':
        print('\nLet\'s see data for Chicago.')
    
      elif city.lower() == 'washington':
        print('\nLet\'s see data for Washington.')
    
      elif city.lower() == 'new york city':
        print('\nLet\'s see data for New York City.')
    
      else:
        print('\nYou provided an invalid input. Please try again\n')
        city_valid = False

    # TO DO: get user input for month (all, january, february, ... , june)

    time_valid = False
    while time_valid == False:
      time_valid = True
    
      time_filter = input("\nWhat would you like to filter data for: Month, Day, or None?\n")

      if time_filter.lower() == 'month':
        month = input("\nPlease select a month: January, February, March, April, May, or June.\n").lower()
        day = "all"
        while (month=='january' or month=='february' or month=='march' or month=='april' or month=='may' or month=='june') == False:
          print("\nInvalid month. Please try again.\n")
          month = input("\nPlease select a month: January, February, March, April, May, or June.\n").lower()

      elif time_filter.lower() == 'day':
        day = input("\nPlease select a day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.\n").lower()
        month = "all"
        while (day=='monday' or day=='tuesday' or day=='wednesday' or day=='thursday' or day=='friday' or day=='saturday' or day=='sunday') == False:
          print('\nInvalid day. Please try again\n')
          day = input("\nPlease select a day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.\n").lower()
  
      elif (time_filter.lower() == 'none'):
        month = 'all'
        day = 'all'
        print("\nData will not be filtered.\n")

      else:
        print("\nYou provided an invalid input. Please try again\n")
        time_valid = False

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

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
    return df

def time_stats(df, month, day):
  """Displays statistics on the most frequent times of travel."""

  print('\nCalculating The Most Frequent Times of Travel...\n')
  start_time = time.time()

  df['Start Time'] = pd.to_datetime(df['Start Time'])
  df['month'] = df['Start Time'].dt.month
  df['day'] = df['Start Time'].dt.weekday
  df['hour'] = df['Start Time'].dt.hour

  months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
  month_index = months.index(month) + 1
  month_data = df[df['month'] == month_index]

  days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
  day_index = days.index(day)#+1
  day_data = df[df['day'] == day_index]

  if month != 'all':
    print('Filtering by month, {}.'.format(month.title()))
    popular_day = month_data['day'].mode()[0]
    print('\nMost popular day of the week:\n', popular_day)
    popular_hour = month_data['hour'].mode()[0]
    print('\nMost popular start hour:\n', popular_hour)

  if day != 'all':
    print('Filtering by day of the week, {}.'.format(day.title()))
    popular_day = day_data['hour'].mode()[0]
    print('\nMost popular start hour:', popular_day)

  if month == 'all' and day == 'all':
    print('Applying no filters')
    popular_month = df['month'].mode()[0]
    print('\nMost popular month:', popular_month)
    popular_day = df['day'].mode()[0]
    print('\nMost popular day of the week:', popular_day)

    # TO DO: display the most common month
    # TO DO: display the most common day of week
    # TO DO: display the most common start hour

  print("\nThis took %s seconds." % (time.time() - start_time))
  print('-'*40)


def station_stats(df,month, day):
  """Displays statistics on the most popular stations and trip."""

  print('\nCalculating The Most Popular Stations and Trip...\n')
  start_time = time.time()

  months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
  month_index = months.index(month) + 1
  month_data = df[df['month'] == month_index]

  days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
  day_index = days.index(day)#+1
  day_data = df[df['day'] == day_index]

  if month != 'all':
    print('Filtering by month, {}.'.format(month.title()))
    popular_start_station = month_data['Start Station'].mode()[0]
    print('\nMost popular start station:\n', popular_start_station)
    popular_end_station = month_data['End Station'].mode()[0]
    print('\nMost popular end station:\n', popular_end_station)
    popular_trip = (month_data['Start Station'] + 'to' + month_data['End Station']).mode()[0]
    print('\nMost populart trip:\n', popular_trip)

  if day != 'all':
    print('Filtering by day of the week, {}.'.format(day.title()))
    popular_start_station = day_data['Start Station'].mode()[0]
    print('\nMost popular start station:\n', popular_start_station)
    popular_end_station = day_data['End Station'].mode()[0]
    print('\nMost popular end station:\n', popular_end_station)
    popular_trip = (day_data['Start Station'] + 'to' + day_data['End Station']). mode()[0]
    print('\nMost populart trip:\n', popular_trip)

  if month == 'all' and day == 'all':
    print('Applying no filters')
    popular_start_station = df['Start Station'].mode()[0]
    print('\nMost popular start station:\n', popular_start_station)
    popular_end_station = df['End Station'].mode()[0]
    print('\nMost popular end station:\n', popular_end_station)
    popular_trip = (df['Start Station'] + 'to' + df['End Station']).mode()[0]
    print('\nMost popular trip:\n', popular_trip)

    # TO DO: display most commonly used start station
    # TO DO: display most commonly used end station
    # TO DO: display most frequent combination of start station and end station trip

  print("\nThis took %s seconds." % (time.time() - start_time))
  print('-'*40)


def trip_duration_stats(df, month, day):
  """Displays statistics on the total and average trip duration."""

  print('\nCalculating Trip Duration...\n')
  start_time = time.time()

  months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
  month_index = months.index(month) + 1
  month_data = df[df['month'] == month_index]

  days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
  day_index = days.index(day) #+ 1
  day_data = df[df['day'] == day_index]

  if month != 'all':
    print('Filtering by month, {}.'.format(month.title()))
    total_travel = month_data['Trip Duration'].count()
    print('\nTotal trip duration:\n', total_travel)
    mean_travel = month_data['Trip Duration'].mean()
    print('\nThe mean travel time:\n', mean_travel)

  if day != 'all':
    print('Filtering by day of the week, {}.'.format(day.title()))
    total_travel = day_data['Trip Duration'].count()
    print('\nTotal trip duration:\n', total_travel)
    mean_travel = day_data['Trip Duration'].mean()
    print('\nThe mean travel time:\n', mean_travel)

  if month == 'all' and day == 'all':
    print('Applying no filters')
    total_travel = df['Trip Duration'].count()
    print('\nTotal trip duration:\n', total_travel)
    mean_travel = df['Trip Duration'].mean()
    print('\nThe mean travel time:\n', mean_travel)

    # TO DO: display total travel time
    # TO DO: display mean travel time

  print("\nThis took %s seconds." % (time.time() - start_time))
  print('-'*40)


def user_stats(df, month, city, day):
  """Displays statistics on bikeshare users."""

  print('\nCalculating User Stats...\n')
  start_time = time.time()

  months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
  month_index = months.index(month) + 1
  month_data = df[df['month'] == month_index]

  days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
  day_index = days.index(day) #+ 1
  day_data = df[df['day'] == day_index]

  if city == 'washington':
    if month != 'all':
      print('Filtering by month, {}.'.format(month.title()))
      user_types = month_data['User Type'].value_counts()
      print('\nNumber of user types:\n', user_types)

    if day != 'all':
      print('Filtering by day of the week, {}.'.format(day.title()))
      user_types = day_data['User Type'].value_counts()
      print('\nNumber of user types:\n', user_types)

    if month == 'all' and day == 'all':
      print('Applying no filters')
      user_types = df['User Type'].value_counts()
      print('\nNumber of user types:\n', user_types)

  if city != 'washington':
      if month != 'all':
        print('Filtering by month, {}.'.format(month.title()))
        user_types = month_data['User Type'].value_counts()
        print('\nNumber of user types:\n', user_types)
        genders = month_data['Gender'].value_counts()
        print('\nGender counts:\n', genders)
        min_birthyear = month_data['Birth Year'].min()
        print('\nThe earliest birth year:\n', min_birthyear)
        max_birthyear = month_data['Birth Year'].max()
        print('\nThe most recent birth year:\n', max_birthyear)
        common_birthyear = month_data['Birth Year'].mode()[0]
        print('\nThe most common birth year:\n', common_birthyear)
      
      if day != 'all':
        print('Filtering by day of the week, {}.'.format(day.title()))
        user_types = day_data['User Type'].value_counts()
        print('\nNumber of user types:\n', user_types)
        genders = day_data['Gender'].value_counts()
        print('\nGender counts:\n', genders)
        min_birthyear = day_data['Birth Year'].min()
        print('\nThe earliest birth year:\n', min_birthyear)
        max_birthyear = day_data['Birth Year'].max()
        print('\nThe most recent birth year:\n', max_birthyear)
        common_birthyear = day_data['Birth Year'].mode()[0]
        print('\nThe most common birth year:\n', common_birthyear)
      
      if month == 'all' and day == 'all':
        print('Applying no filters')
        user_types = df['User Type'].value_counts()
        print('\nNumber of user types:\n', user_types)
        genders = df['Gender'].value_counts()
        print('\nGender counts:\n', genders)
        min_birthyear = df['Birth Year'].min()
        print('\nThe earliest birth year:\n', min_birthyear)
        max_birthyear = df['Birth Year'].max()
        print('\nThe most recent birth year:\n', max_birthyear)
        common_birthyear = df['Birth Year'].mode()[0]
        print('\nThe most common birth year:\n', common_birthyear)

    # TO DO: Display counts of user types
    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth

  print("\nThis took %s seconds." % (time.time() - start_time))
  print('-'*40)

def get_raw(dtf):
  
  raw_valid = False
  raw_yn = input('Would you like to see raw data first?\n').lower()
  n = 0

  while raw_valid == False:
    raw_valid = True  
    
    if raw_yn.lower() == 'yes':
      print('\nLet\'s see the raw data.')
      print(dtf[n:n+5])
      raw_yn = input('Would you like to see more raw data?\n').lower()
      raw_valid = False
      n = n + 5
  
    elif raw_yn.lower() == 'no':
      return()
    
    else:
      raw_yn = input('\nYou provided an invalid input.\nPlease try again: ').lower()
      raw_valid = False

def main():
  while True:
    
    city, month, day = get_filters()
    # city = 'chicago'
    # month = 'all'
    # day = 'monday'
    # day = 'tuesday'
    # day = 'wednesday'
    # day = 'thursday'
    # day = 'friday'
    # day = 'saturday'
    # day = 'sunday'
    df = load_data(city, month, day)
    
    get_raw(df)
    
    time_stats(df, month, day)
    station_stats(df, month, day)
    trip_duration_stats(df, month, day)
    user_stats(df, month, city, day)

    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() != 'yes':
       break


if __name__ == "__main__":
	main()
