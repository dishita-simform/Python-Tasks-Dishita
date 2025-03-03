def word_to_number(word):
    word_map = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", 
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    
    num_str = ""
    i = 0
    
    if word.startswith("minus"):
        return None  
    
    while i < len(word):
        key_list = list(word_map.keys())
        j = 0
        while j < len(key_list):
            key = key_list[j]
            if word[i:].startswith(key):
                num_str += word_map[key]
                i += len(key) - 1
                break
            j += 1
        i += 1
    
    return int(num_str) if num_str else None

def number_to_word(num):
    num_map = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    result = ""
    i = 0
    num_str = str(num)
    while i < len(num_str):
        result += num_map[int(num_str[i])]
        i += 1
        
    return result

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def compute_gcd(word1, word2):
    num1, num2 = word_to_number(word1), word_to_number(word2)
    
    if num1 is None or num2 is None or num1 <= 0 or num2 <= 0:
        return "Invalid Input. Please Enter Valid Positive Word Numbers"
    
    gcd_value = gcd(num1, num2)
    gcd_word = number_to_word(gcd_value)
    
    return (f"First Number: {word1} ({num1})\n"
            f"Second Number: {word2} ({num2})\n"
            f"GCD in Words: {gcd_word}\n"
            f"GCD in Number: {gcd_value}")

if __name__ == "__main__":
    word1 = input("Enter First Number in Words: ").strip().lower()
    word2 = input("Enter Second Number in Words: ").strip().lower()
    print(compute_gcd(word1, word2))
