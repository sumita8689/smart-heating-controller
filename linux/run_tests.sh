#! /bin/bash
echo "Starting automated tests..."
pytest

TEST_RESULT=$?
if [ $TEST_RESULT -eq 0 ]; then
	echo "All tests passed."
else
	echo "Tests failed."
fi

