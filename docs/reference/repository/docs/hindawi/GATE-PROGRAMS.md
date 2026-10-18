# The GATE programs

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

`samples/gate/` holds teaching programs for the programming side of the GATE Computer Science and Information
Technology paper. Each is written once, in English and in C (the paper's programming language), and BURP puts it into
every language. `hindawi gate --langs L` compiles each C program from language L through the original pipeline, runs
it, and checks that it prints exactly what the English original prints; it also reverses every file byte for byte.

The map below follows the ten sections of the GATE 2027 CS syllabus published by IIT Madras (read 18 October 2026).
Topics are described in our own words; the syllabus text itself is not reproduced. Four sections changed for 2027
(Digital Logic, Computer Organisation and Architecture, Computer Networks); the map follows the 2027 version. General
Aptitude has no programs. The new 2027 paper in Robotics and Automation needs its own set and is not started.

## What is covered, and what is still to write

| Section | Programs now | Still to write |
|---|---|---|
| Engineering mathematics: discrete | `discrete_mathematics/permutations.c`, `sieve_of_eratosthenes.c` | truth table of a formula; properties of a relation; group axioms on Z_n; greedy graph colouring; bipartite matching; a recurrence solved by table |
| Engineering mathematics: linear algebra | `engineering_mathematics/gaussian_elimination.c` (system and determinant) | eigenvalue by power iteration; LU decomposition |
| Engineering mathematics: calculus | `engineering_mathematics/simpson_integration.c` | derivative and limit by finite differences; a minimum by golden-section search |
| Engineering mathematics: probability and statistics | `engineering_mathematics/statistics.c`, `bayes_theorem.c` | binomial and Poisson probabilities; uniform, normal and exponential sampled with a fixed generator |
| Digital logic | `digital_logic/gray_code.c`, `ripple_carry_adder.c`, `floating_point.c` | prime implicants by the tabular method; a counter as a state machine; two's complement and fixed point |
| Computer organisation and architecture | `computer_organization/cache_mapping.c`, `pipeline_hazards.c` | a small instruction set with addressing modes; an ALU with flags; a microprogrammed control sequencer; average memory access time; interrupt and DMA transfer counts |
| Programming and data structures | `programming/` (recursion, gcd, pointers, structures and unions), `data_structures/` (stack, circular queue, linked list, binary search tree, min-heap, hash table) | tree traversals in pre-, post- and level order; graphs as adjacency lists |
| Algorithms | `algorithms/` sorting (quick, merge, heap, insertion), searching, greedy (activity selection, fractional knapsack), dynamic programming (0/1 knapsack, LCS, edit distance, matrix chain), divide and conquer (Hanoi, maximum subarray), backtracking (N queens), graphs (BFS, DFS, Dijkstra, Floyd-Warshall, topological sort, Kruskal) | Prim; Huffman code lengths; counting operations to show growth rates |
| Theory of computation | `theory_of_computation/dfa_divisible_by_three.c`, `nfa_simulation.c`, `turing_machine.c` | a regular-expression matcher; a pushdown automaton for aⁿbⁿ; CYK parsing of a grammar in normal form. Pumping lemmas and undecidability are taught in prose |
| Compiler design | `compiler_design/tokenizer.c`, `recursive_descent_parser.c`, `rpn_evaluator.c`, `three_address_code.c` | infix to postfix by syntax-directed translation; activation records; constant folding and propagation; liveness; common subexpressions |
| Operating systems | `operating_systems/round_robin.c`, `bankers_algorithm.c`, `lru_page_replacement.c`, `paging_translation.c` | fork and wait; threads with a mutex; a pipe between processes; producer and consumer with semaphores; FCFS, SJF and priority scheduling; disk scheduling; inode block counts |
| Databases | `databases/hash_join.c`, `attribute_closure.c`, `conflict_serializability.c` | selection, projection and join as functions; candidate keys; B+ tree order and height. SQL needs SQLite and is outside C |
| Computer networks | `computer_networks/crc32.c`, `internet_checksum.c`, `cidr.c`, `distance_vector.c`, `tcp_congestion.c` | transmission and propagation delay; slotted ALOHA efficiency; link-state routing; IPv4 fragmentation; a NAT table; sliding-window flow control; a socket pair echo; DNS name encoding; parsing an HTTP request |

Python, Java, C++ and BASIC programs in `samples/gate/paradigms/` show the other paradigms; they ingest and reverse
exactly, and the C programs are the ones compiled from every language.

## The contract every program keeps

1. One self-contained C file under `samples/gate/<section>/<topic>.c`, one topic per program, with a one-line comment
   at the top saying what it shows. Under about forty lines.
2. It compiles with `gcc -O2 -Wall` without warnings, needing at most `-lm` (and `-lpthread` for threads).
3. It reads no input. Its data is in the program, its output goes to standard output, and it exits with 0.
4. Its output never depends on argument evaluation order, addresses, time, thread scheduling or an unseeded random
   generator. Two calls in one `printf` argument list are a defect.
5. Names are whole English words in snake_case (`values`, `count`, `left`, `queue`, `distance`), because names are
   translated word by word. Standard abbreviations (`gcd`, `crc`) are fine; single letters only for mathematics.
6. Strings and comments are in English. The output is compared with the English original's, character for character.
7. Every word a new name uses must have a column entry in `lang/hindawi/burp/glossary/multi.tsv` for each language
   there, marked as proposed. `hindawi coverage --langs L --missing` lists any word still without one.

A program is accepted when `hindawi gate --langs dari,pashto,urdu,punjabi,punjabi_shahmukhi,sindhi,telugu,kannada,sanskrit`
reports it compiled and matched in every language, and `hindawi coverage` reports the names complete.

## Instructions to give another AI

Paste this, followed by the topics to write from the table above:

> Write teaching programs for the GATE Computer Science paper, one C file per topic I list. Each file: a one-line
> comment saying what it shows; self-contained C99 under forty lines; compiles with `gcc -O2 -Wall` with no warnings
> and at most `-lm`; reads no input, keeps its data in the program, prints a short deterministic result and returns 0.
> The output must not depend on the order in which function arguments are evaluated, on addresses, on time or on
> threads; never call two functions with side effects inside one printf. Use whole English words in snake_case for
> every name (values, count, index, left, right, queue, distance), no abbreviations except gcd and crc, no single
> letters except in mathematics. Strings and comments in English. Give each file as a code block headed by its path,
> `samples/gate/<section>/<topic>.c`, and after all the files, list every distinct word used in the names.

Then add the files, give the listed words their entries in the glossary, and run `hindawi gate` and `hindawi coverage`.
