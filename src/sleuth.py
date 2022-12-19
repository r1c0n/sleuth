# Import necessary modules (run sh/install_requirements.sh if you get any error regarding these. If that doesn't fix it create an issue on the repo.)
import argparse
import conf.var as var
from conf.links import links_list

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add an argument with a short and long option
parser.add_argument("-u", "--user", required=True, help="Username to look up")

# Parse the command line arguments
args = parser.parse_args()

# Extract the values of the arguments
user = args.user

# Prints out links if the user argument has a value
if user:
    links_string = f"\nYou are currently running {var.product} v{var.v}, created by {var.creator}"
    links_string += "\n----------------------------------------------" 
    links_string += "\n".join(link.format(user=user) for link in links_list)
    
    print(links_string)