from threading import Thread
from fetchers import get_best_format, get_lowest_format, get_thumbnail

def handle_command(args):

    if args.t:
        Thread(
            target=get_thumbnail,
            args=(args.url, )
        ).start()

    elif args.b:
        Thread(
            target=get_best_format, 
            args=(args.url, )
            ).start()

    elif args.l:
        Thread(
            target=get_lowest_format, 
            args=(args.url, )
            ).start()

    else:
        print('no arguments passed')

