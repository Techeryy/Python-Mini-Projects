# Python Mini Projects
A collection of my smaller Python algorithms in the style of mini-Python challenges.

## Run Length Encoding
A simple run length encoding compression algorithm, which takes a string entered by the user and compresses it by replacing consecutive occurrences of a value with a count of how many times that value occurs consecutively and the value itself.

For example, if 'AAAAAAFFDDDDDCCCAEEEEEEEE' were to be entered by the user the algorithm would produce '6A2F5D3C1A8E', with the leading integer in a pair being the count and the following character being the value from the original string. 
```
Enter String: AAAAAAFFDDDDDCCCAEEEEEEEE
6A2F5D3C1A8E
```
<a href="Programs/Run-Length-Encoding.py">View Source Code</a>

## Number Finder
A simple algorithm to find a target within a large number even if the number is seperated by values not included within the target number.

For example, if the target value was '4567' and the number was '2983**47**9082**7**6**5**98**465**9832**45**09**6**8**7**32**645**9832**745**982**74**09**7**219**5**8**6**2' the algorithm would return True, since this value contains 4509687 the target value has been found & hence the program returns True.
```
True
```
<a href="Programs/Number-Finder.py">View Source Code</a>