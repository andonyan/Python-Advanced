def get_repeating_DNA(text):
    text_length = len(text)
    subsequences_list = []

    if text_length <= 10:
        return subsequences_list

    else:
        for i in range(text_length - 10):
            match_pattern = text[i:i + 10]
            for k in range(i + 1, text_length - 9):
                inner_sequence = text[k: k + 10]
                if match_pattern == inner_sequence and match_pattern not in subsequences_list:
                    subsequences_list.append(match_pattern)
        else:
            return subsequences_list


a = input()
print(get_repeating_DNA(a))
