File Organizer

A simple Python script that tidies up a messy folder by sorting files into subfolders based on their type (Images, Documents, Videos and so on). It's handy for cleaning up a cluttered `Downloads` folder in seconds.

Requirements

Python 3.6 or newer

Usage

--> Clone the repository from git hub:  ``` git clone https://github.com/drake-gif/mini-projects-python ```
1. In vs code ,cd to ```file organiser folder```, save the script as `organizer.py` 
2. Run it:

   ```bash
   python organizer.py
   ```

3. When prompted, enter the path of the folder you want to organize, or press **Enter** to use `~/Downloads`:

   ```
   Enter folder path to organize (leave blank for Downloads): ~/Desktop
   ```

Resulting structure

```
Downloads/
├── Images/
├── Documents/
├── Videos/
├── Audio/
└── Others/
```

Default Categories

| Category  | Extensions                                         |
|-----------|----------------------------------------------------|
| Images    | `.jpg` `.jpeg` `.png` `.gif` `.svg` `.webp`        |
| Documents | `.pdf` `.docx` `.doc` `.txt` `.xlsx` `.csv` `.pptx`|
| Videos    | `.mp4` `.mkv` `.mov` `.avi`                        |
| Audio     | `.mp3` `.wav` `.aac` `.flac`                       |
| Archives  | `.zip` `.rar` `.tar` `.gz` `.7z`                   |
| Code      | `.py` `.js` `.html` `.css` `.json` `.sql`          |
| Others    | Anything not listed above                          |

Extension matching is case-insensitive, so `PHOTO.JPG` is treated the same as `photo.jpg`.
