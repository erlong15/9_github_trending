from datetime import datetime, timedelta
import requests
import argparse


def get_date_week_ago_as_str():
    return (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')


def get_json_from_api(url):
    response = requests.get(url)
    return response.json()['items']


def extract_repo_info(repo_info):
    need_keys = ['full_name',
                 'url',
                 'description',
                 'has_issues',
                 'issues_url']
    return dict(filter(lambda x: x[0] in need_keys, repo_info.items()))


def get_trending_repositories(url, top_size):
    return map(extract_repo_info, sorted(
        get_json_from_api(url),
        key=lambda x: x['stargazers_count'])[:top_size])


def get_open_issues_amount(issues_url):
    fixed_url = issues_url.replace('{/number}', '')
    response = requests.get(fixed_url)
    return len(response.json())


def get_args():
    parser = argparse.ArgumentParser(description='githiub trends watcher.')
    parser.add_argument('-c', '--count',
                        help='How much repos do you want to see (default: 5)',
                        required=False,
                        default=5)
    return parser.parse_args()


def format_output_str(repo_info):
    output = """
    Repository: {full_name}
    URL: {url}
    Description: {description}
    Issues: {issues_count}
    """.format(**repo_info)

    return output

if __name__ == '__main__':
    args = get_args()
    repo_api = 'https://api.github.com/search/repositories?q=created:>{dt}'

    repo_url = repo_api.format(dt=get_date_week_ago_as_str())

    for repo in get_trending_repositories(repo_url, args.count):
        repo['issues_count'] = get_open_issues_amount(repo['issues_url']) \
            if repo['has_issues'] else 0
        print(format_output_str(repo))
