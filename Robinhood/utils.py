import datetime
import pandas as pd
import yfinance as yf


CASH_APY = 0.049


def get_num_day_per_mon_within_range(start_date: str, end_date: str) -> list:
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


def calculate_cash_pnl(cash_amount: float, start_date: str, end_date: str, apy: float = CASH_APY) -> float:
    """
    Method that calculates how much the uninvested brokerage cash can earn.

    Parameters
    ----------
    start_date : str
        Assume in the format "YYYY-mm-dd".
    """
    daily_rate = apy / 365
    num_day_per_month = get_num_day_per_mon_within_range(start_date, end_date)
    
    pnl = []
    for days in num_day_per_month:
        pnl.append(cash_amount * daily_rate * days)
        cash_amount += pnl[-1]
    
    return cash_amount


def download_data(ticker: list, start_date: str, end_date: str) -> pd.DataFrame:
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")

    data = yf.download(ticker, start=start_date, end=end_date)

    return data


def convert_price_to_return(df: pd.DataFrame) -> pd.DataFrame:
    return df.pct_change(1)




def main():
    print(calculate_cash_pnl(17221, "2023-10-1", "2023-11-1"))


if __name__ == "__main__":
    main()



