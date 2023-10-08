import datetime


def get_num_days_per_mon_within_range(start_date: str, end_date: str) -> list:
    """
    Method that calculates number of days in each month between start date and end date.

    Parameters
    ----------
    start_date : str
        Assume in the format "YYYY-mm-dd".
    """
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")

    result = []
    curr_date = start_date
    while curr_date < end_date:
        if curr_date.month == end_date.month:
            result.append( (end_date-curr_date).days + 1 )
            break
        temp_date = curr_date + datetime.timedelta(days=31)
        temp_date = temp_date.replace(day=1)
        
        if temp_date == end_date:
            result.append( (temp_date-curr_date).days )
            result.append(1)
            break
        else:
            result.append( (temp_date-curr_date).days )
            curr_date = temp_date

    return result



