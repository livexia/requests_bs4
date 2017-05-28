import os


def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)


def create_data_files(name, base_url):
    queue = os.path.join(name + '_queue.txt')
    crawled = os.path.join(name + "_crawled.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


def delete_file_contents(path):
    with open(path, 'w').close():
        pass


def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


def set_to_file(links, file_name):
    with open(file_name, "w") as f:
        for l in sorted(links):
            f.write(l+"\n")


def file_to_list(file_name):
    results = []
    with open(file_name, 'rt') as f:
        for line in f:
            results.append(line.replace('\n', ''))
    return results


def list_to_file(links, file_name):
    with open(file_name, "w") as f:
        for l in links:
            f.write(l+"\n")


def truncate_file(file_name):
    with open(file_name, "w") as f:
        f.truncate()


def print_info(info):
    for key in info:
        print('歌曲id：', key)
        print('     歌曲标题：'+info[key][0])
        print('     歌手：'+info[key][1])
        print('     歌手id：', info[key][2])
        print('     专辑：'+info[key][3])
        print('     专辑id：', info[key][4])
        print('     Url：')
        print('          歌曲链接：'+info[key][5][0])
        print('          歌手链接：'+info[key][5][1])
        print('          专辑链接：'+info[key][5][2])
        print('          专辑图片：', info[key][5][3])