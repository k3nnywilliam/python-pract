
def sortAlienLanguage(words, order):

    '''
    We convert ascii values of each to integers and populate them into the alphabet list.
    Since we want to have a meaningful ascending integer values, we substract the ascii values
    with 'a'. This is because the respective ascii decimal values for 'a', 'b', 'c', and etc 
    correspond to 97, 98, 99 and so on.
    If we substract each with ascii value of 'a' (97), we will have an easier representation in integers 
    like 0, 1, 2, 3 instead of 97, 98, 99, 100. 
    '''
       
    alphabet = []

    for i in range(len(order)):
        alphabet.append(ord(order[i]) - ord('a'))

    return secondMethod(alphabet, words) #firstMethod(alphabet, words) 




def firstMethod(alphabet, words):
    '''
    First, we go through our words and compare i-th words to every other j-th words
    '''
    for i in range(len(words)):
       
        for j in range(i + 1, len(words)):
            '''
            Since the length of each word may vary, we need to make sure 
            to avoid out-of-bounds error as we traverse each k-th character 
            just in case there are shorter words than others. Therefore,
            we just take the minimum length from all of the words.
            '''
            minLength = min((len(words[i]), len(words[j])))

            '''
            Then we start comparing each characters from each words
            and return true if the characters' k-th positions are sorted
            according to the order of the alien language.
            '''

            for k in range(0, minLength):

                '''
                we check each k-th character from each i-th and j-th word
                and then compare each values according to its position in the alien alphabet
                '''
                ichar = words[i][k]
                jchar = words[j][k]

                if alphabet[ord(ichar) - ord('a')] < alphabet[ord(jchar) - ord('a')]:
                    break
                elif alphabet[ord(jchar) - ord('a')] < alphabet[ord(ichar) - ord('a')]:
                    return False
                    '''
                    Below, we compare to the point of last k-th characters, and if
                    the length of i-th word is longer than j-th word then it basically breaks 
                    the rule of the lexicography
                    '''
                elif k == minLength - 1 and len(words[i]) > len(words[j]):
                    return False
    
    return True


def secondMethod(alphabet, words):
    '''
    Second method removes the extra j loop by comparing words[i] and words[i +1]
    '''

    for i in range(1, len(words)):

        if compareWords(words[i - 1], words[i], alphabet) > 0:
            return False
        
    return True

def compareWords(firstWord, secondWord, alphabet):

    i = 0
    j = 0
    compare = 0

    ichar = firstWord[i]
    jchar = secondWord[j]

    while i < len(firstWord) and j < len(secondWord) and compare == 0:

        compare = (alphabet[ord(ichar) - ord('a')]) - (alphabet[ord(jchar) - ord('a')])

        i += 1
        j += 1

    if compare == 0:
        return len(firstWord) - len(secondWord)
    else:
        return compare
        

if __name__ == '__main__':

    '''
    This will return True because 'h' preceds 'l'
    '''
    words = ['hello', 'leetcode'] 
    order =  "hlabcdefgijkmnopqrstuvwxyz" 
    print(sortAlienLanguage(words, order)) 

    '''
    The following input would return False output because 
    the order in the alien alphabet says that 'l' precedes 'd', 
    so therefore this is not in the correct order of the alien lexicography
    '''
    words = ["word", "world", "row"] 
    order = "worldabcefgijkmnpqstuvxyz"
    print(sortAlienLanguage(words, order))

    '''
    This will return False because the length of i-th word
    is longer than j-th word
    '''
    words = ["apple", "app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    print(sortAlienLanguage(words, order))