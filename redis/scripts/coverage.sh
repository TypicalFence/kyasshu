# /usr/bin/env bash
python -m coverage run --source kyasshu_redis -m py.test
coverage report
