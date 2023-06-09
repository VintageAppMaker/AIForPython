from console import Console

def main():
    console = Console()
    name = console.input("이름을 입력하세요: ")
    console.print(f"안녕하세요, {name}!")

if __name__ == "__main__":
    main()