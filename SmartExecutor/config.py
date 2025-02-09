class Config:

    MAX_THREADS = 8         # nombre maximum de threads pour les tâches I/O-bound
    MAX_PROCESSES = 4       # nombre maximum de processus pour les tâches CPU-bound
    LOG_LEVEL = "DEBUG"     # niveau de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    LOG_FILE = "smartexecutor.log"

    @classmethod
    def set_max_threads(cls, num: int):
        cls.MAX_THREADS = num

    @classmethod
    def set_max_processes(cls, num: int):
        cls.MAX_PROCESSES = num

    @classmethod
    def set_log_level(cls, level: str):
        cls.LOG_LEVEL = level

    @classmethod
    def set_log_file(cls, file_name: str):
        cls.LOG_FILE = file_name
