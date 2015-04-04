# -*- coding: utf-8 -*-
__author__ = 'Albéric'
from random import getrandbits, randint


# -------------------------------------------------------------------------------
def verbal(some_class):
    """intended as a class decorator allowing to list all attributes and where
    they come from"""

    def tell(inst):
        print(
            "{:>16}: {}\n".format("instance", ", ".join(
                a for a in vars(inst) if not a.startswith("__"))
                                  ) +
            "".join([
                "{:>16}: {}\n".format(cls.__name__, ", ".join(
                    sorted([a for a in vars(cls) if not a.startswith("__")])
                )) for cls in type(inst).__mro__
            ]) +
            "{:>16}: {}\n".format(type(type(inst)).__name__, ", ".join(
                a for a in vars(type(type(inst))) if not a.startswith("__"))
                                  )
        )

    some_class.tell = tell
    return some_class


# -------------------------------------------------------------------------------


class GeneticClass():
    def __init__(self):
        self.genome = [getrandbits(self.b_genes) for gene in
                       range(self.n_genes)]

    def mutate(self):
        """Applies n_mutations randomly to the genome"""
        for mutation in range(self.mutability):
            self.genome[randint(0, len(self.genome) - 1)] = getrandbits(
                self.b_genes)


def genetic(specie="GenericSpecie",
            number_of_genes=10,
            bits_per_gene=1,
            mutations=5):
    """
    class decorator, makes a template for altering classes
    and allowing genetic algorithms on them
    """
    dictionary = {'specie': specie,
                  'n_genes': number_of_genes,
                  'b_genes': bits_per_gene,
                  'mutability': mutations}

    def genetic_helper(cls):
        #return type(cls.__name__, (cls, GeneticClass), dictionary)
        return type(cls.__name__, (cls, GeneticClass), dictionary)

    return genetic_helper


@verbal
@genetic("10_genes", mutations=3)
class PlaceHolder:
    pass


@verbal
@genetic("papa", mutations=3)
class PaPaLoom():
    pass


if __name__ == "__main__":
    PlaceHolder().tell()