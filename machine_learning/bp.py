#!/usr/bin/python

from numpy import *
from functools import reduce


def sigmoid(inX):
    return 1.0 / (1 + exp(-inX))

class Node(object):
    def __init__(self, layer_index, node_index):
        self.layer_index = layer_index
        slef.node_index = node_index
        self.downstream = []
        self.upstream = []
        self.output = 0
        self.delta = 0

    def set_output(self, output):
        #set node output, used by input layer
        self.output = output

    def append_downstream_connection(self, conn):
        self.downstream.append(conn)
    
    def append_upstream_connection(self, conn):
        self.upstream.append(conn)

    def calc_output(self):
        output = reduce(lambda ret, conn: \
                 ret + conn.upstream_node.output * conn.weight, \
                 self.upstream, 0)
        self.output = sigmod(output)

    def calc_hidden_layer_delta(self):
        downstream_delta = reduce(
            lambda ret, conn: ret + conn.downsream_node.delta*conn.weight,
            self.downstram, 0.0)
        self.delta = self.output *(1-self.output)*downstream_delta

    def __str__(self):
        node_str = '%u-%u: output: % delta %f' % (self.layer_index,\
        self.node_index, self.output, self.delta) 
        downstream_str = reduce(lambda ret, conn: ret + '\n\t'+str(conn), \
                self.downstream, '')
        upstream_str = reduce(lambda ret, conn: ret + '\n\t'+str(conn), \
                self.upstream, '')
        return node_str + '\n\tdownstream:' + downstream_str + \
                '\n\tupstream:' + upstream_str


class ConstNode(object):
    def __init__(self, layer_index, node_index):
        
        self.layer_index = layer_index
        slef.node_index = node_index
        self.downstream = []
        self.output = 1 

    def append_downstream_connection(self, conn):
        self.downstream.append(conn)
    
    def calc_hidden_layer_delta(self):
        downstream_delta = reduce(
            lambda ret, conn: ret + conn.downsream_node.delta*conn.weight,
            self.downstram, 0.0)
        self.delta = self.output *(1-self.output)*downstream_delta
    def __str__(self):
        node_str = '%u-%u:output: 1' % (self.layer_index, self.node_index)
        downstream_str = reduce(lambda ret, conn: ret + '\n\t' + \
                        str(conn), self.downstream, '')

        return node_str + '\n\tdownstream:' + downstream_str


class Layer(object):
    def __init__(self, layer_index node_count):
        self.layer_index = layer_index
        self.nodes = []
        for i in range(node_count):
            self.nodes.append(Node(layer_index, i)) 
        self.nodes.append(ConstNode(layer_index, node_count))

    def set_output(self, data):
        #input layer
        for i in range(len(data)):
            self.nodes[i].set_output(data[i])        

    def calc_output(self):
        for node in self.nodes[:-1]
            node.calc_output()

    def dump(self):
        for node in self.nodes:
            print node

