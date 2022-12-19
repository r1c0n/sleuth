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
        # Basic program information
        links = f"\nYou are currently running {var.product} v{var.v}, created by {var.creator}"
        links += "\n----------------------------------------------" 
        # Links
        links += f"\nhttps://twitter.com/{user}"
        links += f"\nhttps://www.facebook.com/{user}"
        links += f"\nhttps://linkedin.com/in/{user}"
        links += f"\nhttps://www.snapchat.com/app/{user}"
        links += f"\nhttps://www.instagram.com/{user}"
        links += f"\nhttps://www.tiktok.com/@{user}"
        links += f"\nhttps://www.pinterest.com/{user}"
        links += f"\nhttps://www.tumblr.com/blog/view/{user}"
        links += f"\nhttps://www.reddit.com/user/{user}"
        links += f"\nhttps://github.com/{user}"
        links += f"\nhttps://www.flickr.com/photos/{user}"
        links += f"\nhttps://soundcloud.com/{user}"
        links += f"\nhttps://t.me/{user}"
        links += f"\nhttps://www.bitview.net/profile.php?user={user}"
        links += f"\nhttps://www.vidlii.com/user/{user}"
        links += f"\nhttps://www.guilded.gg/{user}"                  
        links += f"\nhttps://www.guilded.gg/u/{user}"
        links += f"\nhttps://bwitter.me/{user}"
        links += f"\nhttps://youtube.com/user/{user}"
        links += f"\nhttps://codepen.io/{user}"
        links += f"\nhttps://pastebin.com/u/{user}"
        links += f"\nhttps://replit.com/@{user}"
        links += f"\nhttps://{user}.carrd.co"
        links += f"\nhttps://www.crunchyroll.comc/user/{user}"
        links += f"\nhttps://scratch.mit.edu/users/{user}"
        links += f"\nhttps://discords.com/bio/p/{user}"
        links += f"\nhttps://www.twitch.tv/{user}"
        links += f"\nhttps://{user}.newgrounds.com"
        links += f"\nhttps://archive.org/details/@{user}"
        links += f"\nhttps://{user}.github.io"
        links += f"\nhttps://vimeo.com/{user}"
        links += f"\nhttps://youtube.com/@{user}"
        links += f"\nhttps://about.me/{user}"
        links += f"\nhttps://{user}.ct8.pl"
        links += f"\nhttps://community.brave.com/u/{user}"
        links += f"\nhttps://{user}.infinityfreeapp.com"
        links += f"\nhttps://{user}.rf.gd"
        links += f"\nhttps://{user}.great-site.net"
        links += f"\nhttps://{user}.epizy.com"
        links += f"\nhttps://{user}.42web.io"
        links += f"\nhttps://{user}.lovestoblog.com"

        print(links)