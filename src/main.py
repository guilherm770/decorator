import functools
import time


def retry(tries=3, delay=1, backoff=2):
    """
    Decorador que permite a reexecução de uma função em caso de falha.

    Parâmetros:
    - tries (int, opcional): O número máximo de tentativas. O padrão é 3.
    - delay (float, opcional): O tempo de espera inicial entre as tentativas, em segundos. O padrão é 1.
    - backoff (float, opcional): O fator de multiplicação para aumentar o tempo de espera em cada tentativa subsequente.
                                O tempo de espera é calculado como delay * (backoff ** (tentativa - 1)). O padrão é 2.

    """
    def decorator_retry(func):
        @functools.wraps(func)
        def wrapper_retry(*args, **kwargs):
            current_delay = delay
            for attempt in range(tries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print("Attempt %d: %s" % (attempt + 1, str(e)))
                    time.sleep(current_delay)
                    current_delay *= backoff
            return []
        return wrapper_retry
    return decorator_retry

@retry(tries=1, delay=2, backoff=2)
def my_func(num):
    if num % 2 == 0:
        print('No retry')
    else:
        raise Exception('Retry')

for i in range(0,5,1):
    my_func(i)