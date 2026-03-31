import subprocess

def list_directory(path="."):
    result = subprocess.run(["ls", "-ls", path])
    return result

def read_file(filepath):
    result = subprocess.run(["cat", filepath], capture_output=True, text=True)

    if result.returncode == 0:
        return result.stdout
    else:
        return f"Error reading file: {result.stderr}"
    
@tool
def search_codebase(search_term: str, path: str =  "."):
    """Searches the codebase for a specific string or function name."""
    result = subprocess.run(["grep", "-rnI", search_term, path], capture_output=True, text=True)
    
    if result.returncode == 0:
        return result.stdout
    else:
        return f"No results found for '{search_term}'."