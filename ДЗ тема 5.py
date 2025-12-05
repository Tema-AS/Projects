from datetime import datetime

def parse_date(date_str, format_str):
    try:
        return datetime.strptime(date_str, format_str)
    except ValueError as e:
        print(f"Ошибка: {e}")
        return None

def main():
    formats = {
        "The Moscow Times": "%A, %B %d, %Y",
        "The Guardian": "%A, %d.%m.%y",
        "Daily News": "%A, %d %B %Y"
    }

    while True:
        newspaper = input("Введите название газеты (The Moscow Times / The Guardian / Daily News) или 'quit' для выхода: ")
        if newspaper.lower() == 'quit':
            break

        if newspaper not in formats:
            print("Неизвестная газета. Попробуйте ещё раз.")
            continue

        date_str = input(f"Введите дату для {newspaper}: ")
        parsed_date = parse_date(date_str, formats[newspaper])

        if parsed_date:
            print(f"Объект datetime: {parsed_date}")
            print(f"Дата в формате ISO: {parsed_date.isoformat()}")

if __name__ == "__main__":
    main()
