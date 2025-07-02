from stats import get_num_words
from stats import count_characters
from stats import sort_chars
import sys
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        wn = get_num_words(sys.argv[1])
        print(f"Found {wn} total words")
        print("--------- Character Count -------")
        cs = sort_chars(sys.argv[1])
        for c in cs:
            print(f"{c["char"]}: {c["num"]}")
            
main()