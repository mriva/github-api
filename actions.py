import sys
from tabulate import tabulate
from lib.datetimeutils import *
from lib.consolecolors import colored_status
from api.runs import *


dispatch = {
    'last': get_last_run,
    'all': get_all_runs,
    'status': get_repos_status
}

try:
    command = sys.argv[1]

    if command not in dispatch:
        print(f"Command '{command}' is not defined.")
        exit(1)
except IndexError:
    raise SystemExit(f"Usage: {sys.argv[0]} <command> [command parameters]")


if len(sys.argv) > 2:
    args = sys.argv[2:]
else:
    args = []

response = dispatch[command](args)

headers = ['nr', 'repository', 'result', 'branch', 'commit', 'timestamp', 'duration', 'committer', 'message']
table_data = []
count = 1

for run in response:
    message = run['head_commit']['message'].split('\n')[0]
    timestamp = localized_timestamp(run['created_at'])
    timestamp_end = localized_timestamp(run['updated_at'])

    table_data.append([
        count,
        run['repository']['full_name'],
        colored_status(run['conclusion'] if run['conclusion'] else run['status']),
        run['head_branch'],
        run['head_sha'][:7],
        timestamp.strftime('%Y-%m-%d %H:%M:%S%z'),
        timestamp_diff(run['created_at'], run['updated_at']),
        run['head_commit']['author']['name'],
        message
    ])

    count += 1

print(tabulate(table_data, headers, tablefmt="grid"))
