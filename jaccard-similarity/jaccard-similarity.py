def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    a=set(set_a)
    b=set(set_b)

    intersection=len(a & b)
    union=len(a|b)

    if union==0:
        return 0.0

    return intersection/union
    