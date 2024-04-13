################################
# Pema Yeshi Dorji
# Electrical Department, Year 1
# 02230071
################################
# No external references used
################################
# SOLUTION
# Your Solution Score:
# 
################################
# Read the input.txt file
def read_input(file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
def calculate_score(input_lines):
    Total_sum = 0
    for line in input_lines:
        opponent, outcome = line.split()
        if outcome == 'X':
            # To lose we shall choose shape that beats opponents shape:
            if opponent == 'A':
                Total_sum += 1 + 6  # Rock > Sissor
            elif opponent == 'B':
                Total_sum += 2 + 3  # Paper == Paper
            elif opponent == 'C':
                Total_sum += 3 + 0  # Scissors lose to  Rock
        elif outcome == 'Y':
            #  To Draw User Chioice should be equal to Opponents choice
            if opponent == 'A':
                Total_sum += 1 + 3  # Rock == Rock
            elif opponent == 'B':
                Total_sum += 2 + 3  # Paper draws with Paper
            elif opponent == 'C':
                Total_sum += 3 + 3  # Scissors draws with Scissors
        elif outcome == 'Z':
            # You need to win, so choose the shape that loses to your opponent's choice
            if opponent == 'A':
                Total_sum += 1 + 0  # Rock < Paper
            elif opponent == 'B':
                Total_sum += 2 + 0 # Paper < Scissors
            elif opponent == 'C':
                Total_sum += 3 + 6  # Scissors < Paper
        else:
            print("Input Invaild")
    print(f"The total score is: {Total_sum}") #Printing the total score using f-string.

# Run the program
if __name__ == "__main__":
    file_name = "CSF101-CAP/input_1_cap1.txt"  # Initializing the file va;ue for the variable 
    input_lines = read_input(file_name) #reading the file for implentation
    if input_lines:
        calculate_score(input_lines)