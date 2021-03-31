"""Module used to merge and export data, and detect duplicates."""

import json
from itertools import chain, starmap


def merge_json_files(file_name, n_files=1):
    """Merges a set of indexed JSON files (1, 2, ..., n) into a new one.

    Args:
        file_name (str): Name of the file to be merged without their indexes and extension.
        n_files (int): Amount of files to be merged.

    Returns:
        The merged file.

    """

    # Creates the data object and its `strains` array
    data = {}
    data['wines'] = []

    # Iterates through every possible file
    for i in range(n_files):
        # Opens the input file
        with open(f'{i+1}_{file_name}', 'r') as f:
            # Loads the temporary data
            tmp_data = json.load(f)

            # Merges the data
            data['wines'] += tmp_data['wines']

        # Closes the file
        f.close()

    # Removes any possible duplicates
    unique_data = list({row['seo_name']: row for row in data['wines']}.values())

    # Opens the output file
    with open(f'{file_name}', 'w') as f:
        # Dumps the merged data
        json.dump(unique_data, f)


def flatten_json_file(json_file):
    """Flattens a multi-level nested JSON file.

    Args:
        json_file (str): Name of the file to be loaded and flattened.

    Returns:
        List containing every flattened record from JSON file.

    """

    def _depack(key, value):
        # Checks whether value is a dictionary
        if isinstance(value, dict):
            # Iterates for every key and value
            for k, v in value.items():
                # Creates a new key string
                new_k = f'{key}_{k}'

                yield new_k, v

        # Checks whether value is a list
        elif isinstance(value, list):
            # Iterates through every value
            for i, v in enumerate(value):
                # Creates a new key string
                new_k = f'{key}_{i}'

                yield new_k, v

        # If the key is not nested
        else:
            yield key, value

    # Opens the JSON file
    with open(json_file, 'r') as f:
        # Loads the JSON file
        json_data = json.load(f)

    # Instantiates a list that will hold every unpacked data
    json_data_list = []

    # Iterates through every sample in the data
    for json_datum in json_data:
        # Performs an all-time true loop
        while True:
            # Unpacks the file
            json_datum = dict(chain.from_iterable(starmap(_depack, json_datum.items())))

            # Creates a loop-break condition
            if not any(isinstance(value, (dict, list)) for value in json_datum.values()):
                break

        # Appends to the list
        json_data_list.append(json_datum)

    return json_data_list
