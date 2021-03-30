"""Module used to merge and export data, and detect duplicates."""

import json


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
        with open(f'{file_name}_{i+1}.json', 'r') as f:
            # Loads the temporary data
            tmp_data = json.load(f)

            # Merges the data
            data['wines'] += tmp_data['wines']

        # Closes the file
        f.close()

    # Removes any possible duplicates
    unique_data = list({row['seo_name']: row for row in data['wines']}.values())

    # Opens the output file
    with open(f'{file_name}.json', 'w') as f:
        # Dumps the merged data
        json.dump(unique_data, f)
