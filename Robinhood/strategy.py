from utils import *


CASH_APY = 0.049


def calculate_cash_pnl(cash_amount: float, start_date: str, end_date: str, apy: float = CASH_APY) -> float:
    """
    Method that calculates how much the uninvested brokerage cash can earn.

    Parameters
    ----------
    start_date : str
        Assume in the format "YYYY-mm-dd".
    """
    daily_rate = apy / 365
    num_days_per_month = get_num_days_per_mon_within_range(start_date, end_date)
    
    pnl = []
    for days in num_days_per_month:
        pnl.append(cash_amount * daily_rate * days)
        cash_amount += pnl[-1]
    
    return cash_amount






def main():
    print(calculate_cash_pnl(17221, "2023-10-1", "2023-11-1"))



if __name__ == "__main__":
    main()

