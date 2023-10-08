import sys
sys.path.append(".")

from Robinhood.utils import *


def test_get_num_days_per_mon_within_range():
    # same month
    start_date_1 = "2023-09-29"
    end_date_1 = "2023-09-30"
    # end of month and start of month
    start_date_2 = "2023-09-30"
    end_date_2 = "2023-10-01"
    # deal with Feb
    start_date_3 = "2023-02-28"
    end_date_3 = "2023-03-01"
    # cross multipy months
    start_date_4 = "2023-02-28"
    end_date_4 = "2023-05-05"
    # cross year
    start_date_5 = "2023-12-28"
    end_date_5 = "2024-02-05"
    
    assert [2] == get_num_days_per_mon_within_range(start_date_1, end_date_1)
    assert [1, 1] == get_num_days_per_mon_within_range(start_date_2, end_date_2)
    assert [1, 1] == get_num_days_per_mon_within_range(start_date_3, end_date_3)
    assert [1, 31, 30, 5] == get_num_days_per_mon_within_range(start_date_4, end_date_4)
    assert [4, 31, 5] == get_num_days_per_mon_within_range(start_date_5, end_date_5)




