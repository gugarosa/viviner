from utils.requester import Requester

import utils.constants as c


# Instantiates a wrapper over the `requests` package
r = Requester('https://www.vivino.com/api/')

# Defines the payload, i.e., filters to be used on the search
payload = {
    "min_rating": 0
}

# Performs an initial request to get the number of records (wines)
res = r.get('explore/explore?', params=payload)
n_matches = res.json()['explore_vintage']['records_matched']

print(n_matches)

# Iterates through the amount of possible pages
for i in range(int(n_matches / c.RECORDS_PER_PAGE)):
    # Adds the page to the payload
    payload['page'] = i + 1

    print(f'Scraping data from page: {payload["page"]}')

    # Performs the request and scraps the URLs
    res = r.get('explore/explore', params=payload)
    matches = res.json()['explore_vintage']['matches']

    # for match in matches:
        # print(match)