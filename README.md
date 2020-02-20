# Wikirace
## General
Given two Wikipedia pages, wikirace will try to find a short path from one page to another using only links to other Wikipedia pages.
Wikirace will use live calculated data (i.e. no pre-calculated link graphs).

## Running
```
$ python3 wikirace.py "Stone Age" "Brian"
```
Example:
```
$ python3 wikirace.py "Stone Age" "Brian"
Stone Age
Brain
Brian
It takes 0 minutes and 27 seconds
```

## Improvements
I used a Breadth-First Search (BFS) but the fastest way will by change algorithm to Bidirectional Search