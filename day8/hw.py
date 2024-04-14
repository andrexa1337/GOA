# Prompt the user to input scores separated by spaces
scores_input = input("Enter your scores separated by spaces: ")

# Split the input string into a list of scores
scores_list = scores_input.split()

# Convert each score from string to float
scores_float = [float(score) for score in scores_list]

# Calculate the arithmetic mean (average) of the scores
mean_score = sum(scores_float) / len(scores_float)

# Print the arithmetic mean
print("The arithmetic mean of your scores is:", mean_score)
