Title: Twitter/X thread blueprint — Collatz signatures

Thread outline (each line = one tweet):

1/ I published a repository with a structural, deterministic framework for the Collatz 3n+1 problem: signatures, exact densities, and computational verification. Link: https://github.com/andressetentay-design/Collatz-bajada-en-cascada

2/ The key idea: classify first-drops by signature (A odd steps, B divisions by 2) and compute exact densities for each signature class. This is not a heuristic: it produces rational densities and explicit formulas.

3/ The work contains 20 deterministic theorems describing allowed signature classes, block behaviors, and a modular (2-adic) balance that enforces descent.

4/ Computational verification: enumerated 1,879,048,192 integers in [2^28,2^30], and convergence logs up to P=107 (accumulated coverage 99.757853%).

5/ Repo: data, logs, and a reproducible Python script to reproduce convergence calculations.

6/ If you’re interested I can share notebooks and visualizations. Feedback welcome.
