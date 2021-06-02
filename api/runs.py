import yaml
from api.client import Client


api_client = Client()


def get_all_runs(argv):
    repo = argv[0]
    branch = argv[1] if len(argv) > 1 else 'master'

    params = {
        'branch': branch,
        'page': 1,
        'per_page': 50
    }

    runs = []

    while True:
        response = api_client.get('repos/' + repo + '/actions/runs', params)

        if len(response['workflow_runs']) == 0:
            break

        runs = runs + response['workflow_runs']
        params['page'] += 1
        print('Retrieved {} of {}'.format(len(runs), response['total_count']))

    return runs


def get_last_run(argv):
    repo = argv[0]
    branch = argv[1] if len(argv) > 1 else 'master'

    params = {
        'branch': branch,
        'page': 1,
        'per_page': 1
    }

    response = api_client.get('repos/' + repo + '/actions/runs', params)
    return response['workflow_runs']


def get_repos_status(argv):
    config = yaml.safe_load(open('config.yml'))

    repos = argv if len(argv) else config['all_repos']
    params = {
        'page': 1,
        'per_page': 1
    }

    runs = []
    for repo in repos:
        response = api_client.get('repos/' + repo + '/actions/runs', params)

        # if 'message' in response & response['message'] == 'Not Found':
        if response.get('message') == 'Not Found':
            raise Exception(f"repository '{repo}' not found")

        runs = runs + response['workflow_runs']

    return runs
