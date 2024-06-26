# Python Mini Projects
A collection of my smaller Python algorithms in the style of mini-Python challenges.

## Run Length Encoding
A simple run length encoding compression algorithm, which takes a string entered by the user and compresses it by replacing consecutive occurrences of a value with a count of how many times that value occurs consecutively and the value itself.

For example, if 'AAAAAAFFDDDDDCCCAEEEEEEEE' were to be entered by the user the algorithm would produce '6A2F5D3C1A8E', with the leading integer in a pair being the count and the following character being the value from the original string. 
```
Enter String: AAAAAAFFDDDDDCCCAEEEEEEEE
6A2F5D3C1A8E
```
<a href="Run-Length-Encoding.py">View Source Code</a>