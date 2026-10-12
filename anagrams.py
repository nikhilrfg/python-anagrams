str_1 = input("Enter the first string: ")
str_2 = input("Enter the second string: ")

strx_1 = ''.join(sorted(list(str_1.upper().replace(' ',''))))
strx_2 = ''.join(sorted(list(str_2.upper().replace(' ',''))))
if len(strx_1) > 0 and strx_1 == strx_2:
	print("Anagrams")
else:
	print("Not anagrams")

# Lab 2.5.8 - Anagrams
#
# Purpose:
# Check whether two strings are anagrams.
#
# Assumptions:
# 1. The user enters two separate strings.
# 2. Two empty strings are not considered anagrams.
# 3. Uppercase and lowercase letters are treated equally.
# 4. Spaces are ignored when comparing the strings.
# 5. Both strings must contain exactly the same characters
#    with the same number of occurrences.
#
# Tracing:
# 1. Ask the user to enter the first string.
# 2. Ask the user to enter the second string.
# 3. Convert both strings to uppercase.
# 4. Remove spaces from both strings.
# 5. Convert each string into a list of characters.
# 6. Sort the characters alphabetically.
# 7. Join the sorted characters back into strings.
# 8. Check that the first processed string is not empty.
# 9. Compare the two processed strings.
# 10. Print "Anagrams" if they match.
# 11. Otherwise, print "Not anagrams".
