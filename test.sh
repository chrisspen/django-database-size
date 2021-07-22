#!/bin/bash
# Runs all tests.
set -e
VENV=.env
[ -d $VENV ] && . $VENV/bin/activate
./pep8.sh
export TESTNAME=; tox
