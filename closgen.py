import argparse
import networkx as nx
import matplotlib.pyplot as plot

parser = argparse.ArgumentParser(description='CLOS Fabric Generator')
parser.add_argument('-t', action="store", dest="tiers")
parser.add_argument('-s', action="store", dest="spine_size")
parser.add_argument('-t4', action="store", dest="t4_size")
parser.add_argument('-t3', action="store", dest="t3_size")
parser.add_argument('-t2', action="store", dest="t2_size")
parser.add_argument('-t1', action="store", dest="t1_size")
args = parser.parse_args()

nodes = {
    'spine_list': [],
    'tier4_list': [],
    'tier3_list': [],
    'tier2_list': [],
    'tier1_list': [],
}
edges = []
clos_image = 'clos.png'

G = nx.Graph()

def build_five_tier_clos(graph, nodes=nodes, edges=edges, image_name='5tier_clos.png'):
    nodes['spine_list'] = ['s1-r' + str(node + 1) for node in range(int(args.spine_size))]
    nodes['t4_list'] = ['t4-r' + str(node + 1) for node in range(int(args.t4_size))]
    nodes['t3_list'] = ['t3-r' + str(node + 1) for node in range(int(args.t3_size))]
    nodes['t2_list'] = ['t2-r' + str(node + 1) for node in range(int(args.t2_size))]
    nodes['t1_list'] = ['t1-r' + str(node + 1) for node in range(int(args.t1_size))]

    G.add_nodes_from(nodes['spine_list'])
    G.add_nodes_from(nodes['t4_list'])
    G.add_nodes_from(nodes['t3_list'])
    G.add_nodes_from(nodes['t2_list'])
    G.add_nodes_from(nodes['t1_list'])

    for spine_router in nodes['spine_list']:
        for t4_router in nodes['t4_list']:
            edges.append((spine_router, t4_router))
            for t3_router in nodes['t3_list']:
                edges.append((t4_router, t3_router))
                for t2_router in nodes['t2_list']:
                    edges.append((t3_router, t2_router))
                    for t1_router in nodes['t1_list']:
                        edges.append((t2_router, t1_router))
    
    G.add_edges_from(edges)

    nx.draw_kamada_kawai(G, font_size=5, width=0.5, with_labels=True, font_weight='bold')
    plot.savefig(image_name) 
    return image_name

def build_three_tier_clos(graph, nodes=nodes, edges=edges, image_name='3tier_clos.png'):
    nodes['spine_list'] = ['s1-r' + str(node + 1) for node in range(int(args.spine_size))]
    nodes['t2_list'] = ['t2-r' + str(node + 1) for node in range(int(args.t2_size))]
    nodes['t1_list'] = ['t1-r' + str(node + 1) for node in range(int(args.t1_size))]

    G.add_nodes_from(nodes['spine_list'])
    G.add_nodes_from(nodes['t2_list'])
    G.add_nodes_from(nodes['t1_list'])

    for spine_router in nodes['spine_list']:
        for t2_router in nodes['t2_list']:
            edges.append((spine_router, t2_router))
            for t1_router in nodes['t1_list']:
                edges.append((t2_router, t1_router))
    
    G.add_edges_from(edges)

    nx.draw(G, font_size=5, width=0.5, with_labels=True, font_weight='bold')
    plot.savefig(image_name)
    return image_name

if args.tiers == '5':
    print(f'{args.tiers} tier CLOS Built, saved as {build_five_tier_clos(G)}')
elif args.tiers == '3':
    print(f'{args.tiers} tier CLOS Built, saved as {build_three_tier_clos(G)}')
