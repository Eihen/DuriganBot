from telegram.ext import CommandHandler
import random as randlib


# /random
def random(args):
    # If arg[2] is not supplied or is 0 then n is 1, else it's arg[2]
    n = max(1, int(args[2])) if len(args) >= 3 else 1

    # No parameters [0, 100]
    if not args:
        a = 0
        b = 100
    else:
        args[0] = int(args[0])

        # One parameter
        if len(args) == 1:
            args[0] = int(args[0])

            # args[0] < 0 -> [args[0], 0]
            if args[0] > 0:
                a = 0
                b = args[0]

            # args[0] > 0 -> [0, args[0]]
            else:
                a = args[0]
                b = 0

        # Two parameters
        else:
            args[1] = int(args[1])

            # args[0] < args[1] -> [args[0], args[1]]
            if args[0] < args[1]:
                a = args[0]
                b = args[1]

            # args[0] >= args[1] -> [args[1], args[0]]
            else:
                a = args[1]
                b = args[0]

    rand = []
    # Generate N numbers on the range [a, b]
    for i in range(0, n):
        rand.append(randlib.randint(a, b))

    return rand


def random_handler(bot, update, args):
    try:
        update.message.reply_text(' '.join(str(r) for r in random(args)))
    except ValueError:
        # if an error occurs reply with a random number in the range [0, 100]
        update.message.reply_text(
            'Something went wrong, so I hope this random number helps: ' +
            str(randlib.randint(0, 100))
        )


def add_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler('random', random_handler, pass_args=True))
