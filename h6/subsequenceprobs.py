#A few optimal subsequence problems
#1. find longest bitonic subsequence
#2. find longest oscillating subsequence

def longestbitonicsubseq(input_values):
    n = len(input_values)
    if n == 0:
        return 0

    # longest bitonic subsequence
    inc_len = [1] * n  # inc_len[i]: LIS length ending at i
    for i in range(n):
        for j in range(i):
            if input_values[j] < input_values[i]:
                if inc_len[j] + 1 > inc_len[i]:
                    inc_len[i] = inc_len[j] + 1

    dec_len = [1] * n  # dec_len[i]: LDS length starting at i
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if input_values[j] < input_values[i]:
                if dec_len[j] + 1 > dec_len[i]:
                    dec_len[i] = dec_len[j] + 1

    longest_bitonic = 0
    for i in range(n):
        current_length = inc_len[i] + dec_len[i] - 1
        if current_length > longest_bitonic:
            longest_bitonic = current_length

    return longest_bitonic


def longestoscsubseq(input_values):
    n = len(input_values)
    if n == 0:
        return 0

    # longest oscillating subsequence
    up_end = [1] * n    # ends at i with last comparison "up"
    down_end = [0] * n  # ends at i with last comparison "down"

    for i in range(n):
        for j in range(i):
            if input_values[j] < input_values[i]:
                # either start the first "up" or continue after a "down"
                candidate = max(2, down_end[j] + 1)
                if candidate > up_end[i]:
                    up_end[i] = candidate
            elif input_values[j] > input_values[i] and up_end[j] >= 2:
                # can only go "down" after already having an "up"
                candidate = up_end[j] + 1
                if candidate > down_end[i]:
                    down_end[i] = candidate

    longest_oscillating = 0
    for i in range(n):
        longest_oscillating = max(longest_oscillating, up_end[i], down_end[i])

    return longest_oscillating


if __name__ == '__main__':
    # get user input
    input_string = input().strip()
    input_values = list(map(int, input_string.split()))

    # Display the input for debugging
    print("Input sequence:", input_string)
    print()

    # Compute both results using DP
    bitonic_length = longestbitonicsubseq(input_values)
    oscillating_length = longestoscsubseq(input_values)

    # Display results
    print("Longest Bitonic Subsequence length:", bitonic_length)
    print("Longest Oscillating Subsequence length:", oscillating_length)
