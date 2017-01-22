
import abc, math
import numpy as np

class WaveFunction(object):

    def __init__(self):
        pass

    @abc.abstractmethod
    def measure(self):
        '''
        when a measurement is made to certain wavefunction, it will collapse and generate probablity
        :return:
        '''
        raise NotImplementedError()


class ChilarityState(WaveFunction):

    hadamard_operator = np.array(
    [[1 / math.sqrt(2.0),   1 / math.sqrt(2.0)], \
     [1 / math.sqrt(2.0), - 1 / math.sqrt(2.0)] ], dtype=complex )

    def __init__(self, left, right):
        self.__state = np.array([left, right], dtype=complex)

    def on_hadarmard_operator(self):
        return self.hadamard_operator.dot(self.__state)

    def set_left(self, num):
        self.__state[0] = num

    def set_right(self, num):
        self.__state[1] = num

    def measure(self):
        return np.dot(self.__state, self.__state.conjugate())

    def __str__(self):
        return 'left:' + str(self.__state[0]) + ',' + 'right:' + str(self.__state[1])

