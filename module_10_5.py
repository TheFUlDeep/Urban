import time, datetime, multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            if line == '':
                break
            all_data.append(line)


def get_files():
    yield from ("file " + str(x) + '.txt' for x in range(1, 5))


def main():
    started_at = time.time()
    for file in get_files():
        read_info(file)
    print(f'{datetime.timedelta(seconds=time.time() - started_at)} (линейный)')

    processes = [multiprocessing.Process(target=read_info, args=(file,)) for file in get_files()]

    started_at = time.time()
    for process in processes:
        process.start()

    for process in processes:
        process.join()
    print(f'{datetime.timedelta(seconds=time.time() - started_at)} (многопроцессорный)')


if __name__ == "__main__":
    main()
