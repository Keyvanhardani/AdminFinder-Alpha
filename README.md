# AdminFinder Alpha

AdminFinder Alpha is a Python-based tool designed to help users search for and locate admin panels on websites. It supports bypassing Cloudflare protection and accepts a list of admin paths to search through. The tool provides informative logs and colored output to indicate the status of the search.

## Installation

1. Clone the repository:

git clone https://github.com/yourusername/adminfinder-alpha.git
cd adminfinder-alpha
Install the required dependencies:

pip install -r requirements.txt
## Usage
Prepare a file containing a list of admin panel paths (one per line).
Run the script from the command line with the following arguments:


python app.py -u <URL> -f <admin_paths_file> [-b]

## Arguments
-u or --url: The URL of the website to search.
-f or --file: The path of the file containing admin panel paths.
-b or --bypass (optional): Include this flag to bypass Cloudflare protection.
Example

python app.py -u https://example.com -f paths.txt -b

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Requirements
The following Python packages are required for this project:

requests
argparse
logging
cloudscraper
termcolor

These dependencies can be installed by running pip install -r requirements.txt