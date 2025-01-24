import json
import os
import sys
import random
from colorama import Fore, Back, Style

def list_subdirectories(base_path):
    """Lists all subdirectories in the given base path."""
    return [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

def load_questions_from_directory(directory):
    """Loads all questions from JSON files in the specified directory."""
    questions_by_file = {}
    try:
        for filename in os.listdir(directory):
            if filename.endswith('.json'):
                filepath = os.path.join(directory, filename)
                with open(filepath, 'r') as file:
                    try:
                        questions_by_file[filepath] = json.load(file)
                    except json.JSONDecodeError:
                        print(f"Error: '{filename}' is not a valid JSON file. Skipping.")
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' was not found.")
    return questions_by_file

def save_questions_to_file(filepath, questions):
    """Saves updated questions back to the JSON file."""
    try:
        with open(filepath, 'w') as file:
            json.dump(questions, file, indent=4)
    except Exception as e:
        print(f"Error saving file '{filepath}': {e}")

def main():
    base_path = os.path.dirname(os.path.abspath(__file__))

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    # List all subdirectories in the current script path
    subdirectories = list_subdirectories(base_path)

    if not subdirectories:
        print("No subdirectories found.")
        return

    # Display the subdirectories and let the user choose
    print("")
    for i, subdir in enumerate(subdirectories):
        print(f"{Fore.CYAN}{i + 1}. {subdir}{Style.RESET_ALL}")

    try:
        choice = int(input("\nEnter which of the above directories to work on: ")) - 1
        if choice < 0 or choice >= len(subdirectories):
            print("Invalid choice. Exiting.")
            return
        selected_dir = os.path.join(base_path, subdirectories[choice])
    except ValueError:
        print("Invalid input. Please enter a number. Exiting.")
        return

    # Load all questions from the chosen directory
    questions_by_file = load_questions_from_directory(selected_dir)
    if not questions_by_file:
        print("No questions found in the directory.")
        return

    # Flatten the questions into a single list with file references and shuffle them
    questions = []
    for filepath, q_list in questions_by_file.items():
        for question in q_list:
            questions.append({"file": filepath, "question": question})
    random.shuffle(questions)
    
    if (len(questions) == 0):
        exit
    
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(f"({Fore.GREEN}[correct]{Style.RESET_ALL}/{Fore.RED}[incorrect]{Style.RESET_ALL})\n")

    # Initialize counters
    current_question = 1
    correct = 0
    incorrect = 0
    total_questions = len(questions)

    # Iterate through the list of questions
    while questions:
        current = questions[0]
        # Display progress
        print(f"\t({Fore.GREEN}{correct}{Style.RESET_ALL}/{Fore.RED}{incorrect}{Style.RESET_ALL})\n")
        print(f"Question {current_question} of {total_questions}: {Fore.GREEN}\n\t{current['question']['Question']}{Style.RESET_ALL}\n")
        input("Press Enter to view the answer...")
        print("\n\n")
        print(f"Answer: {Fore.CYAN}\n\t{current['question']['Answer']}{Style.RESET_ALL}\n")

        while True:
            action = input("Did you know the answer? [y/n] (or \"delete\"): ").strip().lower()
            if action == 'y':
                correct += 1
                break
            elif action == 'n':
                incorrect += 1
                break
            elif action == 'delete':
                # Remove question from the original JSON file
                total_questions -= 1
                filepath = current['file']
                questions_by_file[filepath].remove(current['question'])
                save_questions_to_file(filepath, questions_by_file[filepath])
                print(f"Question deleted from file: {filepath}\n")
                break
            else:
                print("Invalid input.")

        # Remove the current question from the list
        questions.pop(0)
        current_question += 1
        
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        if not questions:
            print(f"You have answered all {total_questions} questions.")
            
            print(f"\nYou got {correct} correct and {incorrect} incorrect.\n")


if __name__ == "__main__":
    run = True
    while (run):
        main() # THIS LINE STARTS THE PROGRAM
        
        while True:
            action = input("\nRestart the program? [y/n]: ").strip().lower()
            if action == 'y':
                break
            elif action == 'n':
                run = False
                break
            else:
                print("Invalid input.")
    
    print()
        
    
