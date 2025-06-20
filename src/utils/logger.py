from datetime import datetime
import os


class Logger:

    def __write_log(self, type: str, message: str):
        log_dir = os.path.join(os.path.dirname(__file__), "../../logs")
        os.makedirs(log_dir, exist_ok=True)
        log_path = os.path.join(log_dir, "execucao.log")
        with open(log_path, "a", encoding="utf-8") as file:
            now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            file.write(f"[{type}] - {now} - {message}\n")

    def info(self, message: str) -> None:
        self.__write_log("INFO", message)

    def error(self, message: str) -> None:
        self.__write_log("ERROR", message)

    def warning(self, message: str) -> None:
        self.__write_log("WARNING", message)
