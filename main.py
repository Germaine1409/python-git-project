# print("--- MISSION 1: Break the Cipher Lock ---")
print()
# Prompt the user to enter an encrypted message
message = input("Enter your encrypted message: ")

# Variable to store the count of vowels
vowel_count_1 = 0

# Loop through each character in the message
for char in message:
    # Convert the character to lowercase
    char = char.lower()

    # Check if the character is a vowel
    if char in "aeiou":
        vowel_count_1 += 1

# Display the total number of vowels found
print("Vowels detected:", vowel_count_1)
print()
# Prompt the user to enter an encrypted message
message = input("Enter your encrypted message: ")

# Variable to store the count of vowels
vowel_count_2 = 0

# Loop through each character in the message
for char in message:
    # Convert the character to lowercase
    char = char.lower()

    # Check if the character is a vowel
    if char in "aeiou":
        vowel_count_2 += 1

# Display the total number of vowels found
print("Vowels detected:", vowel_count_2)
print()
# Prompt the user to enter an encrypted message
message = input("Enter your encrypted message: ")

# Variable to store the count of vowels
vowel_count_3 = 0

# Loop through each character in the message
for char in message:
    # Convert the character to lowercase
    char = char.lower()

    # Check if the character is a vowel
    if char in "aeiou":
        vowel_count_3 += 1

# Display the total number of vowels found
print("Vowels detected:", vowel_count_3)
print()
# Prompt the user to enter an encrypted message
message = input("Enter your encrypted message: ")

# Variable to store the count of vowels
vowel_count_4 = 0

# Loop through each character in the message
for char in message:
    # Convert the character to lowercase
    char = char.lower()

    # Check if the character is a vowel
    if char in "aeiou":
        vowel_count_4 += 1

# Display the total number of vowels found
print("Vowels detected:", vowel_count_4)
#Get the encrypted message
message = input("Enter your encrypted message: ")

# Count vowels
vowel_count = 0

for char in message:
    char = char.lower()
    if char in "aeiou":
        vowel_count += 1

print(f"Vowels detected: {vowel_count}")
print()

# Get the number of rows for the diamond
num_rows = int(input("Enter the number of rows for the diamond: "))

# Upper half
for i in range(1, num_rows + 1):
    print(" " * (num_rows - i) + "*" * (2 * i - 1))

# Lower half
for i in range(num_rows - 1, 0, -1):
    print(" " * (num_rows - i) + "*" * (2 * i - 1))