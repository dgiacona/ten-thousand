# LAB - (06)
## Project: Ten Thousand (v. 1.0)
#### Author: Dominic Giacona
<hr>
Command line version of the dice game, 'Ten Thousand.'
Expanding understanding of Python standard library.
<hr>
### Links and Resources
- back-end server url: (N/A)
- front-end application: (N/A)
### Setup
<!-- .env requirements (where applicable) -->
- Pytest
<!--
- PORT - Port Number
- DATABASE_URL - URL to the running Postgres instance/db -->
- How to initialize/run your application (where applicable) e.g. python main.py
  - `ten_thousand/game_logic.py`
  - `pytest`
    - `test_calculate_score.py`
    - `test_roll_dice.py`
- How to use your library (where applicable)
- Tests
  - How do you run tests?
    - Pytest (ptw)
  - Any tests of note?
    - Calculate score tests all pass
        zilch - roll with no scoring dice should return 0
        ones - rolls with various number of 1s should return correct score
        twos - rolls with various number of 2s should return correct score
        threes - rolls with various number of 3s should return correct score
        fours - rolls with various number of 4s should return correct score
        fives - rolls with various number of 5s should return correct score
        sixes - rolls with various number of 6s should return correct score
        straight - 1,2,3,4,5,6 should return correct score
        three_pairs - 3 pairs should return correct score
        two_trios - 2 sets of 3 should return correct score
        leftover_ones - 1s not used in set of 3 (or greater) should return correct score
        leftover_fives - 5s not used in set of 3 (or greater) should return correct score
    - `calculate_score()` function in code uses loops that work beyond the hard-coded tests provided.
  - Describe any tests that you did not complete, skipped, etc
    - As of time of writing I have not completed any of the stretch goals yet.