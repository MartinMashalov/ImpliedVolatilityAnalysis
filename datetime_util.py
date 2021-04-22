import datetime

def convertDatetoMinutes(date_series):
    '''
    Convert list of datetimes to minutes since midnight
    :param date_series: Collection of datetimes
    :return: List of minutes since midnight
    '''
    return [d.hour * 60 + d.minute for d in date_series]

def convertMinutestoTime(minute_series):
    '''
    Convert list of minutes since midnight to time objects
    :param minute_series: List of minutes since midnight
    :return: List of times
    '''
    temp = minute_series.flatten()
    hours = [datetime.time(t//60, t-t//60*60, 0).hour for t in temp]
    minutes = [datetime.time(t//60, t-t//60*60, 0).minute for t in temp]
    seconds = [datetime.time(t//60, t-t//60*60, 0).second for t in temp]
    length = len(hours)

    response_data = [str(hours[i]) + ':' + str(minutes[i]) + ':' + str(seconds[i]) for i in range(length)]
    print(response_data)

    return response_data