#!/bin/bash
# Run all tests using system Python

echo "Running Portfolio Project Tests..."

# Change to project root directory
cd "$(dirname "$0")/.."

# Add the app directory to Python path so tests can import modules
export PYTHONPATH="${PYTHONPATH}:$(pwd)/app"

# Run tests from the tests directory
python3 -m unittest discover -s tests -p "test_*.py" -v

echo "Tests completed."
