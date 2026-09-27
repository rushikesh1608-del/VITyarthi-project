# Contact Book

A simple command-line contact book written in Python. It lets you add, view,
search, update, and delete contacts (name, phone, email) for the duration of
a single run. Contacts are stored in memory only — closing the program clears
them, since there is no file or database saving in this version.

## Features

- **Add Contact** — save a name, phone number, and optional email
- **View All Contacts** — list every saved contact, sorted alphabetically
- **Search Contact** — look up one contact by exact name
- **Update Contact** — change a contact's phone/email (leave a field blank to keep it as-is)
- **Delete Contact** — remove a contact, with a yes/no confirmation prompt
- **Exit** — quit the program

## Requirements

- Python 3.6 or newer (no third-party packages required — the project only
  uses Python's built-in features)

## Project Files

```
.
├── contact_book.py   # The main program
└── README.md          # This file
```

## Setup

1. **Install Python**, if you don't already have it:
   - Check whether it's installed by running:
     ```bash
     python3 --version
     ```
   - If that fails or shows a version below 3.6, download and install Python
     from [python.org/downloads](https://www.python.org/downloads/).

2. **Get the project files** onto your machine (e.g. download or clone them
   into a folder), and make sure `VITyarthi project.py` is in that folder.

3. **No dependency installation is needed.** The script only uses Python's
   standard library, so there is no `requirements.txt` or virtual environment
   to set up.

## Running the Program

1. Open a terminal (Command Prompt, PowerShell, or a Unix shell).
2. Navigate to the folder containing `VITyarthi project.py`:
   ```bash
   cd path/to/project-folder
   ```
3. Run the script:
   ```bash
   python3 VITyarthi project.py
   ```
   On Windows, if `python3` isn't recognized, try:
   ```bash
   python VITyarthi project.py
   ```

## Using the Program

After starting the program, you'll see a menu:

```
====== CONTACT BOOK =======
1. Add Contact
2. View All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6):
```

Type the number for the action you want and press Enter, then follow the
prompts:

- **Add Contact (1):** enter a name, phone number, and an optional email.
  If the name already exists, you'll be told to use "Update" instead.
- **View All Contacts (2):** prints every contact currently saved, in
  alphabetical order.
- **Search Contact (3):** enter a name to look up; must match exactly
  (case-sensitive).
- **Update Contact (4):** enter the name to update, then new phone/email
  values. Press Enter without typing anything to leave a field unchanged.
- **Delete Contact (5):** enter the name to delete, then confirm with `y`
  (anything else cancels the deletion).
- **Exit (6):** closes the program. All contacts are lost when you exit,
  since nothing is saved to disk.

## Notes / Known Limitations

- **No persistence:** contacts only exist while the program is running.
  Restarting the script starts with an empty contact list.
- **Case-sensitive & exact-match names:** searching, updating, and deleting
  all require the name to be typed exactly as it was entered when added.
- **No input validation** on phone number format — any text is accepted.

## Possible Future Improvements

- Save/load contacts to a file (e.g. JSON or CSV) so data persists between runs
- Add partial/case-insensitive name search
- Validate phone number and email formats
