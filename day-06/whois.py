"""WhoIs API Fetcher

This script allows the user to fetch whoisxml api to get a JSON file
from the list of IPs provided by the user.

This tool creates a JSON file per request.

This script requires that `whois-api` be installed within the Python
environment you are running this script in.
See more at: https://pypi.org/project/whois-api/

This file can also be imported as a module and contains the following
function:

    * main - the main function of the script

MUST HAVE:

# Set an API key by creating a whoisxml account
# Get a JSON from the API. Save this file in a folder.
# From the root folder, read the ips.txt file line by line to get an IP
# Be creative, try to apply at least "try", "except", "Exception" for error handling when opening a file.
# If the script find an error while the program is fetching the API, it's going to throw an error message on the console.
# 	    You need to CREATE a new txt file called "failed_ips" in the root folder where the IPs with errors are going to be stored.
# After fetching all the IPs, you must use this "failed_ips" file to try to fetch again the failed IP.
# BONUS (optional): use exceptions from the API, for example: ApiAuthError

HINTS:

1. Install 'whois-api' library from the following link:
		https://pypi.org/project/whois-api/
2. In the root folder, create a new txt file named "ips".
3. Insert all the UNIQUE IPs in the ips.txt file. One IP per row.
3. Insert all the IPs in the ips.txt file. One IP per row.

RECOMMENDATIONS:

1. One whoisxml account is going to provide only 500 API requests. You need to create multiple accounts in order to have more requests.
2. I use the proton.me mail service to create an email faster and register a new whoisxml account. It will allow you only to create
		at least 2 accounts per your IP, so I used MY PERSONAL PC to use a free VPN to create new accounts and avoid the service SPAM filter.
3. I only introduced 500 IPs into the ips.txt file.
4. When I finish, I copied the IPs from the "failed_ips" txt file to try to fetch them again. Generally, the second try is going to give me
		the JSON file when the IP presents an error.

NOTE:
1. ipv6 is not valid.
2. Local IP addresses are not valid.
3. Empty rows are not valid. Please make sure to have only ips in the ips.txt file.
"""

