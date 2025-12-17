import csv

class ClientFormatter:
    SEX_DICT = {
        "male": "совершил",
        "female": "совершила"
    }

    DEVICE_DICT = {
        "laptop": "ноутбука",
        "desktop": "персонального компьютера",
        "tablet": "планшета",
        "mobile": "мобильного устройства"
    }

    @staticmethod
    def format_age(age: str) -> str:
        try:
            age_int = int(age)
        except ValueError:
            return "лет"

        if 11 <= (age_int % 100) <= 14:
            return "лет"
        last_digit = age_int % 10

        if last_digit == 1:
            return "год"
        if 2 <= age_int <= 4:
            return "года"
        return "лет"

    @staticmethod
    def format_sex(sex: str) -> str:
        return "женского" if sex == "female" else "мужского"


class Client:
    def __init__(self, name, device_type, browser, sex, age, bill, region):
        self.name = name
        self.device_type = device_type
        self.browser = browser
        self.sex = sex
        self.age = age
        self.bill = bill
        self.region = region

    def format_description(self):
        sex = ClientFormatter.format_sex(self.sex)
        age_word = ClientFormatter.format_age(self.age)
        sex_word = ClientFormatter.SEX_DICT.get(self.sex, "совершил(а)")
        device = ClientFormatter.DEVICE_DICT.get(self.device_type, "устройства")
        region = "неизвестно" if not self.region or len(self.region.strip()) == 1 else self.region
        return (
            f"Пользователь {self.name} {sex} пола, "
            f"{self.age} {age_word} {sex_word} покупку на "
            f"{self.bill} y.e. "
            f"с {device} в браузере "
            f"{self.browser}. "
            f"Регион, из которого совершалась покупка: {region}"
        )


def main():
    try:
        with open("web_clients_correct.csv", "r", encoding="utf-8") as clients_csv:
            reader = csv.reader(clients_csv)
            next(reader)

            with open("results.txt", "w", encoding="utf-8") as result_file:
                for row in reader:
                    client = Client(*row)
                    result_file.write(client.format_description() + "\n")
    except FileNotFoundError:
        print("Файл web_clients_correct.csv не найден")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")


main()




