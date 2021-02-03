from telegram.ext import CommandHandler
import logging as log
import random


def handle_rand_args(args):
    # No parameters [0, 100]
    if not args:
        a = 0.
        b = 100.
        n = 1
    else:
        # One parameter
        if len(args) == 1:
            # args[0] > 0 -> [0, args[0]]
            if args[0] > '0':
                a = 0.
                b = float(args[0])

            # args[0] <= 0 -> [args[0], 0]
            else:
                a = float(args[0])
                b = 0.

            n = 1

        # Two parameters or more
        else:
            # args[0] < args[1] -> [args[0], args[1]]
            if args[0] < args[1]:
                a = float(args[0])
                b = float(args[1])

            # args[0] >= args[1] -> [args[1], args[0]]
            else:
                a = float(args[1])
                b = float(args[0])

            n = max(1, round(float(args[2]))) if len(args) > 2 else 1

    return [a, b, n]


# /rand
def rand(args):
    result = []
    # Generate N integers on the range [a, b]
    for i in range(0, args[2]):
        result.append(random.randint(round(args[0]), round(args[1])))

    return result


def rand_handler(bot, update, args):
    try:
        rand_args = handle_rand_args(args);
        update.message.reply_text(' '.join(str(r) for r in rand(rand_args)))
    except ValueError:
        # if an error occurs reply with a random number in the range [0, 100]
        update.message.reply_text(
            'Something went wrong, so I hope this random number helps: ' +
            str(random.randint(0, 100))
        )
        log.exception(' '.join(str(r) for r in rand_args));


# /randf
def randf(args):
    result = []
    # Generate N floats on the range [a, b]
    for i in range(0, args[2]):
        result.append(random.uniform(args[0], args[1]))

    return result


def randf_handler(bot, update, args):
    try:
        rand_args = handle_rand_args(args);
        update.message.reply_text(' '.join(str(r) for r in randf(rand_args)))
    except ValueError:
        # if an error occurs reply with a random number in the range [0, 100]
        update.message.reply_text(
            'Something went wrong, so I hope this random number helps: ' +
            str(random.uniform(0, 100))
        )
        log.exception(' '.join(str(r) for r in rand_args));


def add_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler('rand', rand_handler, pass_args=True))
    dispatcher.add_handler(CommandHandler('randf', randf_handler, pass_args=True))
