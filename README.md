# AdminFinder Alpha

AdminFinder Alpha is a Python-based tool designed to help users search for and locate admin panels on websites. It supports bypassing Cloudflare protection and accepts a list of admin paths to search through. The tool provides informative logs and colored output to indicate the status of the search.

## Installation

1. Clone the repository:

git clone https://github.com/Keyvanhardani/Adminfinder-Alpha.git

cd Adminfinder-Alpha

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

## Debian 
adminfinder -u <URL> -f <admin_paths_file> [-b]

## Windows

AdminFinder-Alpha for Windows is a powerful and user-friendly tool designed to help website administrators, security researchers, and penetration testers discover admin panels and login pages. With its efficient and accurate scanning capabilities, AdminFinder-Alpha streamlines the process of identifying potential points of entry to secure or test web applications.

Key features:

1.  Easy-to-use interface: AdminFinder-Alpha is designed with usability in mind, allowing users to easily set up and initiate scans without any hassle.

2.  Extensive scanning techniques: AdminFinder-Alpha uses advanced algorithms to perform comprehensive scans of websites, efficiently identifying admin panels and login pages.

3.  Customizable scan parameters: Users can tailor the scanning process according to their requirements, adjusting the depth and scope of the scans.

4.  Supports multiple platforms: AdminFinder-Alpha is built to work seamlessly on various Windows operating systems, ensuring compatibility and optimal performance across different devices.

5.  Regular updates: AdminFinder-Alpha is continuously updated to ensure it stays current with the latest security practices and web technologies.

6.  Comprehensive documentation and support: The tool comes with a detailed user guide and dedicated support to help users get the most out of AdminFinder-Alpha.

Discover and secure admin panels with ease using AdminFinder-Alpha for Windows. Download now and enhance the security of your web applications today!
