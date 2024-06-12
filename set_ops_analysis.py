# Task 1: Duplicate Entries Cleanup

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004", 
 "C006", "C004", "C005", "C006"]


def remove_duplicates(customer_ids):
    unique_cust_ids = set(customer_ids)
    print(unique_cust_ids)

remove_duplicates(customer_ids)