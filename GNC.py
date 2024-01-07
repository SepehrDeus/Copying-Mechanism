import numpy as np
import random
from matplotlib import pyplot as plt


class GNC:

    def __init__(self, N):
        self.N = N
        self.L = 0
        self.links = list()
        self.in_deg = np.zeros(N)
        self.out_deg = np.zeros(N)
        self.create_network()

    def create_network(self):
        for node in range(1, self.N):
            self.add_node(node)

    def add_node(self, node):
        target = random.randint(0, node - 1)
        self.add_link(node, target)   # connect to target
        self.connect_to_ancestors(node, target)

    def connect_to_ancestors(self, node, target):
        ancestors = self.find_ancestors(target)
        for ancestor in ancestors:
            self.add_link(node, ancestor)

    def find_ancestors(self, node):
        ancestors = list()
        for link in self.links:
            if link[0] == node:
                ancestors.append(link[1])
        return ancestors

    def add_link(self, source, target):
        self.links.append((source, target))
        self.increase_in_deg(target)
        self.increase_out_deg(source)
        self.increase_L()

    def increase_in_deg(self, node):
        self.in_deg[node] += 1

    def increase_out_deg(self, node):
        self.out_deg[node] += 1

    def increase_L(self):
        self.L += 1


def plot_P_L_distribution(N, M):
    P_L_distribution = {}
    for i in range(N-1, int(N*(N-1)/2) + 1):
        P_L_distribution[i] = 0
    print(P_L_distribution)
    for ind in range(M):
        network = GNC(N)
        P_L_distribution[network.L] += 1
    P_L_array = np.array(P_L_distribution.values())
    L_array = np.array(P_L_distribution.keys())
    '''
    plt.plot(L_array, P_L_array)
    plt.xlabel('L')
    plt.ylabel('$P_L(N)$')
    '''
    #plt.show()


def main():
    plot_P_L_distribution(5, 10)


if __name__ == '__main__':
    main()