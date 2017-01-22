
import math
import states

class OneDimensionalWalker(object):

    def __init__(self, max_steps):
        '''
        e.g. for a walk with maxinum 100 steps, an array of 100(left) + 100(right) + 1(original) is needed

        :param max_steps:
        '''
        self.__original_index = max_steps
        self.__max_steps = max_steps
        self.__evolved_steps  = 0
        self.__is_finished = (max_steps == 0)

        self.__map = self.create_fresh_map()
        self.__map[self.__original_index].set_left(1.0 / math.sqrt(2.0))
        self.__map[self.__original_index].set_right(1.0j / math.sqrt(2.0))

    def get_state(self, index, direction = 'l'):
        assert(direction == 'l' or direction == 'r')
        index = self.__original_index + (-index if direction == 'l' else index)
        return self.__map[index]

    def evolve(self):
        if self.__is_finished:
            return

        newmap = self.create_fresh_map()
        idx = -self.__max_steps
        for state in self.__map:
            transformed = self.__map[idx + self.__max_steps].on_hadarmard_operator()
            if idx - 1 >= -self.__max_steps:
                newmap[idx - 1 + self.__max_steps].set_left(transformed[0])
            if idx +1  <= self.__max_steps:
                newmap[idx + 1 + self.__max_steps].set_right(transformed[1])
            idx += 1

        self.__map = newmap
        self.__evolved_steps += 1
        self.__is_finished = self.__evolved_steps >= self.__max_steps

    def finish(self):
        while not self.__is_finished:
            self.evolve()  # evolve one step after one step

    def get_probability_distribution(self):
        start = -self.__max_steps
        end   = self.__max_steps
        return (range(start, end), [self.__map[index+self.__max_steps].measure() for index in range(start, end)])

    def create_fresh_map(self):
        return [states.ChilarityState(0.0,0.0) for i in range(self.__max_steps * 2 + 1)]

