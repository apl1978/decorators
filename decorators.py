from datetime import datetime


def write_to_log(some_function):
    def new_function(*args, **kwargs):
        result = some_function(*args, **kwargs)
        LOG_PATH = 'logs/log.txt'
        with open(LOG_PATH, 'a') as file_log:
            str_log = f'{datetime.now()} | function: {some_function.__name__} args: {args}, kwargs: {kwargs}, result: {result} \n'
            file_log.write(str_log)
        return result

    return new_function

def write_to_log_path(path):
    def _write_to_log(some_function):
        def new_function(*args, **kwargs):
            result = some_function(*args, **kwargs)
            with open(path, 'a') as file_log:
                str_log = f'{datetime.now()} | function: {some_function.__name__} args: {args}, kwargs: {kwargs}, result: {result} \n'
                file_log.write(str_log)
            return result

        return new_function
    return _write_to_log