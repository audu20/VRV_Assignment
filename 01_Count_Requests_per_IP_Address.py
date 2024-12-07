from collections import Counter  
#Imports the Counter class from the collections module. 
#This class is used to count the occurrence of items in the sample.log.

def analyze_log(filename):    
#Defines a function named analyze_log that takes a filename as input.
   
    with open(filename, 'r') as f:
        ip_addresses = [line.split()[0] for line in f]
    #Opens the specified file in read mode ('r').
    #Iterates through each line in the file.
    #Splits each line by whitespace and extracts the first element (the IP address).
     
    ip_counts = Counter(ip_addresses)
    #Creates a Counter object named ip_counts to count the each IP address in the ip_addresses file.
    
    sorted_ip_counts = ip_counts.most_common()
    # Sort the IP addresses by their counts in descending order
   
    for ip, count in sorted_ip_counts[:10]:
        print(f"{ip:15} {count}")
     # Print the top 10 most frequent IP addresses

if __name__ == "__main__":
    filename = "Sample.log"
    analyze_log(filename)

#Sets the filename variable to the path of the log file.
#Calls the analyze_log function with the specified filename.


