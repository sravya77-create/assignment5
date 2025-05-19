# task2.py

def demonstrate_list_slicing():
    # Creating a list of numbers from 1 to 10
    numbers = list(range(1, 11))

    # Extracting the first five elements from the list
    first_five = numbers[:5]

    # Reversing these extracted elements
    reversed_first_five = first_five[::-1]

    # Printing both the extracted list and the reversed list
    print("First five elements:", first_five)
    print("Reversed first five elements:", reversed_first_five)

if __name__ == "__main__":
    demonstrate_list_slicing()
