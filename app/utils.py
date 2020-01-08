
def dedupe_list(l):
    """Removes duplicates while preserving order."""
    return list(dict.fromkeys(l))
