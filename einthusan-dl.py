import click
import requests


def api_calls(query_url):
    url = 'https://lit-anchorage-62847.herokuapp.com/api/info?url='
    full_url = url + query_url
    data = requests.get(full_url).json()['info']['formats'][0]['url']
    return data


@click.command()
@click.argument('query_url')
def main(query_url):
    streaming_url = api_calls(query_url)
    print(streaming_url)


if __name__ == "__main__":
    main()
