import numpy as np
from numpy import random

class Plant:

    def __init__(self, location, params):
        """
        Creates a new plant at the given location.

        location: tuple coordinates
        params: dictionary of parameters

        loc: (x,y) location on grid of object
        age: number of steps plant has been alive, incremented each step
        size: 'vertical height' of plant (used to determine survival when fighting for resources)
        type: species of plant
        lifespan: Age at which the plant will die
        resilience: Constant used to determine survival when fighting for limited resources
        growth_rate: The amount in which size will be increased by every step
        reproduction_rate: For any of the 8 neighbours, if unoccupied, the chance that a new plant of the same type will appear 

        """
        self.genes = params
        self.loc = tuple(location)
        self.age = 0
        self.size = 0
        self.type = params["type"]
        self.lifespan = int(np.random.uniform(params["min_lifespan"], params["max_lifespan"]))
        self.resilience = np.random.uniform(params["min_resilience"], params["max_resilience"])
        self.growth_rate = np.random.uniform(params["min_growth_rate"], params["max_growth_rate"])
        self.reproduction_rate = np.random.uniform(params["min_reproduction_rate"], params["max_reproduction_rate"])

    def step(self):
        #PLACEHOLDER
        self.age += 1
        self.size = self.size + self.growth_rate
        return 0
    
    def reproduce(self, ecosystem):
        # return a list of plants of the same type to be input into the eco
        empty_neighbours = ecosystem.get_empty_neighbours(self)
        if(len(empty_neighbours) == 0):
            return []
        offspring = []
        for empty_neighbour in empty_neighbours:
            random_zero_to_one = random.random()
            if random_zero_to_one < self.reproduction_rate:
                # generate a new agent
                temp_plant = Plant(empty_neighbour, self.genes)
                offspring.append(temp_plant)
        return offspring
    
    def is_old(self):
        return self.age >= self.lifespan
    
