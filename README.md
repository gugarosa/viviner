# Viviner: Wine Data Scrapper

*This repository holds all the necessary code to run the an automation robot that extracts wine-related information at [Vivino](https://www.vivino.com).*

---

## Package Guidelines

### Installation

Install all the pre-needed requirements using:

```Python
pip install -r requirements.txt
```

### (Optional) Download the Data

We have already dumped all of Vivino's data and made available in both `.json` and `.csv` formats. Note that there might be some missing values as Vivino's database is incomplete for not well-known wines.

* [Vivino Brazilian Wine Data](https://www.recogna.tech/files/datasets/vivino_br_wine_data.tar.gz)

*The dataset and its additional information is also available at [Kaggle](https://www.kaggle.com/gthrosa/vivino-brazilian-wines-metadata)*.

---

## Usage

### Scrap Wines Meta-Data

Initially, one can extract every available wine using the following script:

```Python
python scrap_wine_data.py -h
```

*Note that `-h` invokes the script helper, which assists users in employing the appropriate parameters.*

### (Optional) Scrap List of Wines

One can also scrap/dump the list of wines (URL format) for further inspection. To accomplish such a step, one needs to use the following script:

```Python
python scrap_wine_list.py -h
```

---

## Support

We know that we do our best, but it is inevitable to acknowledge that we make mistakes. If you ever need to report a bug, report a problem, talk to us, please do so! We will be available at our bests at this repository.

---
