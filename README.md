# Company Matching Utility

## Table of Contents
1. [Introduction](#introduction)
2. [How it Works](#how-it-works)
3. [How to Run](#how-to-run)
4. [Data](#data)

## Introduction
This tool is used in a research project on shareholders of publicly traded companies. The tool allows the user to match and categorize companies based on a set of target and matched strings. The tool is designed to be run in a terminal and operates on a CSV file that contains the target and matched strings. The tool will then prompt the user to match the target and matched strings by assigning a unique ID to each set of matching companies.

## How it Works
The tool uses the Python standard library to accomplish its task. It reads the contents of a CSV file and prompts the user to match the target and matched strings. The user inputs their match decision by typing one of the following keys: 'n', '1', '2', 'u', 'b', or 'q'.
- 'n': indicates that the two strings are not the same company.
- '1': indicates that the first string is the correct spelling.
- '2': indicates that the second string is the correct spelling.
- 'u': indicates that the user is unsure about the match.
- 'b': indicates that the user wants to go back to the previous question.
- 'q': indicates that the user wants to quit the utility.

The tool then updates the CSV file with the user's match decision and moves on to the next pair of strings. The process continues until all strings have been matched.

## How to Run
1. Install Python3 on your machine if it's not already installed.
2. Download the code for this tool.
3. Run the following command in the terminal:

`python3 company_matching_utility.py`

4. The tool will start and prompt the user for input as described in the "How it Works" section.

![Screenshot 2023-01-27 at 17 55 35](https://user-images.githubusercontent.com/99140162/215615052-71073048-ca90-4ece-877d-c5feda964774.png)

## Data
The tool operates on a CSV file that contains the target and matched strings, and an optional column for the company ID. A sample data file has been provided, but any CSV file in the same format can be used. The file should contain the following columns:
- `target_index`
- `target_string`
- `match_index`
- `matched_string`
- `company_id`

