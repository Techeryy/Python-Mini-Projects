# Python Mini Projects
A collection of my smaller Python algorithms in the style of mini-Python challenges.

## Contents
- <a href="#run-length-encoding">Run Length Encoding</a>

- <a href="#password-strength-checker">Password Strength Checker</a>

- <a href="#number-finder">Number Finder</a>

- <a href="#linear-search">Linear Search</a>

## Run Length Encoding
A simple run length encoding compression algorithm, which takes a string entered by the user and compresses it by replacing consecutive occurrences of a value with a count of how many times that value occurs consecutively and the value itself.

For example, if 'AAAAAAFFDDDDDCCCAEEEEEEEE' were to be entered by the user the algorithm would produce '6A2F5D3C1A8E', with the leading integer in a pair being the count and the following character being the value from the original string. 
```
Enter String: AAAAAAFFDDDDDCCCAEEEEEEEE
6A2F5D3C1A8E
```
<a href="Programs/Run-Length-Encoding.py">View Source Code</a>

## Password Strength Checker
A relatively simplistic password strength checker algorithm which takes a password input and provides a score based on its strength alongside any criteria which was not met. The password strength checks include length, case, special characters, numeric characters & a check against a selection of the most commonly used passwords.

For example, if the user were to enter their password as 'Nvidia26' they would receive a strength score of 80/100, as for each criteria which isn't met the strength score is reduced by 20 points, since the only criteria which wasn't met was the inclusion of special characters the password received a score of 100 - 20 = 80.
```
Please Enter A Strong Password: Nvidia26
Please Re-Enter Your Password: Nvidia26
Your password received an overall strength score of 80/100
This is considered a weak password, the following criteria were not met: Special Characters
```
<a href="Programs/Password-Strength-Checker.py">View Source Code</a>

## Number Finder
A simple algorithm to find a target within a large number even if the number is seperated by values not included within the target number.

For example, if the target value was '4567' and the number was '2983**47**9082**7**6**5**98**465**9832**45**09**6**8**7**32**645**9832**745**982**74**09**7**219**5**8**6**2' the algorithm would return True, since this value contains 4509687 the target value has been found & hence the program returns True.
```
True
```
<a href="Programs/Number-Finder.py">View Source Code</a>

## Linear Search
A python implementation of a linear search algorithm, where items are individually compared against an item being searched for.

For example, if you were searching for David in a list of names (James, Michael, Robert, John, David, William) the algorithm would iterate through the list and compare each item with the item to be found & would return True when David is found.
```
True
```
<a href="Programs/Linear-Search.py">View Source Code</a>