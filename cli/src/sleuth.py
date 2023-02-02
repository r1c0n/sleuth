#########################################################################
# Find social media accounts, in bulk, with ease!                       #
# Copyright (C) 2021 - 2022  r1c0n                                      #
#                                                                       #
# This program is free software: you can redistribute it and/or modify  #
# it under the terms of the GNU General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or     #
# (at your option) any later version.                                   #
#                                                                       #
# This program is distributed in the hope that it will be useful,       #
# but WITHOUT ANY WARRANTY; without even the implied warranty of        #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
# GNU General Public License for more details.                          #
#                                                                       #
# You should have received a copy of the GNU General Public License     #
# along with this program.  If not, see <https://www.gnu.org/licenses/> #
#########################################################################


# Import necessary modules
import argparse
import conf.var as var
from conf.links import links_list

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add the user argument
parser.add_argument("-u", "--user", required=True, help="Username to look up")

# Parse the command line arguments
args = parser.parse_args()

# Extract the values of the arguments
user = args.user

# Prints out links if the user argument has a value
if user:
    links_string = f"\nYou are currently running {var.product} v{var.v}, created by {var.creator}.\n\n{var.legal}"
    links_string += "\n----------------------------------------------" 
    links_string += "\n".join(link.format(user=user) for link in links_list)
    
    print(links_string)