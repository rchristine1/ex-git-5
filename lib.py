from datetime import datetime
def generate_log(params):

    with open('logs.txt', 'a') as f:

        f.write('on a appelé la fonction moyenne {} avec les parametres {}\n'.format(
            datetime.now(), params)
        )


def moyenne(values):

    generate_log(values)

    return sum(values) /len(values)