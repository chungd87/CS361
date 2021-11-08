from argparse import ArgumentParser

def get_args():
    """
    Argument parser for command line.
    :return: parsed arguments
    """
    parser = ArgumentParser()

    m_group = parser.add_mutually_exclusive_group()
    m_group.add_argument('-n', action='store_true', help='Call name generator.')
    m_group.add_argument('-s', action='store_true', help='Call stat generator.')

    # For name generation
    parser.add_argument('-fl', type=str, required=False, help='First letters of name.')
    parser.add_argument('-l', type=int, required=False, help='Length of name.')

    # For stat generation
    parser.add_argument('-t', type=str, required=False,
                        help='Method of stat generation. Either "drop" or "standard"')

    return parser.parse_args()
