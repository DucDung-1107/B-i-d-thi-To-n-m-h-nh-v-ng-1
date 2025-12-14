import os
import json
import shutil

source_dir = r"C:\Users\Admin\Downloads\GHÉP\archive\Doc_misscellinuous\layout_content\layout_content"
dest_dir = r"C:\Users\Admin\Downloads\GHÉP\results\layout_content_final_QWEN"

def is_all_text_type(file_path):
    """Check if all lines in a JSONL file have type='text'"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    data = json.loads(line)
                    # Check if 'type' field exists and is not 'text'
                    if 'type' in data and data['type'] != 'text':
                        return False
                except json.JSONDecodeError:
                    continue
        return True
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False

def main():
    # Get list of files already in destination
    existing_files = set(os.listdir(dest_dir))
    
    # Get list of files in source
    source_files = [f for f in os.listdir(source_dir) if f.endswith('.jsonl')]
    
    copied_count = 0
    skipped_existing = 0
    skipped_not_text = 0
    
    text_only_files = []
    
    for filename in source_files:
        source_path = os.path.join(source_dir, filename)
        
        # Check if file already exists in destination
        if filename in existing_files:
            skipped_existing += 1
            continue
        
        # Check if all types are 'text'
        if is_all_text_type(source_path):
            text_only_files.append(filename)
            dest_path = os.path.join(dest_dir, filename)
            shutil.copy2(source_path, dest_path)
            copied_count += 1
            print(f"Copied: {filename}")
        else:
            skipped_not_text += 1
    
    print(f"\n=== Summary ===")
    print(f"Total files in source: {len(source_files)}")
    print(f"Files already exist in destination: {skipped_existing}")
    print(f"Files with non-text types (skipped): {skipped_not_text}")
    print(f"Files copied (all text type): {copied_count}")
    
    if text_only_files:
        print(f"\nFiles copied:")
        for f in text_only_files:
            print(f"  - {f}")

if __name__ == "__main__":
    main()
