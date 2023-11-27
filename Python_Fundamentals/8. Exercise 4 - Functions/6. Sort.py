####### First Way without function #######
#sequence_of_numbers = list(map(int, input().split()))
#print(sorted(sequence_of_numbers))





###### SECOND WAY WITH FUNCTION ####

def sorted_sequence(given_sequence):
    return sorted(given_sequence)

sequence_of_numbers = list(map(int, input().split()))
print(sorted_sequence(sequence_of_numbers))
