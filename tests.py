from functions.get_files_info import get_files_info

def main():
    try:
        result = get_files_info("calculator", ".")
        print(result)            
    except Exception as e:
        print(e)

    try:
        result = get_files_info("calculator", "pkg")
        print(result)            
    except Exception as e:
        print(e)

    try:
        result = get_files_info("calculator", "/bin")
        print(result)            
    except Exception as e:
        print(e)

    try:
        result = get_files_info("calculator", "../")
        print(result)            
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()