# Load the text from files again to ensure accuracy
with open('/mnt/data/стаття 1.txt', 'r', encoding='utf-8') as file:
    article_1_content = file.read()

with open('/mnt/data/стаття 2.txt', 'r', encoding='utf-8') as file:
    article_2_content = file.read()

# Define substrings for search: one existing and one fabricated
existing_substring = "рекомендаційні системи"  # A substring that exists in the articles
fabricated_substring = "xyzabc123"  # A substring that does not exist in the articles

# Output the lengths of the articles to understand the scale
len(article_1_content), len(article_2_content)

# Re-implement the search algorithms with Unicode support

def kmp_search(text, pattern):
    lsp = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lsp[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        lsp[i] = j

    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lsp[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == len(pattern):
                return i - j + 1
        j = 0
    return -1

def rabin_karp_search(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    result = []

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                return i
        if i < n - m:
            t = (t - h * ord(text[i])) % q
            t = (t * d + ord(text[i + m])) % q
            t = (t + q) % q
    return -1

def boyer_moore_search(text, pattern):
    d = 256
    bad_char = [-1] * d
    for i in range(len(pattern)):
        bad_char[ord(pattern[i]) % d] = i

    shift = 0
    while shift <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1
        if j < 0:
            return shift
        shift += max(1, j - bad_char[ord(text[shift + j]) % d])
    return -1

# Time the search functions for both articles and both substrings
performance_results = {}
for name, func in search_methods.items():
    performance_results[name] = {}
    for article, content in [('article_1', article_1_content), ('article_2', article_2_content)]:
        for substring, value in [('existing', existing_substring), ('fabricated', fabricated_substring)]:
            duration = time_search(func, content, value)
            performance_results[name].setdefault(article, {})[substring] = duration

performance_results
