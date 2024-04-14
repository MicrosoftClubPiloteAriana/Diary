# Diary

## Introduction

Diary is a command-line Python application that allows users to create and manage diary entries. It provides functionalities such as user authentication, creating diary entries, searching for entries, displaying all entries, and editing entries.

## Features

- User authentication with username and password.
- Diary entries are stored in JSON format.
- Create, search, display, and edit diary entries.
- Date and time stamps for each diary entry.

## Installation

To run this application locally, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/MicrosoftClubPiloteAriana/Diary.git
   ```
2. Navigate to the project directory:

   ```bash
   cd Diary
   ```
3. Run the script:

   ```bash
   python secure_diary.py
   ```
## Usage
1. When prompted, select an option:
   
    Create User: Create a new user account.

    Login: Log in to an existing account.

    Exit: Terminate the application.

2. If you choose to create a user, enter a username and a secure password. If the username is available, a new user account will be created.

3. If you choose to log in, enter your username and password. Upon successful authentication, you will be logged in to your account and presented with a menu.

4. From the menu, you can:
 
    Add Entry: Create a new diary entry by providing a title and content.

    Search Entries: Search for diary entries based on the title or date.

    Display All Entries: View all diary entries.

    Edit Entry: Edit an existing diary entry by searching for it using the title or date.

6. Once you are done, you can choose to logout to exit your session.
