#!/usr/bin/env python3
import sys
import re
import os

def update_version(new_version):
    # Update version in __init__.py
    init_file = 'allievo/__init__.py'
    
    with open(init_file, 'r') as f:
        content = f.read()
    
    # Replace version string
    new_content = re.sub(
        r'__version__ = ["\'][^"\']*["\']',
        f'__version__ = "{new_version}"',
        content
    )
    
    with open(init_file, 'w') as f:
        f.write(new_content)
    
    # Update version in pyproject.toml
    pyproject_file = 'pyproject.toml'
    
    with open(pyproject_file, 'r') as f:
        content = f.read()
    
    # Replace version in pyproject.toml
    new_content = re.sub(
        r'version = ["\'][^"\']*["\']',
        f'version = "{new_version}"',
        content
    )
    
    with open(pyproject_file, 'w') as f:
        f.write(new_content)
    
    print(f"Updated version to {new_version} in both __init__.py and pyproject.toml")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: update_version.py <version>")
        sys.exit(1)
    
    version = sys.argv[1]
    update_version(version)
