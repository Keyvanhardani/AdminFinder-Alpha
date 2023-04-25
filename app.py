import requests
import argparse
import logging
from cloudscraper import create_scraper
from termcolor import colored

banner_top = """ 

                ,%%%%%%,
               ,%%/\%%%%/\%%
              ,%%%\c "" J/%%%
  %.       %%%%/ o  o \%%%%%
  `%%.     %%%%    _  |%%%%
   `%%     `%%%%(__Y__)%%'      AdminFinder Alpha
   //       ;%%%%`\-/%%%%'
  ((       /  O \%%%%^^^
   \\     ,'     `--' |//
    \\   /           // 
     `"`'           ((


            """

banner_bottom = """
            """

version = colored("Version 1.2.1 by Keyvan Hardani (keyvan@hardani.de)", "red")

BANNER = banner_top + version + banner_bottom
# Set up command-line arguments
parser = argparse.ArgumentParser(description="Search for an admin panel on a website.")
parser.add_argument("-u", "--url", required=True, help="The URL of the website to search.")
parser.add_argument("-b", "--bypass", action="store_true", help="Bypass Cloudflare protection.")
parser.add_argument("-f", "--file", required=True, help="The path of the file containing admin paths.")

# Set up logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

def add_trailing_slash(url):
    """Add a trailing slash to the URL if it doesn't already have one"""
    if url[-1] != "/":
        return url + "/"
    else:
        return url

# Define function to search for admin panel
def search_admin_panel(url, bypass, admin_paths_file):
    # Create HTTP session
    if bypass:
        session = create_scraper()
    else:
        session = requests.Session()

    # Read admin paths from file
    with open(admin_paths_file) as f:
        admin_paths = f.read().splitlines()

    # Loop through admin panel paths and file extensions
    found = False
    print(BANNER)
    for path in admin_paths:
        admin_url = url + path
        response = session.get(admin_url)

        logger.info(f"Sending request to {admin_url}...")

        if response.status_code == 200:
           # logger.info(f"Found admin panel at {admin_url}")
            found = True
            print(colored(f"Found admin panel at {admin_url}", "green"))
            break

    if not found:
        logger.info("Admin panel not found")
        print(colored("Admin panel not found", "red"))

# Parse command-line arguments and call search_admin_panel function
if __name__ == "__main__":
    args = parser.parse_args()
    url = add_trailing_slash(args.url)
    bypass = args.bypass
    admin_paths_file = args.file
    search_admin_panel(url, bypass, admin_paths_file)