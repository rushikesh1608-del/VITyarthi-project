# Problem Statement

## Project Title
Contact Book – A Command-Line Application

## Background
Keeping track of personal or professional contacts — names, phone numbers,
and email addresses — is a common everyday need. While full-scale address
book apps exist, a lightweight, dependency-free command-line tool is useful
for learning core programming concepts (data structures, functions, control
flow, and I/O handling) and for quick contact management without the
overhead of a GUI or a database.

## Problem
Build a command-line contact management system in Python that allows a user
to store and manage a set of contacts during a program session, without
relying on any external libraries, files, or a database.

The system must let a user:
- Add a new contact (name, phone number, and an optional email), while
  preventing duplicate names.
- View all saved contacts, sorted alphabetically.
- Search for a specific contact by name.
- Update an existing contact's phone number and/or email, without losing
  the fields the user chooses not to change.
- Delete a contact, with a confirmation step to avoid accidental removal.
- Exit the program cleanly.

## Objective
Design and implement a menu-driven Python program that satisfies the above
requirements using only Python's standard library, runs entirely from the
terminal (no GUI dependency), and is straightforward enough to demonstrate
core programming fundamentals clearly.

## Scope
- **In scope:** in-memory contact storage (dictionary-based), a numbered
  terminal menu, add/view/search/update/delete operations, basic duplicate
  and confirmation checks.
- **Out of scope (current version):** persistent storage (file/database),
  input format validation (e.g. phone number format), a graphical or web
  interface, and multi-user support.

## Expected Outcome
A single, self-contained Python script (`contact_book.py`) that can be run
with `python3 contact_book.py`, presents a clear menu, and correctly
performs all five contact operations as described above, along with
supporting documentation (`README.md`) explaining setup and usage.
