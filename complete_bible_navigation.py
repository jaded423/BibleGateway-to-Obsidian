#!/usr/bin/env python3
"""
Complete Bible Navigation Script
Adds navigation links to all Bible chapter files in one comprehensive script.
Handles both regular books and numbered books with proper cross-book navigation.

Usage: python3 complete_bible_navigation.py
"""

import os
import re

# Complete Bible book information: (folder_name, file_prefix, full_name, chapter_count)
BIBLE_BOOKS = [
    # Old Testament
    ("Genesis", "Gen", "Genesis", 50),
    ("Exodus", "Exod", "Exodus", 40),
    ("Leviticus", "Lev", "Leviticus", 27),
    ("Numbers", "Num", "Numbers", 36),
    ("Deuteronomy", "Deut", "Deuteronomy", 34),
    ("Joshua", "Josh", "Joshua", 24),
    ("Judges", "Judg", "Judges", 21),
    ("Ruth", "Ruth", "Ruth", 4),
    ("1 Samuel", "1 Sam", "1 Samuel", 31),
    ("2 Samuel", "2 Sam", "2 Samuel", 24),
    ("1 Kings", "1 Kgs", "1 Kings", 22),
    ("2 Kings", "2 Kgs", "2 Kings", 25),
    ("1 Chronicles", "1 Chr", "1 Chronicles", 29),
    ("2 Chronicles", "2 Chr", "2 Chronicles", 36),
    ("Ezra", "Ezra", "Ezra", 10),
    ("Nehemiah", "Neh", "Nehemiah", 13),
    ("Esther", "Esth", "Esther", 10),
    ("Job", "Job", "Job", 42),
    ("Psalms", "Ps", "Psalms", 150),
    ("Proverbs", "Prov", "Proverbs", 31),
    ("Ecclesiastes", "Eccl", "Ecclesiastes", 12),
    ("Song of Solomon", "Song", "Song of Solomon", 8),
    ("Isaiah", "Isa", "Isaiah", 66),
    ("Jeremiah", "Jer", "Jeremiah", 52),
    ("Lamentations", "Lam", "Lamentations", 5),
    ("Ezekiel", "Ezek", "Ezekiel", 48),
    ("Daniel", "Dan", "Daniel", 12),
    ("Hosea", "Hos", "Hosea", 14),
    ("Joel", "Joel", "Joel", 3),
    ("Amos", "Amos", "Amos", 9),
    ("Obadiah", "Obad", "Obadiah", 1),
    ("Jonah", "Jonah", "Jonah", 4),
    ("Micah", "Mic", "Micah", 7),
    ("Nahum", "Nah", "Nahum", 3),
    ("Habakkuk", "Hab", "Habakkuk", 3),
    ("Zephaniah", "Zeph", "Zephaniah", 3),
    ("Haggai", "Hag", "Haggai", 2),
    ("Zechariah", "Zech", "Zechariah", 14),
    ("Malachi", "Mal", "Malachi", 4),
    # New Testament
    ("Matthew", "Matt", "Matthew", 28),
    ("Mark", "Mark", "Mark", 16),
    ("Luke", "Luke", "Luke", 24),
    ("John", "John", "John", 21),
    ("Acts", "Acts", "Acts", 28),
    ("Romans", "Rom", "Romans", 16),
    ("1 Corinthians", "1 Cor", "1 Corinthians", 16),
    ("2 Corinthians", "2 Cor", "2 Corinthians", 13),
    ("Galatians", "Gal", "Galatians", 6),
    ("Ephesians", "Eph", "Ephesians", 6),
    ("Philippians", "Phil", "Philippians", 4),
    ("Colossians", "Col", "Colossians", 4),
    ("1 Thessalonians", "1 Thess", "1 Thessalonians", 5),
    ("2 Thessalonians", "2 Thess", "2 Thessalonians", 3),
    ("1 Timothy", "1 Tim", "1 Timothy", 6),
    ("2 Timothy", "2 Tim", "2 Timothy", 4),
    ("Titus", "Titus", "Titus", 3),
    ("Philemon", "Phlm", "Philemon", 1),
    ("Hebrews", "Heb", "Hebrews", 13),
    ("James", "Jas", "James", 5),
    ("1 Peter", "1 Pet", "1 Peter", 5),
    ("2 Peter", "2 Pet", "2 Peter", 3),
    ("1 John", "1 John", "1 John", 5),
    ("2 John", "2 John", "2 John", 1),
    ("3 John", "3 John", "3 John", 1),
    ("Jude", "Jude", "Jude", 1),
    ("Revelation", "Rev", "Revelation", 22)
]

def get_chapter_info(book_index, chapter):
    """Get the navigation info for a specific chapter"""
    folder_name, file_prefix, full_name, chapter_count = BIBLE_BOOKS[book_index]
    
    # Determine previous chapter
    if chapter == 1:
        if book_index == 0:  # First book, first chapter
            prev_link = None
        else:
            # Go to last chapter of previous book
            prev_book = BIBLE_BOOKS[book_index - 1]
            prev_link = f"[[{prev_book[1]} {prev_book[3]}|← {prev_book[2]} {prev_book[3]}]]"
    else:
        prev_link = f"[[{file_prefix} {chapter - 1}|← {full_name} {chapter - 1}]]"
    
    # Determine next chapter
    if chapter == chapter_count:
        if book_index == len(BIBLE_BOOKS) - 1:  # Last book, last chapter
            next_link = None
        else:
            # Go to first chapter of next book
            next_book = BIBLE_BOOKS[book_index + 1]
            next_link = f"[[{next_book[1]} 1|{next_book[2]} 1 →]]"
    else:
        next_link = f"[[{file_prefix} {chapter + 1}|{full_name} {chapter + 1} →]]"
    
    return prev_link, next_link

def create_navigation_line(prev_link, next_link):
    """Create the navigation line based on available links"""
    if prev_link and next_link:
        return f"{prev_link} | {next_link}"
    elif prev_link:
        return prev_link
    elif next_link:
        return next_link
    else:
        return ""

def clean_existing_navigation(content):
    """Remove any existing navigation lines from content"""
    lines = content.split('\n')
    cleaned_lines = []
    
    for line in lines:
        # Skip lines that look like navigation (contain ← or →)
        if '←' in line or '→' in line:
            continue
        # Skip lines that are just separators after navigation
        if line.strip() == '***' and len(cleaned_lines) > 0 and cleaned_lines[-1].strip() == '':
            continue
        cleaned_lines.append(line)
    
    return cleaned_lines

def process_file(bible_path, book_index, chapter):
    """Process a single Bible chapter file"""
    folder_name, file_prefix, full_name, chapter_count = BIBLE_BOOKS[book_index]
    
    # Construct file path
    file_path = os.path.join(bible_path, folder_name, f"{file_prefix} {chapter}.md")
    
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return False
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get navigation links
    prev_link, next_link = get_chapter_info(book_index, chapter)
    nav_line = create_navigation_line(prev_link, next_link)
    
    if not nav_line:
        print(f"Skipping {file_path} - no navigation needed")
        return False
    
    # Remove any existing navigation
    cleaned_lines = clean_existing_navigation(content)
    
    # Find the header line (starts with # and contains the book/chapter info)
    header_index = -1
    for i, line in enumerate(cleaned_lines):
        if line.startswith('#') and (full_name in line or f"{chapter}" in line.split()[-1]):
            header_index = i
            break
    
    if header_index == -1:
        # Try to find any header that starts with #
        for i, line in enumerate(cleaned_lines):
            if line.startswith('#'):
                header_index = i
                break
    
    if header_index == -1:
        print(f"Could not find header in {file_path}")
        return False
    
    # Insert navigation at top (before header)
    new_content = []
    new_content.extend(cleaned_lines[:header_index])
    new_content.append(nav_line)
    new_content.extend(cleaned_lines[header_index:])
    
    # Add navigation at bottom
    new_content.append('')
    new_content.append(nav_line)
    
    # Write the file back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_content))
    
    return True

def find_bible_folder():
    """Find the Bible folder in the current directory"""
    current_dir = os.getcwd()
    
    bible_folders = []
    for item in os.listdir(current_dir):
        if os.path.isdir(item) and any(keyword in item.lower() for keyword in ['bible', 'scripture', 'esv', 'kjv', 'niv']):
            bible_folders.append(item)
    
    if not bible_folders:
        print("No Bible folder found in current directory.")
        print("Looking for folders containing: 'bible', 'scripture', 'esv', 'kjv', or 'niv'")
        return None
    
    if len(bible_folders) == 1:
        bible_path = os.path.join(current_dir, bible_folders[0])
        print(f"Found Bible folder: {bible_folders[0]}")
        return bible_path
    else:
        print("Multiple Bible folders found:")
        for i, folder in enumerate(bible_folders, 1):
            print(f"  {i}. {folder}")
        try:
            choice = int(input("Enter the number of the folder to use: ")) - 1
            if 0 <= choice < len(bible_folders):
                return os.path.join(current_dir, bible_folders[choice])
            else:
                print("Invalid choice")
                return None
        except ValueError:
            print("Invalid input")
            return None

def main():
    print("Complete Bible Navigation Script")
    print("=" * 50)
    
    # Find Bible folder
    bible_path = find_bible_folder()
    if not bible_path:
        return
    
    print("\nProcessing all Bible files...")
    print("This will add navigation to the top and bottom of each chapter.")
    print("Format: [[Previous|← Title]] | [[Next|Title →]]")
    
    # Confirm before proceeding
    response = input("\nProceed? (y/n): ").lower().strip()
    if response not in ['y', 'yes']:
        print("Cancelled.")
        return
    
    print("\nProcessing files...")
    
    updated_count = 0
    total_files = sum(chapter_count for _, _, _, chapter_count in BIBLE_BOOKS)
    
    # Process each book and chapter
    for book_index, (folder_name, file_prefix, full_name, chapter_count) in enumerate(BIBLE_BOOKS):
        print(f"Processing {full_name} ({chapter_count} chapters)...")
        
        book_updated = 0
        for chapter in range(1, chapter_count + 1):
            if process_file(bible_path, book_index, chapter):
                book_updated += 1
                updated_count += 1
        
        if book_updated > 0:
            print(f"  Updated {book_updated}/{chapter_count} files")
        else:
            print(f"  No updates needed (navigation already exists)")
    
    print(f"\nComplete! Updated {updated_count} out of {total_files} total Bible chapters.")
    print("All Bible files now have seamless navigation between chapters and books.")

if __name__ == "__main__":
    main()