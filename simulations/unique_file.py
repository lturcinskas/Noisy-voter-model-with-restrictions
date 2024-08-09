import itertools
import os

def unique_file(
        basename: str,
        ext: str,
):
    """ Determines unique file name.
    Input:
        basename - file name.
        ext - file extension.
    Output:
        a unique file name.
    """
    actualname = "%s.%s" % (basename, ext)
    c = itertools.count()
    while os.path.exists(actualname):
        actualname = "%s (%d).%s" % (basename, next(c), ext)
    return actualname