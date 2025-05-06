<<<<<<< HEAD
#!/usr/bin/env python3
import os
import argparse
from pathlib import Path

def process_log_file(log_path, output_file, max_lines=2000):
    """
    Process a single log file:
    - Skip lines starting with "SLF4J"
    - Add file name as ID column
    - Get only first max_lines lines
    
    Args:
        log_path: Path to the log file
        output_file: Open file handle to write to
        max_lines: Maximum number of lines to process (default: 2000)
    """
    # Extract filename and remove container_ prefix and .log extension
    filename = os.path.basename(log_path)
    file_id = filename
    if filename.startswith("container_"):
        file_id = filename[len("container_"):]
    if file_id.endswith(".log"):
        file_id = file_id[:-4]
    line_count = 0
    
    try:
        with open(log_path, 'r', encoding='utf-8', errors='replace') as log_file:
            for line in log_file:
                # Skip lines starting with SLF4J
                if line.startswith("SLF4J"):
                    continue
                
                # Add file ID as a new column and write to output
                modified_line = f"{file_id} {line.rstrip()}\n"
                output_file.write(modified_line)
                
                line_count += 1
                if line_count >= max_lines:
                    break
                    
        print(f"Processed {line_count} lines from {log_path}")
        return line_count
    except Exception as e:
        print(f"Error processing {log_path}: {str(e)}")
        return 0

def merge_logs(root_folder, output_path, file_extension='.log', max_lines=2000):
    """
    Merge all log files from all application folders into one log file.
    
    Args:
        root_folder: Root folder containing application folders
        output_path: Path for the merged output file
        file_extension: Extension of log files (default: .log)
        max_lines: Maximum number of lines to take from each log file (default: 2000)
    """
    total_files = 0
    total_lines = 0
    
    with open(output_path, 'w', encoding='utf-8') as output_file:
        # Write header
        # output_file.write("file_id|log_content\n")
        
        # Walk through the directory tree
        for root, dirs, files in os.walk(root_folder):
            log_files = [f for f in files if f.endswith(file_extension)]
            
            for log_file in log_files:
                log_path = os.path.join(root, log_file)
                lines_processed = process_log_file(log_path, output_file, max_lines)
                
                if lines_processed > 0:
                    total_files += 1
                    total_lines += lines_processed
    
    print(f"\nMerge completed:")
    print(f"- Total log files processed: {total_files}")
    print(f"- Total lines in merged file: {total_lines}")
    print(f"- Output saved to: {output_path}")

def main():
    parser = argparse.ArgumentParser(description='Merge log files from multiple application folders')
    parser.add_argument('root_folder', help='Root folder containing application folders')
    parser.add_argument('--output', '-o', default='merge/merged_logs.log', 
                        help='Path for the output merged log file (default: merge/merged_logs.log)')
    parser.add_argument('--extension', '-e', default='.log',
                        help='Log file extension to search for (default: .log)')
    parser.add_argument('--max-lines', '-m', type=int, default=2000,
                        help='Maximum lines to take from each log file (default: 2000)')
    
    args = parser.parse_args()
    
    # Convert to absolute paths
    root_folder = os.path.abspath(args.root_folder)
    output_path = os.path.abspath(args.output)
    
    # Validate the input folder exists
    if not os.path.isdir(root_folder):
        print(f"Error: Folder does not exist: {root_folder}")
        return 1
    
    print(f"Starting log merge process:")
    print(f"- Scanning folder: {root_folder}")
    print(f"- Looking for files with extension: {args.extension}")
    print(f"- Taking up to {args.max_lines} lines per log file")
    print(f"- Output will be saved to: {output_path}")
    print("-" * 60)
    
    merge_logs(root_folder, output_path, args.extension, args.max_lines)
    return 0

if __name__ == "__main__":
=======
#!/usr/bin/env python3
import os
import argparse
from pathlib import Path

def process_log_file(log_path, output_file, max_lines=2000):
    """
    Process a single log file:
    - Skip lines starting with "SLF4J"
    - Add file name as ID column
    - Get only first max_lines lines
    
    Args:
        log_path: Path to the log file
        output_file: Open file handle to write to
        max_lines: Maximum number of lines to process (default: 2000)
    """
    # Extract filename and remove container_ prefix and .log extension
    filename = os.path.basename(log_path)
    file_id = filename
    if filename.startswith("container_"):
        file_id = filename[len("container_"):]
    if file_id.endswith(".log"):
        file_id = file_id[:-4]
    line_count = 0
    
    try:
        with open(log_path, 'r', encoding='utf-8', errors='replace') as log_file:
            for line in log_file:
                # Skip lines starting with SLF4J
                if line.startswith("SLF4J"):
                    continue
                
                # Add file ID as a new column and write to output
                modified_line = f"{file_id} {line.rstrip()}\n"
                output_file.write(modified_line)
                
                line_count += 1
                if line_count >= max_lines:
                    break
                    
        print(f"Processed {line_count} lines from {log_path}")
        return line_count
    except Exception as e:
        print(f"Error processing {log_path}: {str(e)}")
        return 0

def merge_logs(root_folder, output_path, file_extension='.log', max_lines=2000):
    """
    Merge all log files from all application folders into one log file.
    
    Args:
        root_folder: Root folder containing application folders
        output_path: Path for the merged output file
        file_extension: Extension of log files (default: .log)
        max_lines: Maximum number of lines to take from each log file (default: 2000)
    """
    total_files = 0
    total_lines = 0
    
    with open(output_path, 'w', encoding='utf-8') as output_file:
        # Write header
        # output_file.write("file_id|log_content\n")
        
        # Walk through the directory tree
        for root, dirs, files in os.walk(root_folder):
            log_files = [f for f in files if f.endswith(file_extension)]
            
            for log_file in log_files:
                log_path = os.path.join(root, log_file)
                lines_processed = process_log_file(log_path, output_file, max_lines)
                
                if lines_processed > 0:
                    total_files += 1
                    total_lines += lines_processed
    
    print(f"\nMerge completed:")
    print(f"- Total log files processed: {total_files}")
    print(f"- Total lines in merged file: {total_lines}")
    print(f"- Output saved to: {output_path}")

def main():
    parser = argparse.ArgumentParser(description='Merge log files from multiple application folders')
    parser.add_argument('root_folder', help='Root folder containing application folders')
    parser.add_argument('--output', '-o', default='merge/merged_logs.log', 
                        help='Path for the output merged log file (default: merge/merged_logs.log)')
    parser.add_argument('--extension', '-e', default='.log',
                        help='Log file extension to search for (default: .log)')
    parser.add_argument('--max-lines', '-m', type=int, default=2000,
                        help='Maximum lines to take from each log file (default: 2000)')
    
    args = parser.parse_args()
    
    # Convert to absolute paths
    root_folder = os.path.abspath(args.root_folder)
    output_path = os.path.abspath(args.output)
    
    # Validate the input folder exists
    if not os.path.isdir(root_folder):
        print(f"Error: Folder does not exist: {root_folder}")
        return 1
    
    print(f"Starting log merge process:")
    print(f"- Scanning folder: {root_folder}")
    print(f"- Looking for files with extension: {args.extension}")
    print(f"- Taking up to {args.max_lines} lines per log file")
    print(f"- Output will be saved to: {output_path}")
    print("-" * 60)
    
    merge_logs(root_folder, output_path, args.extension, args.max_lines)
    return 0

if __name__ == "__main__":
>>>>>>> 2ba4dafa332bd1f4d7b245a7011b588af28727e0
    exit(main())