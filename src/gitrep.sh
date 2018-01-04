#!/usr/bin/env bash
echo Ahead:
git for-each-ref --format="    %(refname:short) %(upstream:track)" refs/heads | grep ahead
echo
echo Behind:
git for-each-ref --format="    %(refname:short) %(upstream:track)" refs/heads | grep behind
echo

