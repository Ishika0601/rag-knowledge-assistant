# RAG Experiments & Observations

This document captures experiments conducted to evaluate and tune the
Retrieval-Augmented Generation (RAG) system.

---

## Experiment 1: Retrieval Depth (Top-K)

**Goal:**  
Determine the optimal number of retrieved chunks that balances
accuracy and latency.

**Method:**  
- Fixed chunk size at 500
- Varied k = {3, 5, 7}
- Measured hit@k, faithfulness, and latency

| k | hit@k | Faithful Answers | Avg Latency |
|---|------|------------------|-------------|
| 3 | 0.68 | 82% | 0.94s |
| 5 | 0.82 | 90% | 1.18s |
| 7 | 0.85 | 91% | 1.42s |

**Observation:**  
Increasing k improved retrieval accuracy, but latency increased noticeably beyond k=5.

**Decision:**  
Selected **k = 5** as the optimal balance between accuracy and performance.

---

## Experiment 2: Chunk Size

**Goal:**  
Understand how chunk size impacts retrieval quality and answer grounding.

**Method:**  
- Fixed k = 5
- Varied chunk size = {300, 500, 800}

| Chunk Size | hit@k | Faithfulness |
|-----------|-------|--------------|
| 300 | 0.71 | 88% |
| 500 | 0.82 | 90% |
| 800 | 0.79 | 89% |

**Observation:**  
- Smaller chunks increased precision but reduced contextual completeness.
- Larger chunks introduced noise.

**Decision:**  
Selected **chunk size = 500** with overlap for optimal performance.

---

## Summary

- Retrieval accuracy is sensitive to both chunk size and retrieval depth.
- Prompt grounding combined with evaluation metrics effectively reduced hallucinations.
- Explicit experimentation helped avoid arbitrary configuration choices.
