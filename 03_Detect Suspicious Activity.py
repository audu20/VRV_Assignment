import re
# This module specifically for matching patterns in text.

def detect_brute_force(filename, threshold=10):
#Detects potential brute force attacks in a log file.
# Args filename the path to the log file.
#threshold: The maximum number of failed login attempts allowed per IP.
#Returns: A list of tuples, each containing an IP address and its failed login count.

    failed_logins = {}
    # to store IP addresses 
    with open(filename, 'r') as f:
        for line in f:
            ip_address = re.search(r'\d+\.\d+\.\d+\.\d+', line)
            if ip_address:
                ip = ip_address.group(0)
                if "401 Unauthorized" in line or "Invalid credentials" in line:
                    failed_logins[ip] = failed_logins.get(ip, 0) + 1
    # Uses a regular expression to extract the IP address from the line.
    # If the IP address is not in the dictionary, it's added with a count of 1.

    suspicious_ips = [(ip, count) for ip, count in failed_logins.items() if count >= threshold]
    return suspicious_ips
    #Creates a list of tuples, where each tuple contains an IP address and its corresponding failed login count.

if __name__ == "__main__":
    filename = "Sample.log"  # Replace with your log file name
    threshold = 10  # Adjust the threshold as needed

    suspicious_ips = detect_brute_force(filename, threshold)

    if suspicious_ips:
        print("Suspicious Activity Detected:")
        print("IP Address\tFailed Login Attempts")
        for ip, count in suspicious_ips:
            print(f"{ip}\t\t{count}")
    else:
        print("No suspicious activity detected.")


        