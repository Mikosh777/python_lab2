print("Task 1")
#№,1
# Define the sequence of numbers as a list
sequence = [4, 8, 15, 16, 23, 42]

try:
    # Use formatted output (f-string) to print the sequence with spaces
    output = ' '.join(map(str, sequence))
    print(output)
except Exception as e:
    # Handle exceptions, if any
    print(f"An error occurred: {e}")
    
   # 1,2
# Define the sequence of numbers as a list
sequence = [4, 8, 15, 16, 23, 42]

try:
    # Iterate through the sequence and print each number on a separate line
    for number in sequence:
        print(number)
except Exception as e:
    # Handle exceptions, if any
    print(f"An error occurred: {e}")

#1,3
try:
    # Get the first number from the user
    first_number = int(input("Enter the first number: "))
    
    # Calculate and print the next two consecutive numbers
    print(first_number)
    print(first_number + 1)
    print(first_number + 2)
except ValueError:
    print("Invalid input. Please enter an integer.")
except Exception as e:
    print(f"An error occurred: {e}")
    
    #1,4
try:
    # Get three integers from the user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    
    # Calculate and display their sum
    total = num1 + num2 + num3
    print(total)
except ValueError:
    print("Invalid input. Please enter integers.")
except Exception as e:
    print(f"An error occurred: {e}")

#1,5
try:
    # Get the edge length from the user
    edge_length = float(input("Enter the edge length of the cube: "))
    
    # Calculate the volume and surface area
    volume = edge_length ** 3
    surface_area = 6 * (edge_length ** 2)
    
    # Display the results
    print(f"Volume = {int(volume)}")
    print(f"Total surface area = {int(surface_area)}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
except Exception as e:
    print(f"An error occurred: {e}")





                                        #TAsk 2
print("Task 2")
                                        
try:
    N = int(input("Enter the number of schoolchildren: "))
    K = int(input("Enter the number of tangerines: "))
    
    # Calculate how many tangerines each student gets and the remainder
    students_share = K // N
    remaining_tangerines = K % N
    
    # Display the results using formatted output
    print(f"Each student gets: {students_share}")
    print(f"Remaining tangerines in the basket: {remaining_tangerines}")
except ValueError:
    print("Invalid input. Please enter integers.")
except ZeroDivisionError:
    print("Number of schoolchildren cannot be zero.")
except Exception as e:
    print(f"An error occurred: {e}")

try:
    # Get the four-digit number from the user
    number = int(input("Enter a four-digit number: "))
    
    # Extract and display the digits using formatted output
    thousands = number // 1000
    hundreds = (number // 100) % 10
    tens = (number // 10) % 10
    units = number % 10
    
    print(f"The digit in the thousands position is {thousands}")
    print(f"The digit in the hundreds position is {hundreds}")
    print(f"The digit in the tens position is {tens}")
    print(f"The digit in the position of units is {units}")
except ValueError:
    print("Invalid input. Please enter a four-digit integer.")
except Exception as e:
    print(f"An error occurred: {e}")

try:
    # Get the population from the user
    population = int(input("Enter the population of the universe: "))
    
    # Calculate the number of survivors based on whether the population is even or odd
    if population % 2 == 0:
        survivors = population // 2
    else:
        survivors = (population // 2) + 1
    
    # Display the number of survivors
    print(f"Number of survivors: {survivors}")
except ValueError:
    print("Invalid input. Please enter an integer.")
except Exception as e:
    print(f"An error occurred: {e}")

try:
    # Get a number from the user
    number = int(input("Enter a number: "))
    result = number << 1
    
    if result == 0:
        print("Warning: The result is zero.")
    else:
        print(f"The result of << is {result}")
except ValueError:
    print("Invalid input. Please enter an integer.")
except Exception as e:
    print(f"An error occurred: {e}")
