# ESV Bible Setup for Obsidian with Complete Navigation

This guide provides a complete setup process for creating a fully navigable ESV Bible in Obsidian with bold Jesus words, chapter/verse breaks, and seamless navigation between all 1,189 chapters across 66 books.

## Features

- **Complete ESV text** with proper formatting
- **Bold words of Jesus** throughout the Gospels
- **Chapter and verse breaks** for easy reading
- **Seamless navigation** between all chapters and books
- **Cross-book navigation** (e.g., Matthew 28 → Mark 1)
- **Obsidian-optimized** with proper linking and cross-references

## Prerequisites

- **Ruby** (pre-installed on macOS, [install on Windows](https://www.perl.org/get.html))
- **Perl** (may be needed on Windows)
- **Python 3** (for navigation script)
- **Obsidian** vault ready for import

## Installation Steps

### Step 1: Clone Required Repositories

Clone both the original BibleGateway-to-Markdown script and the Obsidian adapter:

```bash
git clone https://github.com/jgclark/BibleGateway-to-Markdown.git
git clone https://github.com/jaded423/BibleGateway-to-Obsidian.git
```

### Step 2: Set Up Scripts

Copy both required scripts to the same directory:

```bash
# Copy the core script
cp BibleGateway-to-Markdown/bg2md.rb .

# Copy the Obsidian adapter
cp BibleGateway-to-Obsidian/bg2obs.sh .

# Copy the locales folder (required for language support)
cp -r BibleGateway-to-Obsidian/locales .
```

### Step 3: Install Ruby Dependencies

```bash
gem install colorize optparse clipboard
```

### Step 4: Download ESV Bible

Run the BibleGateway script with the following arguments for optimal ESV setup:

```bash
bash bg2obs.sh -v ESV -b -e -a -i -c -y
```

**Command breakdown:**
- `-v ESV` - Downloads English Standard Version
- `-b` - Bold words of Jesus
- `-e` - Include editorial headers (chapter/verse structure)
- `-a` - Create aliases in YAML front matter
- `-i` - Show verbose progress information
- `-c` - Include inline navigation for breadcrumbs
- `-y` - Print navigation in frontmatter for breadcrumbs plugin

This creates a `Scripture (ESV)` folder with all Bible books and chapters.

### Step 5: Add Complete Navigation

The original script may have incomplete navigation, especially for numbered books (1 Chronicles, 1 John, etc.). Use the complete navigation script to fix this:

1. **Save the navigation script** as `complete_bible_navigation.py` in the same directory
2. **Run the navigation script:**

```bash
python3 complete_bible_navigation.py
```

This script will:
- Auto-detect your Bible folder
- Add navigation to all 1,189 chapters
- Handle cross-book navigation properly
- Fix any broken links in numbered books

### Step 6: Import to Obsidian

1. **Move the entire `Scripture (ESV)` folder** into your Obsidian vault
2. **Use `The Bible.md`** as your main navigation file
3. **Start exploring** with full navigation between all chapters

## Navigation Format

Each chapter will have navigation at the top and bottom in this format:

```markdown
[[Matt 8|← Matthew 8]] | [[Matt 10|Matthew 10 →]]
# Matthew 9
***
[chapter content]
***
[[Matt 8|← Matthew 8]] | [[Matt 10|Matthew 10 →]]
```

## File Structure

```
Scripture (ESV)/
├── Genesis/
│   ├── Gen 1.md
│   ├── Gen 2.md
│   └── ...
├── Matthew/
│   ├── Matt 1.md
│   ├── Matt 2.md
│   └── ...
├── 1 Chronicles/
│   ├── 1 Chr 1.md
│   ├── 1 Chr 2.md
│   └── ...
└── The Bible.md (main navigation)
```

## Troubleshooting

### Navigation Links Don't Work
- Make sure you ran the `complete_bible_navigation.py` script
- Check that file names match the link format (e.g., `Matt 5.md` not `Matthew 5.md`)

### Ruby Gems Not Installing
Try installing with admin privileges:
```bash
sudo gem install colorize optparse clipboard
```

### Language Not Found Error
Make sure you copied the `locales` folder from the BibleGateway-to-Obsidian repository.

### ESV Copyright Notice
The ESV has specific copyright restrictions. This setup is intended for personal study use only. Please respect the ESV copyright guidelines regarding distribution and usage limits.

## Scripts Used

1. **bg2md.rb** - Core BibleGateway scraping script (by jgclark)
2. **bg2obs.sh** - Obsidian formatting adapter (by selfire1/jaded423)
3. **complete_bible_navigation.py** - Complete navigation system (custom)

## Credits

- Original BibleGateway-to-Markdown: [jgclark](https://github.com/jgclark/BibleGateway-to-Markdown)
- Obsidian adaptation: [selfire1](https://github.com/selfire1/BibleGateway-to-Obsidian)
- Fork used: [jaded423](https://github.com/jaded423/BibleGateway-to-Obsidian)
- Navigation enhancements: Custom solution for complete Bible navigation

## Final Result

A complete, navigable ESV Bible in Obsidian with:
- 66 books, 1,189 chapters
- Bold Jesus words
- Seamless navigation between any chapters
- Cross-references and linked mentions
- Perfect for Bible study and note-taking in Obsidian