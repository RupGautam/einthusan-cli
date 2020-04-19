import random
import re
import sys

import click
import requests

check_mark = "\033[92m✔\033[0m"
erase_line = "\x1b[2K"


def api_calls(query_url):
    url = 'https://einthusan-cli.herokuapp.com/api/info?url='
    # full_url = url + query_url
    full_url = 'http://0.0.0.0:8000/out.json'
    url = requests.get(full_url).json()['info']['formats'][0]['url']
    return {
        'url': url
    }


def download(url, filename):
    with open(filename, 'wb') as f:
        r = requests.get(url, stream=True)
        total = r.headers.get('content-length')
        if total is None:
            f.write(r.content)
        else:
            downloaded = 0
            total = int(total)
            for data in r.iter_content(chunk_size=max(int(total/1024), 1024 * 1024)):
                downloaded += len(data)
                f.write(data)
                done = int(50 * downloaded / total)
                sys.stdout.write('\r[{}{}]'.format(
                    '█' * done, '.' * (50-done)))
                sys.stdout.flush()
    sys.stdout.write('\n')


@click.command()
@click.argument('url')
@click.argument('filename')
def main(url, filename):
    print('Fetching streaming URL..', end='\r', flush=True)
    sys.stdout.write(erase_line)
    movie_url = api_calls(url)
    print(check_mark, movie_url['url'])

    movie = download(movie_url['url'], filename)


if __name__ == "__main__":
    main()
