#!/bin/bash

#  python unit tests
python3 /app/tests/test_transform.py

# exit code (0 = success, 1 = fail)
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo "Task Completed Successfully"
else
    echo "Task Failed"
fi

exit $EXIT_CODE