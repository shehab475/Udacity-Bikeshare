import time
import calendar
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities=list(CITY_DATA.keys())
months=['january', 'february', 'march', 'april', 'may', 'june','all']

days={'monday', 'tuesday','wednesday','thursday','friday','saturday','sunday','all'}

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
      city=input("pick a city to analayze data (eg. chicago,new york city,washington) : ").lower()
      if city  in cities:
           break
      elif city not in cities:
           print('enter again with a correct city ')
      else:
                 break
    
    # TO DO: get user input for month (all, january, february, ... , june)
 
    
    while True :
      month=input("pick a month to analayze data (eg. january,february,... or all) : ").lower()    
      if month  in months:
             break
      elif month not in months:
           print('enter again with a correct month ')
      else:
                break
            
           

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
      day=input("pick a day to analayze data (eg. monday,tuesday,... or all) : ").lower()    
      if day in days:
                break
      elif day not in days:
                 print('enter again with a correct day ')
      else:
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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day']==day.title()]
    
    return df
    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
  
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months_by_number=df['month'].mode()[0]
    months_by_name =calendar.month_name[months_by_number]  
    print('common month is : {}'.format(months_by_name))
    # TO DO: display the most common day of week
     

    print('common day is : {} '.format(df['day'].mode()[0]))

    # TO DO: display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    hour1=df['hour'].mode()[0]
    if hour1<=12:
       print('common hour is : {} AM'.format(hour1))
    else:
         hour1-=12
         print('common hour is : {} PM'.format(hour1))
          

    print("\nThis took %s seconds." % round((time.time() - start_time),2))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station=df['Start Station'].mode()[0]
    print('common start station is :' , common_start_station)

    # TO DO: display most commonly used end station
    common_end_station=df['End Station'].mode()[0]
    print('common end station is :' , common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination_start_end']= (df['Start Station']+df['End Station'])
        
        
    print('most frequent combination of start station and end station trip\n' , df['combination_start_end'].mode()[0])
     

    print("\nThis took %s seconds." % round((time.time() - start_time),2))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_seconds=df['Trip Duration'].sum()
    total_trip_minutes=total_trip_seconds//60
    print('the total travel time is : {} minutes.'.format(round(total_trip_minutes,1)) )
    
    # TO DO: display mean travel time
    mean_trip_seconds=df['Trip Duration'].mean()
    mean_trip_minutes=mean_trip_seconds//60
    print('the mean travel time is : {} minutes. '.format(int(round(mean_trip_minutes,1))))

    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    print( df['User Type'].value_counts() )              
    # TO DO: Display counts of gender
    

    if city == 'washington':
        print('Gender : None')
    else:
        print( df['Gender'].value_counts() ) 
        
        
    # TO DO: Display earliest, most recent, and most common year of birth
        print('The most common year of birth is : {}.'.format(int(df['Birth Year'].mode()[0])))
        print('The most earliest year of birth is : {}.'.format(int(df['Birth Year'].min())))
        print('The most recent year of birth is : {}.'.format(int(df['Birth Year'].max())))
        
        

    print("\nThis took %s seconds."  % round((time.time() - start_time),2))
    print('-'*40)
def display_raw_data(df):
    """ Your docstring here """
    index = 5
    raw_data = input("Do you like to display raw data?\n(answer by 'Yes' or 'No') ").lower() # TO DO: convert the user input to lower case using lower() function
    

    while True:            
        if raw_data == 'no':
            print('Congratulations, this analyzing test is over.\nThank you.\nSee you later!')
            break
        elif raw_data == 'yes':
            print(df.head(index)) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw_data = input('Do you like to display extra 5 rows?\n(answer by Yes or No)').lower() # TO DO: convert the user input to lower case using lower() function
            index+=5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
