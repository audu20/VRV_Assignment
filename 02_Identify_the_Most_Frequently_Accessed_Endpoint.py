from collections import Counter

def most_frequent_endpoint(filename): 
   # Argument 'filename' The path to the log file.
   # Returns: A tuple containing the most frequent endpoint and its count.
    
    with open(filename, 'r') as f:
        endpoints = [line.split()[6].split('/')[1] for line in f]
    # Opens the specified file in read mode ('r')
    # Iterates through each line in the file.
    # Appends the extracted endpoint to the endpoints list.

    endpoint_counts = Counter(endpoints)
    most_common_endpoint = endpoint_counts.most_common(1)[0]
    # Creates a Counter object named endpoint_counts to count the occurrences of each endpoint in the Sample log file.
    # Uses the most_common(1) method to get the most frequent endpoint and its count as a tuple.
    return most_common_endpoint

if __name__ == "__main__":
    filename = "Sample.log"  # Replace with log file name
    endpoint, count = most_frequent_endpoint(filename)
    print(f"Most Frequently Accessed Endpoint:\n{endpoint} (Accessed {count} times)")
#- Prints the most frequent endpoint and its count in a formatted string.

