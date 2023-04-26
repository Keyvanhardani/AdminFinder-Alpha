from . import app

def main():
    # Set up command-line arguments
    parser = app.argparse.ArgumentParser(description="Search for an admin panel on a website.")
    parser.add_argument("-u", "--url", required=True, help="The URL of the website to search.")
    parser.add_argument("-b", "--bypass", action="store_true", help="Bypass Cloudflare protection.")
    parser.add_argument("-f", "--file", required=True, help="The path of the file containing admin paths.")

    # Parse command-line arguments and call search_admin_panel function
    args = parser.parse_args()
    url = app.add_trailing_slash(args.url)
    bypass = args.bypass
    admin_paths_file = args.file
    app.search_admin_panel(url, bypass, admin_paths_file)

if __name__ == "__main__":
    main()
