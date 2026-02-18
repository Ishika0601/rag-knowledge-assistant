def is_faithful(answer: str, context: str) -> bool:
    key_sentences = answer.split(".")[:2]
    return all(s.strip().lower() in context.lower() for s in key_sentences if s.strip())
