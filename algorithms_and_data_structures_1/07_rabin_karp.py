class RabinKarp:

    def __init__(self):
        pass

    def search(self, pattern, text):
        """
            This method uses the RabinKarp algorithm to search a given pattern in a given input text.
            @ param pattern - The string pattern that is searched in the text.
            @ param text - The text string in which the pattern is searched.
            @ return a list with the starting indices of pattern occurrences in the text, or None if not found.
            @ raises ValueError if pattern or text is None or empty.
        """
        if pattern is None or len(pattern)==0 or text is None or len(text)==0:
            raise ValueError
        
        start_indices = []
        hash_p = self.get_rolling_hash_value(pattern, '0', 0)
        m = len(pattern)

        hash_t=0
        for i in range(len(text)-m+1):
            sequence = text[i:i+m]
            last_char = text[i-1] if i!=0 else '0'

            hash_t = self.get_rolling_hash_value(sequence, last_char, hash_t)

            if hash_t == hash_p:        
                brute_force_ok=True
                for j in range(m):
                    if sequence[j] != pattern[j]:
                        brute_force_ok=False
                if brute_force_ok:
                    start_indices.append(i)

        return start_indices if len(start_indices)!=0 else None

    @staticmethod
    def get_rolling_hash_value(sequence, last_character, previous_hash):
        """
            This method calculates the (rolling) hash code for a given character sequence. For the calculation use the 
            base b=29.
            @ param sequence - The char sequence for which the (rolling) hash shall be computed.
            @ param last_character - The character to be removed from the hash when a new character is added.
            @ param previous_hash - The most recent hash value to be reused in the new hash value.
            @ return hash value for the given character sequence using base 29.
        """
        b=29
        m=len(sequence)

        if previous_hash==0:
            h_i = 0
            j=1
            # x(i) = t[i]*b**(m-1) + t[i+1]*b**(m-2) + ... + t[i+m-1]
            for i in range(m):
                h_i += ord(sequence[i])*b**(m-j)
                j+=1
        else:
            # h(i) = h(i-1)*b – t[i-1] *(b**m) + t[i+m-1]
            h_i = previous_hash*b - ord(last_character)*(b**m) + ord(sequence[-1])

        return h_i

