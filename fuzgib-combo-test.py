from gibberish_detector import detector
from thefuzz import fuzz, process

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


def search_engine(preset_queries):
    """
    Function to filter gibberish queries while passing through fuzzy queries

    Args:

        takes a list of preset queries / availabble article titles

    Returns:

        if the word is gibberish, will return an error message
        if the query is real, it will return a list of results matching the query or will return a search suggestion where it struggled to match queries:
            if fuzz match finds that the similarity score is high enough to match any of its preset queries, it will return the search results
            if fuzz gives it a low score, it will create a "did you mean..." message for the closest result it got
    """
    # filter out any gibberish immediately
    user_query = input("Query: ")
    Detector = detector.create_from_model("philosophy.model")
    if Detector.is_gibberish(user_query):
        return print(
            f"Sadly, we could not find a result for '{user_query}'. Please try again."
        )

    # loop through queries to get scores of all preset query against the user_query and find the highest scores
    token_sort_ratio_score = fuzz.token_sort_ratio(preset_queries[0], user_query)
    partial_token_sort_score = fuzz.partial_token_sort_ratio(
        preset_queries[0], user_query
    )
    i = 1
    while i < len(preset_queries):
        q = preset_queries[i]
        new_ts_score = fuzz.token_sort_ratio(q, user_query)
        new_pts_score = fuzz.partial_token_sort_ratio(q, user_query)

        if (
            new_ts_score > token_sort_ratio_score
            and new_pts_score > partial_token_sort_score
        ):
            token_sort_ratio_score = new_ts_score
            partial_token_sort_score = new_pts_score
        i += 1

    # scores at 65 or higher should pass through as search results using either token sort ratio for balanced acceptance or partial token for lenient acceptance (or both as done below)
    if token_sort_ratio_score >= 65 and partial_token_sort_score >= 65:
        results = process.extract(user_query, preset_queries)
        print("Here are your results:")
        for r in results:
            print(r[0])

    # if there are no scores higher than 65, find the highest score and return it as a "did you mean..." suggestion using extractOne
    else:
        return print(
            f" We could not find a match for '{user_query}'. Did you mean '{process.extractOne(user_query, preset_queries)[0]}'?"
        )


search_engine(intended_queries)
