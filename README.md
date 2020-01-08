![](readme_files/banner.png)

# Bulk File Comparison

## Features
 - Compare files in two directories to see whether they are identical.
    - Check files contents using cmp.
 - Report if a file was not matched against anything.

## Requirements and Installation
 - [Python 3.6+](https://www.python.org/)
 - Linux (tested)
 - Install all dependencies from the requirements.txt file. `pip3 install -r requirements.txt`

## Arguments
#### Required arguments:
  - `-p1 PATH1` || `--path1 PATH1`
    - Main path (absolute or relative). This is the path which you want every file checked.
  
  - `-p2 PATH2` || `--path2 PATH2`
    - Sub path (absolute or relative). This is the path where files may be skipped if they are not in path1.
  

#### Optional arguments:
  - `-o` || `--toOutput`
    - Removes ANSI escape sequences for terminal colouring. It is useful for redirecting.
    - Default: Disabled

  - `-s` || `--silent`
    - If a file in path1 is not found in path2, hide in output.
    - Default: Disabled
  
  - `--version`
    - Display program version


## Usage
 - Run 'compare.py' in terminal with arguments (see above)

### Starter command(s)
 - Run
    - `python3 compare.py -p1 "full_physical_path" -p2 "full_logical_path"`
    
 - Run w/ output
    - `python3 compare.py -p1 "full_physical_path" -p2 "full_logical_path" -o >> FILE.txt`


## Changelog
#### Version 1.0 - Initial release
 - Compare files in two directories
 - Hide non paired files using silent mode
 - Clear terminal colouring using output mode
 
#### Version 1.1 - Bug fixes
 - Fixed bugs that prevented files from being properly compared