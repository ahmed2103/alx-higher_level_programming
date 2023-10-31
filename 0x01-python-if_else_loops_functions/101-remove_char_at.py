def remove_char_at(input_str, n):
    if 0 <= n < len(input_str):
        result = ""
        for i in range(len(input_str)):
            if i != n:
                result += input_str[i]
        return result
    return input_str
