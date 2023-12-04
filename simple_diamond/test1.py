import radix_cluster
import datetime
first_datetime = datetime.datetime.now()
query_hash_tables = {'CTT': [0,2,6], 'ATT': [2,9,10]}
reference_hash_tables = {'CTT': [0,2,6], 'ATT': [2,9,10]}

sorted_query_hash_table = radix_cluster.sort_seeds(query_hash_tables)
sorted_reference_hash_table = radix_cluster.sort_seeds(reference_hash_tables)
last_date_time = datetime.datetime.now()
print(last_date_time - first_datetime)