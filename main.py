import wiki_scrapper


def build_content_graph(_name: str, _lang: str, **kwargs):
    """
    This function builds a graph of the content of the wikipedia pages.
    :param _name: the name of the graph.
    :param _lang: the language of the pages.
    :param kwargs: the setup parameters.
    :return: the graph.
    """
    _setup_params = {}
    for key, value in kwargs.items():
        _setup_params[key] = value

    _setup_params['langs'] = [_lang]
    _setup_params['starting_points'] = [_name]
    _setup_params['content'] = True
    _save = True

    # using scrapper to build the graph
    _graph = wiki_scrapper.build_graph(False, _save, **_setup_params)
    print("Graph built\n\n")
    return _graph


def build_multilang_graph(_names, _langs, **kwargs):
    """
    This function builds a graph of the content of the wikipedia pages in multiple languages.
    :param _names: the name of the graph. (will take the first element)
    :param _langs: the languages of the pages.
    :param kwargs: the setup parameters.
    :return: the graph.
    """
    _setup_params = {}
    for key, value in kwargs.items():
        _setup_params[key] = value

    _setup_params['langs'] = _langs
    _setup_params['starting_points'] = _names

    _save = True

    # using scrapper to build the graph
    _graph = wiki_scrapper.build_graph(False, _save, **_setup_params)
    print("Graph built\n\n")
    return _graph


if __name__ == '__main__':
    LANGS = ["en", "es", "fr"]  # List of languages to use.

    # create a list of main subjects for different graph sizes.

    subjects = {100: ["Mathematics", "Mathématiques", "Matemáticas"],
                500: ["Physics", "Physique", "Física"],
                1000: ["Biology", "Biologie", "Biología"]}

    content_subjects = ['Greece', "book", "Chemistry", "education"]

    setup_params = {'langs': LANGS, 'starting_points': subjects[1000], 'max_pages_per_lang': 1000,
                    'removal_chance': 0, 'inversion_chance': 0, 'print_info': True, 'content': False, 'max_links': 10,
                    'format': 'csv'}
    save = True

    for subject in content_subjects:
        graph = build_content_graph(subject, 'en', **setup_params)
        for node in graph.nodes:
            print(f"{node}: {graph.nodes()[node]['content']}")
        print(f"Graph built\n\n")

    # test_subjects_1k = [['fire', 'fuego', "feu"],]
    # import random
    # for test_sub in test_subjects_1k:
    #     n_pages = random.choice(range(650, 1250))
    #     # n_pages = 10
    #     print(f"Building graph for {test_sub} with {n_pages} pages.")
    #     setup_params['max_pages_per_lang'] = n_pages
    #
    #     # build the graph
    #     graph = build_multilang_graph(test_sub, LANGS, **setup_params)

