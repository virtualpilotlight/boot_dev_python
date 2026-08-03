def merge(dict1, dict2):
    merged = {}
    for  k, v in dict1.items():
        merged[k] = v

    for k, v in dict2.items():
        merged[k] = v
    return merged
