# EC602 Track 1 Checkpoint

Xuanyang Wang | Individual project | [python-dotenv issue #494](https://github.com/theskumar/python-dotenv/issues/494)

## Build and test results

| Check | Result from my fork |
| --- | --- |
| Python version (`python --version`) | `Python 3.14.4` |
| Source commit before adding the test (`git rev-parse HEAD`) | `4fbc6ff07215367ece731006855e732d1405992c` |
| Build (`python -m build --wheel`) | `Successfully built python_dotenv-1.2.4-py3-none-any.whl` |
| Original suite (`python -m pytest -q` before adding the test) | `291 passed, 1 skipped, 32 warnings in 1.43s` |
| New test (`python -m pytest -q tests/test_find_dotenv_start_dir.py`) | `TypeError: find_dotenv() got an unexpected keyword argument 'dir'`<br>`1 failed in 0.02s` |

## Reproduction

The test creates two `.env` files in a temporary directory. One is in the working directory and one is in its `project` subdirectory. It calls `find_dotenv(dir=...)` with `project/src` as the starting point. The expected result is the path to `project/.env`, with the working directory still at the temporary directory. The current implementation rejects `dir` before it starts searching.

## Fix plan

I plan to add an optional `dir` argument that accepts a string or a `pathlib.Path`. When a caller supplies it, `find_dotenv()` will start its existing search through parent directories from that location. Calls that omit `dir` will use the current rules for selecting a starting point. I will run the new test, check relative and absolute paths and missing files, and rerun the original suite.

## Changes since the proposal

The proposal described a test with a `.env` file above the starting directory. The checkpoint test adds a second `.env` file in the working directory. If the search starts there by mistake, it finds a different file, and the path assertion catches the error.
