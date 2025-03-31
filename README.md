# QnA-quiz

## Project description

Simple way of quizzing yourself on questions. Good practice for exams etc. Add a question, add an answer to the question and play the quiz!

In the "json" folder, there are subdirectories which contain the JSON files that are used for the quiz. When you play the quiz it only loads the questions that are within this directory to allow you to sort the questions for different topics and courses. This allows you to prepare the quiz for many different subjects but focus on only one at a time!

When you start the program you get to choose which directory to play in, and then the program lets you add more questions if you wish. This will automatically add the questions and answers to a JSON file within that directory.

A quick way of adding questions is also to send your teachers powerpoints or other files containing good information to ChatGPT and ask to extract a couple of questions from each file. Then you could also upload one of the JSON files within this project and ask ChatGPT to create new JSON files with this format and input the questions and answers it extracted from the powerpoints or PDFs you sent it. Then you simply save these new JSON files and put them within the correct directory!

This image is what the program looks like when you reveal an answer:

![Image Description](https://i.imgur.com/cURTJpf.png)


## Usage

This project is quite small and has minimal dependencies. It runs in a command prompt and only requires Python and Colorama to be installed. You run the program like this:

### Linux (Debian)

To install Python and Colorama, paste this into a terminal window:

```bash
# Install Python and Colorama
sudo apt update
sudo apt install python3 python3-colorama

echo ""

# Confirm that Python and Colorama are installed
python3 --version
python3 -c "import colorama; print(f'Colorama version {colorama.__version__}')"

echo ""
```

Then run the program by doing:

```bash
cd <program-directory>
quiz.py
```

### Windows

First go to https://www.python.org/downloads/ to download and install Python. 

Then install Colorama by pasting this into a terminal window (it also works if you make it a .bat script):

```cmd
@echo off
echo.
pip install colorama

echo.

REM Check that everything is installed:
python --version
echo.
pip --version
echo.
python -c "import colorama; print(f'Colorama version {colorama.__version__}')"

pause
```

Then run the program by doing:

```cmd
cd <program-directory>
py quiz.py
```
