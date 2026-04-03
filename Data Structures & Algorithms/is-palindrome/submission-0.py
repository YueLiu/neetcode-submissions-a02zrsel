import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        def process_string(input_string):
            # Convert to lowercase
            input_string = input_string.lower()
            # Remove all non-alphanumeric characters
            processed_string = re.sub(r'[^a-z0-9]', '', input_string)
            return processed_string
        
        text = process_string(s)

        L, R = 0, len(text) - 1

        while L < R:
            if text[L] != text[R]:
                return False
            L, R = L+1, R-1
        return True

        