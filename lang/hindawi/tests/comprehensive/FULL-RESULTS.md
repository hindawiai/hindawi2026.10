# Full test results

## Coverage

76 languages × 9 Shailis = 684 combinations

## Results

| status | count |
|---|---|
| PASS | 679 |
| NO_UHIN | 5 |
| FLEX_FAIL | 0 |
| GCC_FAIL | 0 |

## Test method

1. flex -o scanner.c lang/shaili.uhin
2. gcc -o scanner scanner.c -lfl
3. Check exit code

## Missing

5 .uhin files not present (Hindi partial coverage in hindi/ directory).

## Date

2026-10-16
