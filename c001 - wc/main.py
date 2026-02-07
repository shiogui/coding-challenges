import sys, os, re

def count_bytes(file_name):
    try:
        size = os.path.getsize(file_name)
        print(f"{size} {file_name}")
    except FileNotFoundError:
        print(f"Error: The file {file_name} wasn't found.")
    except Exception as e:
        print(f"Error: {e}")

def count_lines(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = len(file.readlines())
        print(f"{lines} {file_name}")
    except FileNotFoundError:
        print(f"Error: The file {file_name} wasn't found.")
    except Exception as e:
        print(f"Error: {e}")

def count_words(file_name):
    try:
        with open(file_name, 'r') as file:
            words = [x for x in re.split("\n|\t| ", file.read()) if x != ""]
        print(f"{len(words)} {file_name}")
    except FileNotFoundError:
        print(f"Error: The file {file_name} wasn't found.")
    except Exception as e:
        print(f"Error: {e}")

def main(argv: list[str]):
    if len(argv) < 3:
        print("Error: Missing parameters, you need to pass flag + file name.")
        return

    flag, file_name = argv[1:]

    match flag:
        case "-c":
            count_bytes(file_name)
        case "-l":
            count_lines(file_name)
        case "-w":
            count_words(file_name)
        case _:
            print(f"The `{flag}` flag is not a known option.")

if __name__ == "__main__":
    main(sys.argv)
