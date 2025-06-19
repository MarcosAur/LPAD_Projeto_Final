from datetime import datetime


class Logger:

    def __write_log(self, type: str, message: str):
        with open("../logs/execucao.log", "a") as file:
            now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            file.write(f"[{type}] - {now} - {message}\n")

    def info(self, message: str) -> None:
        self.__write_log("INFO", message)

    def error(self, message: str) -> None:
        self.__write_log("ERROR", message)

    def warning(self, message: str) -> None:
        self.__write_log("WARNING", message)
