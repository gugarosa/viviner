import requests

# Instantiate a dictionary of headers
# We only need to `manipulate` an User-Agent key
headers = {
    "User-Agent": ""
}

# Instantiate a dictionary of query strings
# Defines the only needed payload
payload = {
    "min_rating": 1,
    "order_by": "price",
    "order": "asc",
    "price_range_max": 500,
    "price_range_min": 1,
    "region_ids[]": 394
}

# Performs an initial request and gathers the amount of results
r = requests.get('https://www.vivino.com/api/explore/explore?',
                 params=payload, headers=headers)
n_matches = r.json()['explore_vintage']['records_matched']

# Iterates through the amount of possible pages
# A page is defined by n_matches divided by 25 (number of results per page)
for i in range(int(n_matches / 25)):
    # Adds the page on the payload
    payload['page'] = i + 1

    print(f'Requesting data from page: {payload["page"]}')

    # Performs the request and saves the matches
    r = requests.get('https://www.vivino.com/api/explore/explore?',
                     params=payload, headers=headers)
    matches = r.json()['explore_vintage']['matches']

    # Iterates through every match
    for match in matches:
        # Defines the wine's identifier
        _id = match['vintage']['wine']['id']

        # Defines a page counter
        page_counter = 1

        # Performs an all-time true loop
        while True:
            print(f'Requesting reviews from wine: {_id} and page: {page_counter}')

            # Performs the request and saves the reviews
            r = requests.get(f'https://www.vivino.com/api/wines/{_id}/reviews?per_page=50&page={page_counter}',
                             headers=headers)
            reviews = r.json()['reviews']

            print(f'Number of reviews: {len(reviews)}')

            # If there are no reviews anymore,
            # it indicates that the loop can be broken
            if len(reviews) == 0:
                # Breaks the loop
                break

            # Otherwise, increments the counter
            page_counter += 1
