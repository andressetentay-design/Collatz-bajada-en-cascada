Title: A deterministic approach to the Collatz conjecture: signatures, exact densities, and computational verification

Post for MathOverflow

Body:

I present a repository that develops a structural (non-probabilistic) framework for the Collatz 3n+1 map based on "signatures" (counts of odd operations and divisions by two), exact density formulas for first-drops, and a modular (2-adic) balance analysis. The work contains a system of 20 deterministic theorems describing allowed signature classes and their densities, accompanied by computational verification over large intervals [2^28,2^30] (1,879,048,192 integers) and detailed logs of convergence up to P=107.

Main claims and material included:
- Deterministic theorem system (20 theorems) describing signature classes and block balance
- Exact density derivations for first-drops (P up to >100, documented)
- Numerical verification data: data/verification_collatz_k28_k30.csv
- Convergence logs: logs/log_convergencia_p1_p107.txt
- Reproducible Python code: code/convergence_exact_calculation.py

What I seek from MathOverflow:
- Critical feedback on the conceptual framework and theorem statements
- Suggestions on gaps in proofs or references I might have missed
- Advice on preparing a formal write-up suitable for peer review or arXiv

Repository: https://github.com/andressetentay-design/Collatz-bajada-en-cascada

If you'd like, I can post a short summary of the principal theorems and definitions in a follow-up post.
