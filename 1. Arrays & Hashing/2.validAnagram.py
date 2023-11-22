#neetCode
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT


#vsCode
import sys

class Solution:                                       #main logic
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}                      # creating hashmap

        for i in range(len(s)):
            #print(s)
           # print(countS)
            countS[s[i]] = 1 + countS.get(s[i], 0)     # we can access the value of a dictionary with the syntax dictionary[key]. In this case, the key is the character s[i]. So, the line countS[s[i]] is accessing the value of the dictionary countS for the key s[i]. 
            #print(s[i])
            print(countS)                              # so  countS[s[i]] = r for first iteration
                                                       # &  1 + countS.get(s[i], 0) = 1 . This tries to get the s[i] from the dictonary countS. 
            countT[t[i]] = 1 + countT.get(t[i], 0)
            print(countT)
        #print (countS == countT)
        return countS == countT                        #The return countS == countT line returns True if the two dictionaries countS and countT are equal. Otherwise, the function returns False
          
def main():                                            # logic for manual input
    s = input("Enter the first string: ")
    t = input("Enter the second string: ")

    solution = Solution()
    result = solution.isAnagram(s, t)

    if result:
        print("The two strings are anagrams.")
    else:
        print("The two strings are not anagrams.")

if __name__ == "__main__":
    main()
