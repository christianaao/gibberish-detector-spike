from nostril import nonsense

# list of queries
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


# function to return results for all queries
def check_queries(query_object):
    """
    Function to evaluate whether given query is gibberish or not

    Args

        takes an dictionary of list of queries

    Returns

        String confirming if library evaluated the query to True (i.e. it is a gibberish query) or False (it is a real query)
    """

    # accessing both the key and value items (everything in the query list) from the query object
    for query_list_name, list in query_object.items():
        for q in list:
            try:
                if nonsense(q):
                    print(
                        f"{query_list_name.upper()} {q} evaluated to TRUE: Query deemed to be NONESENSE"
                    )
                else:
                    print(
                        f"{query_list_name.upper()} {q} evaluated to FALSE: Query deemed to be REAL"
                    )
            except ValueError:
                print(f"{query_list_name.upper()} {q} was deemed to be TOO SHORT")


check_queries(queries)
