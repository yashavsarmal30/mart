import threading
import time

# Function to print numbers
def print_numbers():
    for i in range(1, 6):
        time.sleep(1)
        print(f"Number: {i}")

# Function to print letters
def print_letters():
    for letter in 'ABCDE':
        time.sleep(1.5)
        print(f"Letter: {letter}")

# Main function
def main():
    # Create two threads
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)

    # Start both threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

    print("\nBoth threads have finished execution.")

# Running the main function
if __name__ == "__main__":
    main()
