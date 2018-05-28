#######################################################################
# BruteGen
#
# Generate blocks of brute forced passwords.
# Usefull for enumerating a large wordlist in sections without writing it to disk.

# Version: 1.0r
# Author: Laurance Yeomans 2018
#######################################################################

class BruteGen:
    def __init__(self,min_len,max_len,charset):
        # add data validation for charset
        self.m_charset = charset
        self.m_set_last_c = charset[len(charset)-1] 
        self.m_set_first_c = charset[0]
        self.m_min = min_len
        self.m_max = max_len
        self.Reset()
        
    def Reset(self):
        self.m_first_run = True
        self.m_is_done = False
        self.m_wordlist = list()
        self.m_word = list()
        for i in range(0,self.m_min):
            self.m_word.append(self.m_set_first_c)

    def IsDone(self):
        return self.m_is_done

    def StartFrom(self,word):
        self.m_word = list()
        for c in word:
            self.m_word.append(c)

    def __inc_char(self,i):
        curr_c = self.m_word[i]
        if curr_c != self.m_set_last_c:
            index = 0
            for c in self.m_charset:
                if c == curr_c:
                    break
                index += 1
            self.m_word[i] = self.m_charset[index + 1]

    def __recursive_update(self,n):
        n = n - 1 # fixes indexing issues
        if n >= 0: 
            if self.m_word[n] == self.m_set_last_c:
                self.m_word[n] = self.m_set_first_c
                self.__recursive_update(n)
            else:
                self.__inc_char(n)

    def __update_word(self):
        word_len = len(self.m_word)

        all_last_c = True
        for c in self.m_word:
            if c != self.m_set_last_c:
                all_last_c = False

        if all_last_c:
            if word_len == self.m_max:
                self.m_is_done = True # Done!
            else:
               self.m_word = list()
               for i in range(0,word_len + 1):
                   self.m_word.append(self.m_set_first_c)
        else:
            self.__recursive_update(word_len)


    def __append_wordlist(self):
        word = ''
        for c in self.m_word:
            word = word + str(c)
        self.m_wordlist.append(word)

    #####
    # Get the next n words
    def Next(self,n):
        self.m_wordlist = []

        for i in range(0,n):
            if self.m_first_run == False:
                self.__update_word()
            else:
                self.m_first_run = False

            if self.m_is_done == True:
                break
            else:
                self.__append_wordlist()

        return self.m_wordlist