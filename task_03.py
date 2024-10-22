from pathlib import Path
from colorama import init, Fore
import sys

def directory_structure_visualizer():
    try:
        if len(sys.argv) <= 1:
            print(f'{Fore.RED}Required arguments are missing')
            return
        
        directory = Path(sys.argv[1])

        if not directory.exists() or not directory.is_dir():
            print(f'{Fore.RED}Path does not exist or is not a directory.')
            return
        
        def recursive_print(current_path, indent_level=0):
            for item in current_path.iterdir():
                indent = ' ' * 4 * indent_level
                if item.is_dir():
                    print(f'{indent}{Fore.BLUE}{item.name}/')
                    recursive_print(item, indent_level + 1)
                else:
                    print(f'{indent}{Fore.GREEN}{item.name}')
        
        recursive_print(directory)
        
    except Exception as e:
        print(f'{Fore.RED}An unexpected error occurred: {e}')

if __name__ == '__main__':
    init(autoreset=True)
    directory_structure_visualizer()