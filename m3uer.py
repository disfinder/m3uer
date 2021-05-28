#!/usr/bin/env python3
import sys, os, logging

KNOWN_EXTENTIONS = [
    '.mp3',
    'cue'
]


def gather_files(path):
    result = []
    for root, dirs, files in os.walk(path):
        for file in files:
            # special hack for macos fnames:
            # https://stackoverflow.com/questions/59306977/macos-os-listdir-returns-double-items-which-starts-with
            if not file.startswith('._'):
                _, extention = os.path.splitext(file)
                if extention.lower() in KNOWN_EXTENTIONS:
                    unixfname = "{}/{}".format(root.replace(path, ''), file).lstrip('/')
                    windows_fname = unixfname.replace('/', '\\')
                    result.append(windows_fname)
    return result


def print_result(file_list):
    print('#EXTM3U')
    for filename in file_list:
        print('#EXTINF: 0, {}'.format(filename.split('\\')[-1]))
        print(filename)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info('Start searching...')
    path = '.'
    if len(sys.argv) > 1:
        path = sys.argv[1]
    files_list = gather_files(path)
    logging.info('Gathered {} files'.format(len(files_list)))
    print_result(files_list)
    logging.info('Done.')
