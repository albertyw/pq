# pq
[jq](https://github.com/stedolan/jq) or [rq](https://github.com/dflemstr/rq) for parentheses.

This is a utility that when fed a datastructure of parentheses through STDIN,
will validate that parentheses are properly closed and then format the data
using newlines and indentation and output through STDOUT.  It also optionally
accepts arguments to select subsets of data similar to jq.

The goal is to write this in multiple languages, starting in python.
