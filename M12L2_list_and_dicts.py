import timeit
import sys

def list_of_squares(n):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return [i ** 2 for i in range(1, n + 1)]

def reverse_sublist(lst, i, j):
    """
    Time Complexity: O(j-i+1)
    Space Complexity: O(j-i+1)
    """
    lst[i:j + 1] = lst[i:j + 1][::-1]
    return lst

def merge_sorted_lists(list1, list2):
    """
    Time Complexity: O(n+m)
    Space Complexity: O(n+m)
    """
    merged = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    merged.extend(list1[i:])
    merged.extend(list2[j:])

    return merged

def merge_dicts(dict1, dict2):
    """
    Time Complexity: O(n+m)
    Space Complexity: O(n+m)
    """
    merged = dict1.copy()
    merged.update(dict2)
    return merged

def intersect_dicts(dict1, dict2):
    """
    Time Complexity: O(n)
    Space Complexity: O(k) where k is the number of common keys
    """
    return {key: dict1[key] for key in dict1 if key in dict2}

def count_word_frequencies(words):
    """
    Time Complexity: O(n)
    Space Complexity: O(u) where u is the number of unique words
    """
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

def measure_performance():
    # List of Squares
    n = 1000
    start_time = timeit.default_timer()
    result_squares = list_of_squares(n)
    time_squares = timeit.default_timer() - start_time
    space_squares = sys.getsizeof(result_squares)

    # Reverse Sublist
    lst = list(range(1, 1001))
    start_time = timeit.default_timer()
    result_reverse = reverse_sublist(lst, 200, 400)
    time_reverse = timeit.default_timer() - start_time
    space_reverse = sys.getsizeof(result_reverse)

    # Merge Sorted Lists
    list1 = list(range(1, 501))
    list2 = list(range(501, 1001))
    start_time = timeit.default_timer()
    result_merge = merge_sorted_lists(list1, list2)
    time_merge = timeit.default_timer() - start_time
    space_merge = sys.getsizeof(result_merge)

    # Merge Two Dictionaries
    dict1 = {i: f'val{i}' for i in range(1, 501)}
    dict2 = {i: f'val{i + 500}' for i in range(1, 501)}
    start_time = timeit.default_timer()
    result_merge_dicts = merge_dicts(dict1, dict2)
    time_merge_dicts = timeit.default_timer() - start_time
    space_merge_dicts = sys.getsizeof(result_merge_dicts)

    # intersection of Dictionaries
    dict1 = {i: f'val{i}' for i in range(1, 501)}
    dict2 = {i: f'val{i + 500}' for i in range(100, 600)}
    start_time = timeit.default_timer()
    result_intersection = intersect_dicts(dict1, dict2)
    time_intersection = timeit.default_timer() - start_time
    space_intersection = sys.getsizeof(result_intersection)

    # count Word Frequencies
    words = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    start_time = timeit.default_timer()
    result_word_freq = count_word_frequencies(words)
    time_word_freq = timeit.default_timer() - start_time
    space_word_freq = sys.getsizeof(result_word_freq)

    # print Results
    print("Task 1: List of Squares")
    print(f"Time: {time_squares:.6f} seconds, Space: {space_squares} bytes\n")

    print("Task 2: Reverse Sublist")
    print(f"Time: {time_reverse:.6f} seconds, Space: {space_reverse} bytes\n")

    print("Task 3: Merge Sorted Lists")
    print(f"Time: {time_merge:.6f} seconds, Space: {space_merge} bytes\n")

    print("Task 4: Merge Two Dictionaries")
    print(f"Time: {time_merge_dicts:.6f} seconds, Space: {space_merge_dicts} bytes\n")

    print("Task 5: Intersection of Two Dictionaries")
    print(f"Time: {time_intersection:.6f} seconds, Space: {space_intersection} bytes\n")

    print("Task 6: Count Word Frequencies")
    print(f"Time: {time_word_freq:.6f} seconds, Space: {space_word_freq} bytes\n")


if __name__ == "__main__":
    measure_performance()
