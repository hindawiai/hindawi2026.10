# The GATE programs

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

`samples/gate/` holds teaching programs for the programming side of the GATE Computer Science and Information
Technology paper. Each is written once, in English and in C (the paper's programming language), and BURP puts it into
every language. `hindawi gate --langs L` compiles each C program from language L through the original pipeline, runs
it, and checks that it prints exactly what the English original prints; it also reverses every file byte for byte.

The map below follows the ten sections of the GATE 2027 CS syllabus published by IIT Madras (read 18 October 2026).
Topics are described in our own words; the syllabus text itself is not reproduced. Three sections changed for 2027
(Digital Logic, Computer Organisation and Architecture, Computer Networks); the map follows the 2027 version. General
Aptitude has no programs. The new 2027 paper in Robotics and Automation needs its own set and is not started.

## What is covered

Every topic of the ten sections that a program can show has one: 113 C programs, plus Python, Java, C++ and BASIC
programs in `samples/gate/paradigms/` for the other paradigms.

| Section | Programs |
|---|---|
| Engineering mathematics | discrete: `truth_table`, `relation_properties`, `group_axioms`, `graph_colouring`, `bipartite_matching`, `recurrence_table`, `permutations`, `sieve_of_eratosthenes`; linear algebra: `gaussian_elimination`, `lu_decomposition`, `power_iteration`; calculus: `finite_differences`, `golden_section`, `simpson_integration`; probability and statistics: `statistics`, `bayes_theorem`, `binomial_poisson`, `distribution_sampling` |
| Digital logic | `quine_mccluskey` (tabular minimisation), `sequence_detector` (a state machine), `ripple_carry_adder`, `gray_code`, `twos_complement_fixed_point`, `floating_point` |
| Computer organisation and architecture | `addressing_modes`, `alu_flags`, `microprogrammed_control`, `cache_mapping`, `memory_access_time`, `pipeline_hazards`, `interrupt_dma` |
| Programming and data structures | `recursion_fibonacci`, `gcd_and_lcm`, `pointers_and_arrays`, `structures_and_unions`, `preprocessor_macros`; `stack`, `circular_queue`, `linked_list`, `binary_search_tree`, `tree_traversals`, `min_heap`, `hash_table`, `adjacency_list` |
| Algorithms | sorting: `quick_sort`, `merge_sort`, `heap_sort`, `insertion_sort`; `binary_search`; greedy: `activity_selection`, `fractional_knapsack`, `huffman_code_lengths`; dynamic programming: `knapsack_01`, `longest_common_subsequence`, `edit_distance`, `matrix_chain`; divide and conquer: `towers_of_hanoi`, `maximum_subarray`; `n_queens`; graphs: `breadth_first_search`, `depth_first_search`, `dijkstra`, `floyd_warshall`, `topological_sort`, `kruskal`, `prim`; analysis: `growth_rates` |
| Theory of computation | `dfa_divisible_by_three`, `nfa_simulation`, `regex_matcher`, `pda_anbn`, `cyk_parsing`, `turing_machine` |
| Compiler design | `tokenizer`, `recursive_descent_parser`, `infix_to_postfix`, `rpn_evaluator`, `activation_records`, `three_address_code`, `constant_folding`, `liveness_analysis`, `common_subexpression` |
| Operating systems | `fork_wait`, `threads_mutex`, `pipe_ipc`, `producer_consumer`, `cpu_scheduling`, `round_robin`, `bankers_algorithm`, `paging_translation`, `lru_page_replacement`, `disk_scheduling`, `inode_blocks` |
| Databases | `relational_algebra`, `hash_join`, `attribute_closure`, `candidate_keys`, `conflict_serializability`, `bplus_tree_order` |
| Computer networks | `delay_throughput`, `crc32`, `internet_checksum`, `aloha_efficiency`, `distance_vector`, `link_state`, `ip_fragmentation`, `cidr`, `nat_table`, `sliding_window`, `tcp_congestion`, `socket_pair`, `dns_name_encoding`, `http_request` |

What no C program shows is taught in prose: pumping lemmas and undecidability, the ER model, and SQL itself (which
needs a database engine rather than C). The new 2027 paper in Robotics and Automation needs its own set.

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

Paste this, followed by the topics to write (more practice programs for a section, or the first set for the
Robotics and Automation paper):

> Write teaching programs for the GATE Computer Science paper, one C file per topic I list. Each file: a one-line
> comment saying what it shows; self-contained C99 under forty lines; compiles with `gcc -O2 -Wall` with no warnings
> and at most `-lm`; reads no input, keeps its data in the program, prints a short deterministic result and returns 0.
> The output must not depend on the order in which function arguments are evaluated, on addresses, on time or on
> threads; never call two functions with side effects inside one printf. Use whole English words in snake_case for
> every name (values, count, index, left, right, queue, distance), no abbreviations except gcd and crc, no single
> letters except in mathematics. Strings and comments in English. Give each file as a code block headed by its path,
> `samples/gate/<section>/<topic>.c`, and after all the files, list every distinct word used in the names.

Then add the files, give the listed words their entries in the glossary, and run `hindawi gate` and `hindawi coverage`.
