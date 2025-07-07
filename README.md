# C++ Unit Test Generator with LLMs

## Approach
- Used Ollama to run Llama 3 locally for generating and refining unit tests.
- Provided strict YAML instructions to ensure correct and non-redundant tests.
- Integrated Google Test for unit testing and GNU tools for coverage analysis.

## Results
- All functions in main.cpp are covered by unit tests.
- Achieved 85% line coverage (see coverage.info for details).
- Iteratively fixed build and test issues using LLM feedback.

## Challenges
- Initial tests missed some edge cases; resolved by refining prompts and reviewing coverage.
- Build issues due to missing includes were fixed with LLM-assisted debugging.

## How to Run
1. Install dependencies as described.
2. Run `g++ --coverage -o test_main test_main.cpp main.cpp -lgtest -lpthread`.
3. Execute `./test_main` and check coverage with `gcovr -r .`.

