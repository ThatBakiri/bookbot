from stats import word_count
from stats import character_count
from stats import sort_characters
import sys

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()

	return file_contents

def main():
	if len(sys.argv) > 1 and len(sys.argv) < 3:
		num_words = word_count(get_book_text(sys.argv[1]))
		characters = character_count(get_book_text(sys.argv[1]))
		sorted_characters = sort_characters(characters)
		sorted_characters.sort(key= lambda item: item[1], reverse = True)
		print("============ BOOKBOT ============")
		print(f"Analyzing book found at {sys.argv[1]}")
		print("----------- Word Count ----------")
		print(f"Found {num_words} total words")
		print("--------- Character Count -------")
		for key, value in sorted_characters:
			if key.isalpha():
				print(f"{key}: {value}")
		print("============= END ===============")
		sys.exit(0)
	else:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
main()
