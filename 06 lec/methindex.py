animals = ["cat", "dog", "rabbit", "hanster", "dog", "parrot",]
first_dig_index = animals.index("dog")
print(f"The first occurrence of 'dog' is at index: {first_dig_index}")

second_dig_index = animals.index("dog", first_dig_index + 1)
print(f"The second occurrence of 'dog' is at index: {second_dig_index}")