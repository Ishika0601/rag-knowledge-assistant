def hit_at_k(docs, expected_terms):
    hits = 0
    for term in expected_terms:
        if any(term.lower() in d.page_content.lower() for d in docs):
            hits += 1
    return hits / len(expected_terms)
