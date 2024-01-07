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
    plt.scatter(L_array[100:600], P_L_array[100:600], s=0.5)
    plt.xlabel('L')
    plt.ylabel('$P_L(N)$')
    plt.show()
    #print(P_L_distribution)


def in_degree_distribution(gnc_list):
    in_deg = np.zeros(gnc_list[0].N)
    for gnc in gnc_list:
        in_deg += gnc.in_deg
    in_deg /= len(gnc_list)
    return in_deg


def out_degree_distribution(gnc_list):
    out_deg = np.zeros(gnc_list[0].N)
    for gnc in gnc_list:
        out_deg += gnc.out_deg
    out_deg /= len(gnc_list)
    return out_deg


def plot_in_degree_distribution(in_deg_dist, x_axis):
    plt.scatter(x_axis, in_deg_dist, s=3)
    plt.title("In-Degree Distribution")
    plt.show()


def plot_out_degree_distribution(out_deg_dist, x_axis):
    plt.scatter(x_axis, out_deg_dist, s=3)
    plt.title("Out-Degree Distribution")
    plt.show()


def main():
    N = 1000
    M = 100
    gnc_list = [GNC(N) for _ in range(M)]
    # plot_P_L_distribution(5, 10)
    in_deg_dist = in_degree_distribution(gnc_list)
    out_deg_dist = out_degree_distribution(gnc_list)
    x_axis = np.arange(len(in_deg_dist))
    plot_in_degree_distribution(in_deg_dist, x_axis)
    plot_out_degree_distribution(out_deg_dist, x_axis)


if __name__ == '__main__':
    main()
