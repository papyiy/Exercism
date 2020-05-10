def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Not equally long")
    diff = 0
    for a,b in zip(strand_a, strand_b):
        if a!= b:
            diff += 1
    return diff
