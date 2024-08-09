
import time

async def dummy_func(msg):
    print('dorme 1 sec')
    time.sleep(1)
    print(f'mensagem:{msg}')
    is_ok = True

    if not is_ok:
        is_ok = False
        raise('QUALQUER EXCEPTION AQUI...')

    return is_ok
