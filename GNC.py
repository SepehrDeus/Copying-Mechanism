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


def plot_P_L_distribution(N, network_list):
    P_L_distribution = {}
    for i in range(N-1, int(N*(N-1)/2) + 1):
        P_L_distribution[i] = 0
    for network in network_list:
        P_L_distribution[network.L] += 1
    P_L_array = np.array(list(P_L_distribution.values()))
    L_array = np.array(list(P_L_distribution.keys()))
    plt.scatter(L_array, P_L_array, s = 1)
    plt.xlabel('L')
    plt.ylabel('$P_L(N)$')
    plt.show()
    plt.scatter(L_array[0: 10*N], P_L_array[0: 10*N], s=1)
    plt.xlabel('L')
    plt.ylabel('$P_L(N)$')
    plt.show()
    #print(P_L_distribution)

def main():
    N = 100
    M = 10000
    gnc_list = [GNC(N) for _ in range(M)]
    plot_P_L_distribution(N, gnc_list)


if __name__ == '__main__':
    main()