import urllib.request
import re


class MyFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

        modes = ["read", "write", "append", "url"]

        if mode not in modes:
            raise ValueError("Введён неподдерживаемый тип работы с файлом")
        if mode == "url":
            self.url = True
        else:
            self.url = False

    def read(self):
        if self.mode != "read":
            raise TypeError("Выбранный тип работы файла не поддерживает чтение")
        file = open(self.filename, "r")
        return file.read()


    def write(self, string):
        if self.mode not in ["write", "append"]:
            raise TypeError("Выбранный тип работы файла не поддерживает запись")
        if self.mode == "append":
            file = open(self.filename, "a")
            file.write(string)
            return string
        if self.mode == "write":
            file = open(self.filename, "w")
            file.write(string)
            return string


    def read_url(self):
        if (self.url == False):
            raise TypeError("Выбранный тип работы файла не поддерживает работу с URL")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        req = urllib.request.Request(self.filename, headers=headers)
        response = urllib.request.urlopen(req)
        content = response.read().decode('utf-8')
        return content


    def count_urls(self):
        if (self.url == False):
            raise TypeError("Выбранный тип работы файла не поддерживает работу с URL")
        pattern = re.compile(
            r'''href=["'](https?://[^"'\s>]+)["']|'''  # href атрибуты
            r'''src=["'](https?://[^"'\s>]+)["']|'''  # src атрибуты
            r'''url\(["']?(https?://[^"'\s)]+)["']?\)''',  # url() в CSS
            re.IGNORECASE
        )
        return len(set(pattern.findall(self.read_url())))

    def write_url(self, target):
        if (self.url == False):
            raise TypeError("Выбранный тип работы файла не поддерживает работу с URL")
        file = open(target, "w")
        file.write(self.read_url())


file = MyFile("text.txt", "read")
text = file.read() # происходит чтение в виде str
print(text)

file = MyFile("text.txt", "write")
text = file.write("привет!") # происходит запись строки в файл

file = MyFile("text.txt", "append")
text = file.write("привет!") # происходит добавление строки в конец файла

# указали URL
file = MyFile("https://dfedorov.spb.ru", "url")
# и может читать содержимое страницы по указанному URL
text = file.read_url() # происходит чтение в виде str
print(text)

# возвращает кол-во url адресов на странице, например, методом count
count = file.count_urls()
print(count)

# происходит запись содержимого страницы по URL в указанный файл
file.write_url("text.txt")
