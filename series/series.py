def slices(series, length):
    output = []
    s_len = len(series)
    i = 0
    if not series or length <= 0 or length > s_len:
        raise ValueError("Invalid param")
    while i + length <= s_len:
        output.append(series[i:i+length])
        i += 1
    return output
