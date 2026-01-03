from gibberish_detector import detector

query_list = [
    "ai",
    "gaza",
    "harry and meghan",
    "david white on bbc radio cornwall",
    f"uk inflation unexpectedly jumps to 3.6% as food prices rise again",
    "dealer to plead guilty in matthew perry death",
    "fire",
    "best dramas",
    "indecent",
    "Radiohead",
    "Doctor Who",
    "Rugby",
    "Inflation",
    "Artifical intelligence",
    "US vs China chip manufacturing",
    "Europa League",
    "Russia",
    "Trump",
    "Fire",
    "Energy bills increase",
]

natural_queries = [
    "Thenewstoday",
    "msnchester bews",
    "Turkiye",
    "Selfie",
    "Telly",
    "Bestie",
    "BBC",
    "Npc",
    "Iykyk",
    "Skibidi",
    "Delulu",
    "agentic",
    "boujee",
    "overtourism",
    "Rage bait",
    "Lewk",
    "Memeify",
    "nepo baby",
    "Rizz",
    "Brain rot",
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
    "00ps-wr0ng_p4ssw0rd",
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

# query dict
queries = {
    "query list": query_list,
    "natural queries": natural_queries,
    "gibberish queries": gibberish_queries,
}


def check_queries(query_object, model="philosophy.model"):
    """
    Function to evaluate whether given query is gibberish or not

    Args

        takes an dictionary of query lists and an optional arg of model to detect gibberish against (will default to own philosophy.model if none is given)

    Returns

        String confirming if library evaluated the query to True (i.e. it is a gibberish query) or False (it is a real query)
    """
    Detector = detector.create_from_model(model)

    for query_list_name, list in query_object.items():
        for q in list:
            if Detector.is_gibberish(q):
                print(
                    f"{query_list_name.upper()} {q} evaluated to TRUE: Query deemed to be GIBBERISH"
                )
            else:
                print(
                    f"{query_list_name.upper()} {q} evaluated to FALSE: Query deemed to be REAL"
                )


# def gibberish_filter(query, model="big.model"):
#     Detector = detector.create_from_model(model)

#     query_list = query.split(" ")
#     filtered_list = []
#     for q in query_list:
#         if Detector.is_gibberish(q) == False:
#             filtered_list.append(q)
#     print(" ".join(filtered_list))


# function to return results for all queries
check_queries(
    queries
)  # Function to evaluate whether given query is gibberish or not with optional arg to to use your own model
