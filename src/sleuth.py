# Import necessary modules (run sh/install_requirements.sh if you get any error regarding these. If that doesn't fix it create an issue on the repo.)
import argparse
import conf.var as var

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
    print(
            # Basic program information
            "\nYou are currently running product version: " + var.product + " v" + var.v + ", created by " + var.creator +
            "\n----------------------------------------------" + 
            # Links
            "\nhttps://twitter.com/" + user +
            "\nhttps://www.facebook.com/" + user +
            "\nhttps://linkedin.com/in/" + user +
            "\nhttps://www.snapchat.com/app/" + user +
            "\nhttps://www.instagram.com/" + user +
            "\nhttps://www.tiktok.com/@" + user +
            "\nhttps://www.pinterest.com/" + user +
            "\nhttps://www.tumblr.com/blog/view/" + user +
            "\nhttps://www.reddit.com/user/" + user +
            "\nhttps://github.com/" + user +
            "\nhttps://www.flickr.com/photos/" + user +
            "\nhttps://soundcloud.com/" + user +
            "\nhttps://t.me/" + user +
            "\nhttps://www.bitview.net/profile.php?user=" + user +
            "\nhttps://www.vidlii.com/user/" + user +
            "\nhttps://www.guilded.gg/" + user +                     
            "\nhttps://www.guilded.gg/u/" + user
        )