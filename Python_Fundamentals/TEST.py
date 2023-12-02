#number_of_orders = int(input())
#total_price = 0
#for order in range(number_of_orders):
#    price_per_capsule = float(input())
#    days = int(input())
#    capsules_needed_per_day = int(input())
#    if not 0.01 <= price_per_capsule <= 100:
#        continue
#    if not 1 <= days <= 31:
#        continue
#    if not 1 <= capsules_needed_per_day <= 2000:
#        continue
#    price = days*(price_per_capsule*capsules_needed_per_day)
#    total_price += price
#    print(f"The price for the coffee is: ${price:.2f}")
#print(f"Total: ${total_price:.2f}")
#
#######################################################


#current_command = input()
#total_coffee_needed = 0
#while current_command != "END":
#    if current_command == "coding":
#        if str.isupper(current_command):
#            total_coffee_needed += 2
#        else:
#            total_coffee_needed += 1
#    elif current_command == "dog" or "cat":
#        if str.isupper(current_command):
#            total_coffee_needed += 2
#        else:
#            total_coffee_needed += 1
#    elif current_command == "movie":
#        if str.isupper(current_command):
#            total_coffee_needed += 2
#        else:
#            total_coffee_needed += 1
#    else:
#        continue
#if total_coffee_needed > 5:
#    print("You need extra sleep")
#else:
#    print(total_coffee_needed)
#    current_command = input()
#
###########################################################


#initial_string = input()
#
#final_list = []
#for i in range(len(initial_string)):
#    current_letter = initial_string[i]
#    if 65 <= ord(current_letter) <= 90:
#        final_list.append(i)
#
#print(final_list)
#

def decipher_message(secret_message):
    words = secret_message.split()

    deciphered_words = []
    for word in words:
        if len(word) >= 2:
            # Swap the second and last letters
            new_word = word[0] + word[-1] + word[2:-1] + word[1]
            # Replace the first letter with its character code
            first_letter_code = str(ord(word[0]))
            new_word = first_letter_code + new_word[1:]

            deciphered_words.append(new_word)
        else:
            # If the word has only one letter, keep it unchanged
            deciphered_words.append(word)

    deciphered_message = ' '.join(deciphered_words)
    return deciphered_message

# Example usage:
secret_message = input()
deciphered_message = decipher_message(secret_message)
print(deciphered_message)