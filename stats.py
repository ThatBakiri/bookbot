def word_count(file_contents):
        text = file_contents.split()
        word_count = 0
        for word in text:
                word_count += 1

        return word_count

def character_count(file_contents):
	characters = {}
	text = file_contents.lower()
	for character in text:
		if character in characters:
			characters[character] += 1
		else:
			characters[character] = 1

	return characters

def sort_characters(my_dict):
	my_list = list(my_dict.items())
	return my_list


