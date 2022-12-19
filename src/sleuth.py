# Import necessary modules (run sh/install_requirements.sh if you get any error regarding these. If that doesn't fix it create an issue on the repo.)
import argparse
import conf.var as var

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add an argument with a short and long option
parser.add_argument("-u", "--username", required=True, help="Username to look up")

# Parse the command line arguments
args = parser.parse_args()

# Extract the values of the arguments
user = args.user

# Prints out links if the user argument has a value
if user:
    print(
            # Basic program information
            f"\nYou are currently running {var.product} v{var.v}, created by {var.creator}"
            "\n----------------------------------------------" + 
            # Links
            f"\nhttps://twitter.com/{user}" +
            f"\nhttps://www.facebook.com/{user}" +
            f"\nhttps://linkedin.com/in/{user}" +
            f"\nhttps://www.snapchat.com/app/{user}" +
            f"\nhttps://www.instagram.com/{user}" +
            f"\nhttps://www.tiktok.com/@{user}" +
            f"\nhttps://www.pinterest.com/{user}" +
            f"\nhttps://www.tumblr.com/blog/view/{user}" +
            f"\nhttps://www.reddit.com/user/{user}" +
            f"\nhttps://github.com/{user}" +
            f"\nhttps://www.flickr.com/photos/{user}" +
            f"\nhttps://soundcloud.com/{user}" +
            f"\nhttps://t.me/{user}" +
            f"\nhttps://www.bitview.net/profile.php?user={user}" +
            f"\nhttps://www.vidlii.com/user/{user}" +
            f"\nhttps://www.guilded.gg/{user}" +                     
            f"\nhttps://www.guilded.gg/u/{user}" +
            f"\nhttps://bwitter.me/{user}" +   
            f"\nhttps://youtube.com/user/{user}" +   
            f"\nhttps://codepen.io/{user}" +   
            f"\nhttps://pastebin.com/u/{user}" +   
            f"\nhttps://replit.com/@{user}" +   
            f"\nhttps://{user}.carrd.co" +   
            f"\nhttps://www.crunchyroll.comc/user/{user}" +   
            f"\nhttps://scratch.mit.edu/users/{user}" +   
            f"\nhttps://discords.com/bio/p/{user}" +   
            f"\nhttps://www.twitch.tv/{user}" +   
            f"\nhttps://{user}.newgrounds.com" +   
            f"\nhttps://archive.org/details/@{user}" +   
            f"\nhttps://{user}.github.io" +   
            f"\nhttps://vimeo.com/{user}" +   
            f"\nhttps://youtube.com/@{user}" +   
            f"\nhttps://about.me/{user}" +   
            f"\nhttps://{user}.ct8.pl" +   
            f"\nhttps://community.brave.com/u/{user}" +   
            f"\nhttps://{user}.infinityfreeapp.com" +   
            f"\nhttps://{user}.rf.gd" +   
            f"\nhttps://{user}.great-site.net" +   
            f"\nhttps://{user}.epizy.com" +   
            f"\nhttps:///{user}.42web.io" +   
            f"\nhttps:///{user}.lovestoblog.com"   
        )