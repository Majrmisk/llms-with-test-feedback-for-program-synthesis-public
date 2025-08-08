from generated_function import most_frequent_substring

def test_basic():
    assert most_frequent_substring("ababc", 2) == "aa"

def test_single_char():
    assert most_frequent_substring("a", 1) == "a"

def test_k_exceeds_length():
    assert most_frequent_substring("abc", 4) == ""

def test_empty_string():
    assert most_frequent_substring("", 1) == ""

def test_k_zero():
    assert most_frequent_substring("abc", 0) == ""

def test_tie_lex_smallest():
    assert most_frequent_substring("abba", 2) == "ab"

def test_tie_lex_smallest2():
    assert most_frequent_substring("baab", 2) == "aa"

def test_all_same():
    assert most_frequent_substring("aaaaa", 2) == "aa"

def test_alternating_pattern():
    assert most_frequent_substring("xyxyxyx", 3) == "xyx"

def test_full_string():
    s = "abcdef"
    assert most_frequent_substring(s, 6) == "abcdef"

def test_multiple_ties():
    s = "caccac"
    assert most_frequent_substring(s, 2) == "ac"

def test_large_string_pattern():
    s = ("ab" * 10000) + ("ba" * 10000) + "ab"
    assert most_frequent_substring(s, 2) == "ab"

def test_normal_sentence():
    s = "the quick brown fox jumps over the lazy dog"
    assert most_frequent_substring(s, 3) == "the"

def test_long_paragraph():
    s = "In today's rapidly evolving digital landscape, the convergence of technology and society has sparked profound changes across every facet of human life, from the way we communicate and work to how we learn and solve complex global challenges. With the advent of artificial intelligence, machine learning, and ubiquitous connectivity, traditional boundaries between physical and digital realms have blurred, paving the way for innovative solutions that were once the realm of science fiction. This transformation is evident in modern healthcare systems that leverage big data and predictive analytics to personalize treatment, as well as in smart cities where interconnected devices work in unison to optimize energy consumption and enhance public safety. Furthermore, the proliferation of remote work technologies has redefined professional environments, allowing teams to collaborate seamlessly across continents, thus fostering a truly global economy. However, these advancements also come with significant challenges, including the need to ensure data privacy, bridge the digital divide, and address the ethical implications of automated decision-making processes. As we navigate these uncharted territories, it becomes increasingly important to strike a balance between embracing innovation and maintaining a vigilant stance toward potential risks, thereby ensuring that technology serves as a tool for sustainable progress and the collective betterment of society."
    assert most_frequent_substring(s, 4) == "tion"
