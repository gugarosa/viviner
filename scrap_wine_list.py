import argparse

import utils.constants as c
from utils.requester import Requester


def get_arguments():
    """Gets arguments from the command line.

    Returns:
        A parser with the input arguments.

    """

    parser = argparse.ArgumentParser(usage='Scraps all wine URLs from Vivino.')

    parser.add_argument('output_file', help='Output .txt file', type=str)

    parser.add_argument('-start_page', help='Starting page identifier', type=int, default=1)

    return parser.parse_args()


if __name__ == '__main__':
    # Gathers the input arguments and its variables
    args = get_arguments()
    output_file = args.output_file
    start_page = args.start_page

    # Instantiates a wrapper over the `requests` package
    r = Requester(c.BASE_URL)

    # Defines the payload, i.e., filters to be used on the search
    payload = {
        "min_rating": 0
    }

    # Performs an initial request to get the number of records (wines)
    res = r.get('explore/explore?', params=payload)
    n_matches = res.json()['explore_vintage']['records_matched']

    print(f'Number of matches: {n_matches}')

    # Iterates through the amount of possible pages
    for i in range(start_page, int(n_matches / c.RECORDS_PER_PAGE) + 1):
        # Adds the page to the payload
        payload['page'] = i

        print(f'Scraping data from page: {payload["page"]}')

        # Performs the request and scraps the URLs
        res = r.get('explore/explore', params=payload)
        matches = res.json()['explore_vintage']['matches']

        # Opens the output file with append
        with open(output_file, 'a') as f:
            # Iterates over every match
            for match in matches:
                # Dumps the URL to file
                f.write(f'{c.BASE_URL}w/{match["vintage"]["wine"]["id"]}\n')
