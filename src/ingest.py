# ingest.py – placeholder for DWG/DXF ingestion

import ezdxf
import networkx as nx

def load_dwg(path: str) -> nx.Graph:
    """Load a DWG or DXF file and return a NetworkX graph of its entities."""
    doc = ezdxf.readfile(path)
    g = nx.Graph()
    # Very simplified: each entity becomes a node, connections via geometric proximity
    for i, entity in enumerate(doc.entities):
        g.add_node(i, type=entity.dxftype(), handle=entity.dxf.handle)
    # Add naive edges based on bounding box overlap (placeholder)
    for u in g.nodes:
        for v in g.nodes:
            if u >= v:
                continue
            # In a real implementation we would compute spatial relationships
            g.add_edge(u, v)
    return g
