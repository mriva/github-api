import os


def get_token():
    token_path = os.path.expanduser('~/.github_token')
    if os.path.exists(token_path):
        with open(token_path) as f:
            token = f.read().strip()
            return token
    elif os.environ.get('GITHUB_TOKEN'):
        return os.environ.get('GITHUB_TOKEN')
    else:
        raise Exception('No token found')
