"""
    Module-level docstring start
"""


class Individual(object):
    """
        Class Docstring

        NEAT Responsibilities:
            1. Maintain a Genome
            2. Track their fitness each generation
        Data Reporting/Visualization Responsibilities:
            1. Increment and track their global number (Increment on construction, don't copy or rebuild the individuals)
    """
    num_created = 0

    def __init__(self, genome, bias):
        super().__init__()
        Individual.num_created += 1
        self.id = Individual.num_created
        self.genome = genome
        self.genome.assemble_topology()
        self.fitness = 0
        self.assigned_specie = None
        self.kBias_node = bias

    def evaluate(self, inputs):
        """
        :param inputs:
        :return:
        """
        if self.kBias_node:
            inputs = [1.0] + inputs
        return self.genome.evaluate(inputs)

    def frame(self, inputs):
        # In certain applications a frame is a more intuitive concept than evaluate
        return self.evaluate(inputs)
