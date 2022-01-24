# Data for the article "New methods for analysing diachronic suffix competition across registers"

This repository contains the input data connected to the following article:

- Rodríguez-Puente, Paula, Tanja Säily and Jukka Suomela. "New methods for analysing diachronic suffix competition across registers: How *-ity* gained ground on *-ness* in Early Modern English". *International Journal of Corpus Linguistics.*


## data.json

The file `data.json` contains the following top-level elements:

**samples** = metadata on the corpus texts; each text is an object with the following key–value pairs:

- *corpus:* the corpus to which the text belongs
- *genre:* the genre to which the text belongs
- *period:* the time period to which the text belongs
- *sample:* the name of the text
- *words:* the number of running words in the text
- *year:* the year in which the text was written/published

**tokens** = the *-ness* and *-ity* tokens found in the corpora; each token is a list that contains the following elements in this order:

- *corpus:* see above
- *sample:* see above
- *dataset:* the suffix represented by the token (*-ness* or *-ity*)
- *token:* the *-ness/-ity* word in question, normalized to present-day spelling
- *before:* the context before the token in the text
- *word:* the token in its original spelling in the text
- *after:* the context after the token in the text

We refer to the article for more details on how the data was derived and how to interpret these records.


## CSV files

The CSV files `samples.csv` and `tokens.csv` contain the same information as `data.json`. The first one contains one sample per row, and the second one contains one token per row.

These files were created using the Python script `bin/json-to-csv.py`.


## License

The content is licensed under CC BY 4.0:
https://creativecommons.org/licenses/by/4.0/


## Authors

- Paula Rodríguez-Puente (the main author of this data set)
- Tanja Säily
- Jukka Suomela
