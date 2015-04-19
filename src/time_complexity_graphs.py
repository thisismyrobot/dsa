""" Time complexity testing.
"""
import importlib
import os
import matplotlib.pyplot
import operator
import timeit

CONFIG = {
    'singly_linked_list': {
        'search': {
            'worst_case': {
                'instance_class': lambda module: module.SinglyLinkedList,
                'data_generator': lambda module, size: [module.Node(value)
                                                        for value
                                                        in range(0, size)],
                'needle': lambda module: module.Node('needle'),
                'operation': lambda haystack, needle: operator.setitem(
                    haystack, len(haystack) - 1, needle
                ),
                'callable': lambda instance, needle: instance.exists(needle),
            }
        }
    }
}


def get_mod(mod_name):
    return importlib.import_module(mod_name)


def generate():
    """ Generate the graphs.
    """
    for (mod_name, operations) in CONFIG.items():
        mod = get_mod(mod_name)

        for operation, cases in operations.items():

            for (case, config) in cases.items():

                results = []

                for size in range(0, 1000, 10):

                    if size == 0:
                        results.append((0, 0))
                        continue

                    # The haystack we'll work within
                    haystack = config['data_generator'](mod, size)

                    # The needle we're interested in
                    needle = config['needle'](mod)

                    # Manipulate the haystack appropriately to insert the
                    # needle.
                    config['operation'](haystack, needle)

                    # Create an instance of the module
                    inst = config['instance_class'](mod)()

                    # All implementations support a 'populate' method for the
                    # purposes of efficient testing. This method is not timed
                    # and is not part of the complexity calculation - it only
                    # serves to pre-fill the implementation.
                    inst.populate(haystack)

                    config['callable'](inst, needle)

                    result = timeit.timeit(
                        lambda: config['callable'](inst, needle),
                        number=1000,
                    )

                    results.append((size, result))

                matplotlib.pyplot.plot(*zip(*results))
                matplotlib.pyplot.savefig(
                    os.path.join(
                        '..',
                        'graphs',
                        ' - '.join((mod_name, operation, case)) + '.png'
                    )
                )


if __name__ == '__main__':
    generate()
