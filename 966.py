# Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

# For a given query word, the spell checker handles two categories of spelling mistakes:

#     Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
#         Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
#         Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
#         Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
#     Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
#         Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
#         Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
#         Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)

# In addition, the spell checker operates under the following precedence rules:

#     When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
#     When the query matches a word up to capitlization, you should return the first such match in the wordlist.
#     When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
#     If the query has no matches in the wordlist, you should return the empty string.

# Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        result=[]
        worddict=set(wordlist)
        lowerlist={}
        vowellist={}
        for i in wordlist:
            lowered=i.lower()
            lowerlist.setdefault(lowered,i)
            vowellist.setdefault(lowered.replace('a','*').replace('e','*').replace('i','*').replace('o','*').replace('u','*'),i)
        for i in queries:
            if i in worddict:
                result.append(i)
            elif lowerlist.get(i.lower()) is not None:
                result.append(lowerlist[i.lower()])
            elif vowellist.get(i.lower().replace('a','*').replace('e','*').replace('i','*').replace('o','*').replace('u','*')) is not None:
                result.append(vowellist[i.lower().replace('a','*').replace('e','*').replace('i','*').replace('o','*').replace('u','*')])
            else:
                result.append("")
        return result
        #     vowelindices=[]
        #     for c in i:
        #         if c in "aeiouAEIOU":
        #             vowelindices.append(idx)
        #         idx+=1
        #     for j in wordlist:
        #         if i in j:
        #             result.append(j)
        #             break
        #         elif i.lower() in j.lower():
        #             result.append(j)
        #             break
        #         else:
        #             if (all(j[k] in "aeiouAEIOU" for k in vowelindices) and i.lower() == j.lower()):
        #                 result.append(i)
        #                 break
        #             else:
        #                 result.append("")
        # return result
