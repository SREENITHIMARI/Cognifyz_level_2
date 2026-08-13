#!/usr/bin/env python3
"""
Task 5: File Manipulation - Word Count
Analyze text files and count words, lines, characters, etc.
"""
import os
from pathlib import Path

def count_file_stats(file_path):
    """
    Count statistics for a file
    Returns: word_count, line_count, char_count, file_size
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            lines = content.split('\n')
            words = content.split()
            
            word_count = len(words)
            line_count = len(lines)
            char_count = len(content)
            file_size = os.path.getsize(file_path)
            
            return word_count, line_count, char_count, file_size
    except Exception as e:
        return None, None, None, None, str(e)

def analyze_multiple_files(directory):
    """Analyze all text files in a directory"""
    results = []
    
    if not os.path.isdir(directory):
        return None, "Directory not found!"
    
    for file_path in Path(directory).glob('*.txt'):
        try:
            word_count, line_count, char_count, file_size = count_file_stats(str(file_path))
            if word_count is not None:
                results.append({
                    'name': file_path.name,
                    'words': word_count,
                    'lines': line_count,
                    'chars': char_count,
                    'size': file_size
                })
        except Exception as e:
            pass
    
    return results, None

def create_sample_file():
    """Create a sample text file for testing"""
    sample_content = """Python is a high-level, interpreted programming language.
It's known for its simplicity and readability.
Python supports multiple programming paradigms.

Key features of Python:
- Easy to learn and use
- Extensive standard library
- Dynamic typing
- Automatic memory management
- Great for web development, data science, and AI

Python is used by many companies including Google, Facebook, and Instagram.
"""
    
    sample_path = "sample.txt"
    with open(sample_path, 'w', encoding='utf-8') as file:
        file.write(sample_content)
    
    return sample_path

def file_manipulation():
    """Main file manipulation function"""
    print("\n" + "=" * 60)
    print("    📄 FILE MANIPULATION - WORD COUNT & ANALYSIS")
    print("=" * 60)
    print("\nChoose an option:")
    print("1. Analyze a single file")
    print("2. Analyze all files in a directory")
    print("3. Create a sample file and analyze it")
    print("4. Compare multiple files")
    print("5. Back to main menu")
    print()
    
    while True:
        try:
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '5':
                break
            
            elif choice == '1':
                print()
                file_path = input("Enter file path: ").strip()
                
                if not os.path.exists(file_path):
                    print("❌ File not found!\n")
                    continue
                
                word_count, line_count, char_count, file_size = count_file_stats(file_path)
                
                if word_count is None:
                    print(f"❌ Error reading file: {file_size}\n")
                    continue
                
                print("\n" + "-" * 60)
                print(f"📊 File Analysis: {os.path.basename(file_path)}")
                print("-" * 60)
                print(f"📝 Word Count:       {word_count:>12,d} words")
                print(f"📋 Line Count:       {line_count:>12,d} lines")
                print(f"🔤 Character Count:  {char_count:>12,d} characters")
                print(f"💾 File Size:        {file_size:>12,d} bytes ({file_size/1024:.2f} KB)")
                
                if word_count > 0:
                    avg_word_length = char_count / word_count
                    print(f"📏 Avg Word Length:  {avg_word_length:>12.2f} characters")
                
                if line_count > 1:
                    avg_words_per_line = word_count / (line_count - 1)
                    print(f"📊 Avg Words/Line:   {avg_words_per_line:>12.2f} words")
                
                print("-" * 60 + "\n")
            
            elif choice == '2':
                print()
                directory = input("Enter directory path: ").strip()
                
                results, error = analyze_multiple_files(directory)
                
                if error:
                    print(f"❌ {error}\n")
                    continue
                
                if not results:
                    print("ℹ️  No .txt files found in directory.\n")
                    continue
                
                print("\n" + "-" * 80)
                print(f"📊 Files in directory: {directory}")
                print("-" * 80)
                print(f"{'File Name':<30} {'Words':>12} {'Lines':>12} {'Chars':>12} {'Size (KB)':>12}")
                print("-" * 80)
                
                total_words = 0
                total_lines = 0
                total_chars = 0
                total_size = 0
                
                for file_info in results:
                    print(f"{file_info['name']:<30} {file_info['words']:>12,d} {file_info['lines']:>12,d} {file_info['chars']:>12,d} {file_info['size']/1024:>12.2f}")
                    total_words += file_info['words']
                    total_lines += file_info['lines']
                    total_chars += file_info['chars']
                    total_size += file_info['size']
                
                print("-" * 80)
                print(f"{'TOTAL':<30} {total_words:>12,d} {total_lines:>12,d} {total_chars:>12,d} {total_size/1024:>12.2f}")
                print("-" * 80 + "\n")
            
            elif choice == '3':
                print()
                sample_path = create_sample_file()
                print(f"✅ Created sample file: {sample_path}\n")
                
                word_count, line_count, char_count, file_size = count_file_stats(sample_path)
                
                print("-" * 60)
                print(f"📊 Sample File Analysis")
                print("-" * 60)
                print(f"📝 Word Count:       {word_count:>12,d} words")
                print(f"📋 Line Count:       {line_count:>12,d} lines")
                print(f"🔤 Character Count:  {char_count:>12,d} characters")
                print(f"💾 File Size:        {file_size:>12,d} bytes")
                print("-" * 60)
                print(f"\n📄 Sample content:\n")
                
                with open(sample_path, 'r') as f:
                    print(f.read())
                
                print("-" * 60 + "\n")
            
            elif choice == '4':
                print()
                num_files = int(input("How many files to compare? "))
                
                files_data = []
                for i in range(num_files):
                    file_path = input(f"Enter file path {i+1}: ").strip()
                    
                    if not os.path.exists(file_path):
                        print(f"❌ File not found: {file_path}")
                        continue
                    
                    word_count, line_count, char_count, file_size = count_file_stats(file_path)
                    if word_count is not None:
                        files_data.append({
                            'name': os.path.basename(file_path),
                            'words': word_count,
                            'lines': line_count,
                            'chars': char_count,
                            'size': file_size
                        })
                
                if not files_data:
                    print("❌ No valid files to compare.\n")
                    continue
                
                print("\n" + "-" * 80)
                print("📊 File Comparison")
                print("-" * 80)
                print(f"{'File Name':<30} {'Words':>12} {'Lines':>12} {'Chars':>12} {'Size (KB)':>12}")
                print("-" * 80)
                
                for file_info in files_data:
                    print(f"{file_info['name']:<30} {file_info['words']:>12,d} {file_info['lines']:>12,d} {file_info['chars']:>12,d} {file_info['size']/1024:>12.2f}")
                
                print("-" * 80)
                print(f"Most words: {max(files_data, key=lambda x: x['words'])['name']}")
                print(f"Longest file: {max(files_data, key=lambda x: x['lines'])['name']}")
                print(f"Largest file: {max(files_data, key=lambda x: x['size'])['name']}")
                print("-" * 80 + "\n")
            
            else:
                print("❌ Invalid choice! Please enter 1-5.\n")
        
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.\n")
        except KeyboardInterrupt:
            print("\n\n⚠️  Interrupted!")
            break

if __name__ == "__main__":
    try:
        file_manipulation()
    except KeyboardInterrupt:
        print("\n⚠️  Interrupted!")
