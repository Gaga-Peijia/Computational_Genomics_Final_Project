from concurrent.futures import ThreadPoolExecutor

# Constants
NUM_PARTITIONS = 1024
num_workers = 8  # Number of threads

def sort_seeds(hash_table):
    """ Sorts the dictionary by keys in lexicographic order. """
    sorted_keys = sorted(hash_table)
    return sorted_keys


# Using ThreadPoolExecutor to process partitions in parallel
with ThreadPoolExecutor(max_workers=num_workers) as executor:
    # Submitting all partitions to be processed in parallel
    futures = [executor.submit(sort_seeds, i) for i in range(NUM_PARTITIONS)]

    # Wait for all partitions to be processed
    for future in futures:
        try:
            result = future.result()  # Handle the results
        except Exception as e:
            print(f"An error occurred: {e}")
# The sorted hash tables are now stored in sorted_query_hash_table and sorted_reference_hash_table


# Sort the global hash tables
'''
sorted_query_hash_table = sort_seeds(query_hash_tables)
sorted_reference_hash_table = sort_seeds(reference_hash_tables)
print(query_hash_tables)
print(sorted_query_hash_table)
'''
