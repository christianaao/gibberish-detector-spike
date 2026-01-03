from thefuzz import fuzz, process

# Query lists for testing library
intended_queries = [
    "the news today",
    "manchester news",
    "Turkiye",
    "Harry and Meghan",
    "Doctor Who",
    "Manchester city",
    "Manchester United",
    "Energy bills increase",
    "Dealer to plead guilty in Matthew Perry death",
    "UK inflation unexpectedly jumps to 3.6% as food prices rise again",
    "Trump in the White House",
    "US vs China chip manufacturing",
    "Artificial intelligence",
    "Europa League",
    "best dramas",
    "Telly",
    "Bestie",
    "hey, it's Olamide!",
    "oops, wrong password",
    "delulu",
]

fuzzy_queries = [
    "Thenewstoday",
    "msnchester bews",
    "Turkey",
    "megan and harry",
    "dr who",
    "man city",
    "manu",
    "nrg blls ncrs",
    "matthew perry guilty dealer",
    "uk intlashion unecpeft3rly jumpyd yo 3.6 per cent as food prices rise agin",
    "ttump in the the whit hoyse",
    "us v china chip making",
    "ai",
    "uropa lege",
    "bezt dramz",
    "tellie",
    "best friend",
    "h3y, 1t's 0l4m1d3!",
    "00ps-wr0ng_p4ssw0rd",
    "delusional",
]

gibberish_queries = [
    "sfsdsfsd",
    "dhasfd",
    "Ahnahfdsgv",
    "qwgfw ywegdbfehd hyfv",
    "/,./.,.//,@324.//.",
    "0123456789",
    "1i2uq234yt9u4r",
    ".’1;.[l’52q]kotg5rtgyy.;]",
    "h3y, 1t's 0l4m1d3!",
    "00ps-wr0ng_passw0rd",
    "       .x jx n",
    "consiethem",
    "merprithe",
    "slessom",
    "thatio",
    "fleep",
    "discorns",
    "proublesh",
    "consient",
    "naturn",
]


# Functions for testing library
def score_match(intended_query_list, fuzzy_query_list):
    """
    Function to compare fuzzy queries to the corresponding intended query

    Args

        takes two query lists, intended query list and fuzzy / gibberish query list (the fuzzy / gibberish query will be matched against the intended query)

    Returns

        a similarity score
    """
    i = 0

    while i < len(intended_query_list):
        iq = intended_query_list[i]
        fq = fuzzy_query_list[i]
        print(
            f"Intended Query: {iq} | Fuzzy Query: {fq} | Simple Fuzz Score: {fuzz.ratio(iq, fq)} | Partial Ratio Score: {fuzz.partial_ratio(iq, fq)} | Token Sort Ratio Score: {fuzz.token_sort_ratio(iq, fq)} | Token Set Ratio Score: {fuzz.token_set_ratio(iq, fq)} | Partial Token Sort Ratio Score: {fuzz.partial_token_sort_ratio(iq, fq)}"
        )
        print("-" * 180)
        i += 1


def giberish_score(intended_query_list, gibberish_query_list):
    """
    Function to compare gibberish queries to intended queries

    Check the similarity scores of every gibberish query against each intended query

    Args

        takes two lists: takes two query lists, intended query list and fuzzy / gibberish query list (each fuzzy / gibberish query will be matched against each of the intended query)

    Returns

        Comparison list detailing the scores of each fuzz ratio  for each gibberish query compared to the intended query
    """
    for iq in intended_query_list:
        print("Intended Query: ", iq)
        for gq in gibberish_query_list:
            print(
                f"Gibberish Query: {gq} | Simple Fuzz Score: {fuzz.ratio(iq, gq)} | Partial Ratio Score: {fuzz.partial_ratio(iq, gq)} | Token Sort Ratio Score: {fuzz.token_sort_ratio(iq, gq)} | Token Set Ratio Score: {fuzz.token_set_ratio(iq, gq)} | Partial Token Sort Ratio Score: {fuzz.partial_token_sort_ratio(iq, gq)}"
            )
        print("-" * 180)


def find_query(query_match_list, query_to_look_for=""):
    """
    Function to find the closest matching results from a given query

    Function will prompt you for query and number of matching results to return to you. If no amount is entered, it will return a score for every query in the query_match_list

    Args

        a list representing the 'search result' or the query that the user intended to input

    Returns

        list of requested number of results matching the query
    """
    query_to_look_for = input("enter query: ")
    num_of_results = input(
        "enter number of results to return, type 'all' for max results that match your query or enter '0' to see the score of all results against your query: "
    )

    def results():
        match num_of_results:
            case "0" | "":
                print(
                    f"Query: {query_to_look_for} | Results: ",
                    process.extract(query_to_look_for, query_match_list, limit=None),
                )
            case "1":
                print(
                    f"Query: {query_to_look_for} | Result: ",
                    process.extractOne(query_to_look_for, query_match_list),
                )
            case "all":
                print(
                    f"Query: {query_to_look_for} | Results: ",
                    process.extract(query_to_look_for, query_match_list),
                )
            case _:
                print(
                    f"Query: {query_to_look_for} | Results: ",
                    process.extract(
                        query_to_look_for, query_match_list, limit=int(num_of_results)
                    ),
                )

    if query_to_look_for:
        results()
    else:
        i = 0
        while i < len(fuzzy_queries):
            query_to_look_for = fuzzy_queries[i]
            results()
            print("-" * 180)
            i += 1


## Uncomment the function you'd like to use:

# score_match(intended_queries, fuzzy_queries)  # Function to compare fuzzy queries to intended queries
# giberish_score(intended_queries, gibberish_queries)  # Function to compare gibberish queries to intended queries - ** warning: this will output a lot of data **
# find_query(intended_queries)  # Function to return matching results to a given query
