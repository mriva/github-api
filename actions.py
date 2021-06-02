import sys
from api.datetimeutils import localized_timestamp
from api.runs import *
from tabulate import tabulate

try:
    command = sys.argv[1]
except IndexError:
    raise SystemExit(f"Usage: {sys.argv[0]} <command> [command parameters]")

dispatch = {
    'last': get_last_run,
    'all': get_all_runs,
    'status': get_repos_status
}

try:
    if len(sys.argv) > 2:
        args = sys.argv[2:]
    else:
        args = []

    response = dispatch[command](args)
except Exception as e:
    raise e

count = 1

headers = ['nr', 'repository', 'result', 'branch', 'timestamp', 'committer', 'message']
table_data = []

for run in response:
    message = run['head_commit']['message'].split('\n')[0]
    timestamp = localized_timestamp(run['created_at'])

    table_data.append([
        count,
        run['repository']['full_name'],
        run['conclusion'] if run['conclusion'] else run['status'],
        run['head_branch'],
        timestamp.strftime('%Y-%m-%d %H:%M:%S%z'),
        run['head_commit']['author']['name'],
        message
    ])

    count += 1

print(tabulate(table_data, headers, tablefmt="grid"))
