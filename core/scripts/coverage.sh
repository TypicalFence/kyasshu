# /usr/bin/env bash
python -m coverage run --source kyasshu -m py.test
coverage report
