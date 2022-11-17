import argparse
import json

import utils.constants as c
from utils.requester import Requester


def get_arguments():
    """Gets arguments from the command line.

    Returns:
        A parser with the input arguments.

    """

    parser = argparse.ArgumentParser(usage='Scraps all wine data from Vivino.')

    parser.add_argument('output_file', help='Output .json file', type=str)

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
        "country_codes[]": "br",
        # "food_ids[]": 20,
        # "grape_ids[]": 3,
        # "grape_filter": "varietal",
        "min_rating": 3.7,
        # "order_by": "ratings_average",
        # "order": "desc",
        # "price_range_min": 25,
        # "price_range_max": 100,
        # "region_ids[]": 383,
        # "wine_style_ids[]": 98,
        # "wine_type_ids[]": 1,
        # "wine_type_ids[]": 2,
        # "wine_type_ids[]": 3,
        # "wine_type_ids[]": 4,
        # "wine_type_ids[]": 7,
        # "wine_type_ids[]": 24,
    }

    # Performs an initial request to get the number of records (wines)
    res = r.get('explore/explore?', params=payload)
    n_matches = res.json()['explore_vintage']['records_matched']

    print(f'Number of matches: {n_matches}')

    # Iterates through the amount of possible pages
    for i in range(start_page, max(1, int(n_matches / c.RECORDS_PER_PAGE)) + 1):
        # Creates a dictionary to hold the data
        data = {}
        data['wines'] = []

        # Adds the page to the payload
        payload['page'] = i

        print(f'Page: {payload["page"]}')

        # Performs the request and scraps the URLs
        res = r.get('explore/explore', params=payload)
        matches = res.json()['explore_vintage']['matches']

        # Iterates over every match
        for match in matches:
            # Gathers the wine-based data
            wine = match['vintage']['wine']

            # Popping redundant values
            if wine['style']:
                wine['style'].pop('country', None)
                wine['style'].pop('region', None)
                wine['style'].pop('grapes', None)

            print(f'Scraping data from wine: {wine["name"]}')

            # Appends current match to the dictionary
            data['wines'].append(wine)

            # Gathers the full-taste profile from current match
            res = r.get(f'wines/{wine["id"]}/tastes')
            tastes = res.json()

            # Replaces the taste profile
            data['wines'][-1]['taste'] = tastes['tastes']

        # Opens the output .json file
        with open(f'{i}_{output_file}', 'w') as f:
            # Dumps the data
            json.dump(data, f)
        
        # Closes the file
        f.close()
