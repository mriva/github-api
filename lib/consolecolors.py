class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def color_status(status):
    if status == 'success':
        color = Colors.GREEN
    elif status == 'failure':
        color = Colors.RED
    else:
        color = Colors.YELLOW

    return color + status + Colors.END
