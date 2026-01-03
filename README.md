# Testing Gibberish Detectors
This project tests different gibberish detector libraries against a set of queries.
For more information on any of these libraries, please see the source code in the References section below

## What Each File Does

### Library Tests
**fuzgib-combo-test**: incorporates Gibberish Detector and TheFuzz to create a search engine to filter gibberish queries and match fuzzy queries to pre-determined queries
**fuzzy-matching-library-test**: tests TheFuzz capabilities on a set of queries, including matching fuzzy queries to pre-determined queries
**gibberish-detector-library-test**: tests Gibberish Detector capabilities on a set of queries
**gibberishpy-library-test**: attempt to run gibberishpy
**nostril-library-test**: tests nostril capabilities on a set of queries

### Other Files
**idealist-philosophy-corpus**: Corpus used to create model for gibberish-detector
**philosophy-model**: model created from Gibbertish Detector's train feature using the Idealist Philosophy corpus, used as default model in Gibberish Detector and Combo tests
**queries-fuzzy**: text file of queries used to test TheFuzz
**queries-list**: queries used to test libraries in a suitable format
**queries**: text file of queries used to test libraries
**txt-convert**: converts txt file to list datatype to easily be used for testing

## How to Run the Code Locally

### System Requirements
Ensure you have Python 3 installed, found [here](https://www.python.org/downloads/)

### fuzgib-combo-test
#### Installation Steps
Install rapid_fuzz
```bash
pip install rapidfuzz
```
Install thefuzz
```bash
pip install thefuzz
```
#### Running the Code
```bash
python fuzgib-combo-test.py
```

### fuzzy-matching-library-test
#### Installation Steps
Install rapid_fuzz
```bash
pip install rapidfuzz
```
Install thefuzz
```bash
pip install thefuzz
```
#### Running the Code
First, uncomment the function you’d like to test at the bottom of the file (lines 179 - 181) by deleting the first `#` or using `cmd + /`
There are 3 functions for the three tests that were conducted:
    * `score_match`: Function to compare fuzzy queries to intended queries
    * `gibberish_score`: Function to compare gibberish queries to intended queries
    * `find_query`: Function to return requested number of matching results to query entered

You can then run the file
```bash
python fuzzy-matching-library-test.py
```
### gibberish-detector-library-test
#### Installation Steps
Install gibberish detector
```bash
pip install gibberish-detector
```

#### Running the Code
To train a corpus to use as a model, enter the following to the CLI:
```bash
gibberish-detector train (text file) > file-name.model
```
Now you can refer to this as your model to detect gibberish against

### gibberishpy-library-test
**__* Please note that this library did not work for me. I was not able to run this code and I am only including the installation steps I found on the library's docs *__**
#### Installation Steps
Install gibberishpy
```bash
pip install gibberishpy
```

### nostril-library-test
#### Installation Steps
```bash
cd nostril
python3 -m pip install .
```
If this does not work, you can also try `sudo python3 -m pip install .`
#### Running the Code
You can either run the code in the CLI using:
```bash
nostril (query to test)
```
Or you can run the function I created:
```bash
python nostril-library-test.py
```
### txt-convert
#### Running the Code
In the CLI, run:
```bash
python txt-convert
```

## References

### Libraries

#### Nostril
**Documentation** - https://github.com/casics/nostril/blob/master/docs/explanations/README.md
Paper - Hucka, M. (2018). Nostril: A nonsense string evaluator written in Python. Journal of Open Source Software, 3(25), 596, https://doi.org/10.21105/joss.00596
**Source Code** - https://github.com/casics/nostril

#### RapidFuzz
**Source Code** - https://github.com/rapidfuzz/RapidFuzz

#### TheFuzz
**Source Code** - https://github.com/seatgeek/thefuzz

#### fuzzy_wuzzy (deprecated)
**Source Code** - https://github.com/seatgeek/fuzzywuzzy

#### Gibberish Detector
**Source Code** - https://github.com/domanchi/gibberish-detector
**Original Source Code** - https://github.com/rrenaud/Gibberish-Detector

#### Gibberishpy (did not work)
**Source Code** - https://github.com/yuenshingyan/gibberishpy

### Documents

**Corpus used for gibberish-detector** - Randrup, Axel, 2006, Idealist Philosophy, Oxford Text Archive, http://hdl.handle.net/20.500.12024/2501