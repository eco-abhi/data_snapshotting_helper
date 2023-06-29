from datetime import date, datetime, timedelta

# Define the start and end dates for the date range
start_date = datetime.strptime('01/01/2023', '%m/%d/%Y').date()
end_date = date.today()

# Initialize an empty list to store the generated date strings
date_list = []

# Loop through the dates from the start date to the end date
current_date = start_date
while current_date <= end_date:
    # Format the current date as a SQL statement representing a date
    date_string = current_date.strftime("SELECT '%Y-%m-%d'::date AS date_month")
    # Append the date string to the list
    date_list.append(date_string)
    # Increment the current date by one day
    current_date += timedelta(days=1)

# Join the date strings using "UNION ALL" as the separator
result_string = "\nUNION ALL\n".join(date_list)

# Create the query to create a table using the result string
snapshot_helper_query = f"CREATE TABLE rivian_t2_supplychain_stg.data_snapshotting_helper as {result_string}"

# Print the query
print(snapshot_helper_query)
