# Testing Gibberish Detectors
This project tests different gibberish detector libraries against a set of queries.<br /><br />
For more information on any of these libraries, please cheeck their individual documentations and/or source code linked in the References section below

## What Each File Does

### Library Tests
- `fuzgib-combo-test.py` - incorporates Gibberish Detector and TheFuzz to create a search engine to filter gibberish queries and match fuzzy queries to pre-determined queries
- `fuzzy-matching-library-test.py` - tests TheFuzz capabilities on a set of queries, including matching fuzzy queries to pre-determined queries
- `gibberish-detector-library-test.py` - tests Gibberish Detector capabilities on a set of queries
- `gibberishpy-library-test.py` - attempt to run gibberishpy. However, this did not work
- `nostril-library-test.py` - tests nostril capabilities on a set of queries

### Other Files
- `idealist-philosophy-corpus.txt` - Corpus used to create model for gibberish-detector
- `philosophy.model` - model created from Gibbertish Detector's train feature using the Idealist Philosophy corpus, used as default model in Gibberish Detector and Combo tests
- `queries-fuzzy.txt` - text file of queries used to test TheFuzz
- `queries-list.py` - queries used to test libraries, formatted in a suitable datatype
- `queries.txt` - text file of queries used to test libraries
- `txt-convert.py` - converts a txt file to a list datatype that can easily be used for testing

## How to Run the Code Locally

### System Requirements
Ensure you have Python3 installed, found [here](https://www.python.org/downloads/).

### fuzzy-matching-library-test
#### Installation Steps
Install rapid_fuzz
```bash
pip install rapidfuzz
```
Install TheFuzz
```bash
pip install thefuzz
```
#### Running the Code
First, uncomment the function you’d like to test at the bottom of the file (lines 179 - 181) by deleting the first `#` or using `cmd + /`
There are 3 functions for the three tests that were conducted:
- `score_match` - Function to compare fuzzy queries to intended queries
- `gibberish_score` - Function to compare gibberish queries to intended queries
- `find_query` - Function to return requested number of matching results to query entered

You can then run the file
```bash
python fuzzy-matching-library-test.py
```

### gibberish-detector-library-test
#### Installation Steps
Install Gibberish Detector
```bash
pip install gibberish-detector
```
#### Running the Code
You can choose to use the default model, `philosophy.model`, or train your own model.<br />
To train a corpus to use as a model, enter the following to the CLI:
```bash
gibberish-detector train (text file) > file-name.model
```
Now you can refer to this as your model to detect gibberish against. Ensure to change the default model in the code to your new model.<br /><br />

You can either run the code in the CLI using:
```bash
gibberish-detector detect --model (your model) --interactive
```
Or you can run the function I created:
```bash
python gibberish-detector-library-test
```

### gibberishpy-library-test
***Please note that this library did not work for me. I was not able to run this code and I am only including the installation steps I found on the library's docs***
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

### fuzgib-combo-test
#### Installation Steps
Install Gibberish Detector
```bash
pip install gibberish-detector
```
Install rapid_fuzz
```bash
pip install rapidfuzz
```
Install TheFuzz
```bash
pip install thefuzz
```
#### Running the Code
You can choose to use the default model, `philosophy.model`, or train your own model.<br />
To train a corpus to use as a model, enter the following to the CLI:
```bash
gibberish-detector train (text file) > file-name.model
```
Now you can refer to this as your model to detect gibberish against. Ensure to change the default model in the code to your new model.<br /><br />
To run the code:
```bash
python fuzgib-combo-test.py
```

### txt-convert
#### Running the Code
In the CLI, run:
```bash
python txt-convert
```

## References

### Libraries 

#### RapidFuzz
* Source Code - https://github.com/rapidfuzz/RapidFuzz

#### TheFuzz
* Source Code - https://github.com/seatgeek/thefuzz

#### fuzzy_wuzzy (deprecated)
* Source Code - https://github.com/seatgeek/fuzzywuzzy

#### Gibberish Detector
* Source Code - https://github.com/domanchi/gibberish-detector
* Original Source Code - https://github.com/rrenaud/Gibberish-Detector

#### Gibberishpy (did not work)
* Source Code - https://github.com/yuenshingyan/gibberishpy

#### Nostril
* Documentation - https://github.com/casics/nostril/blob/master/docs/explanations/README.md  
* Paper - Hucka, M. (2018). Nostril: A nonsense string evaluator written in Python. Journal of Open Source Software, 3(25), 596, https://doi.org/10.21105/joss.00596  
* Source Code - https://github.com/casics/nostril 

### Documents

* Corpus used for `gibberish-detector-library-test` model - Randrup, Axel, 2006, Idealist Philosophy, Oxford Text Archive, http://hdl.handle.net/20.500.12024/2501
