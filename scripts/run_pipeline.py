# run_pipeline.py – end‑to‑end driver (placeholder)

from src.ingest import load_dwg
from src.retrieval import encode_graph, build_index
from src.generator import generate_layout
from src.rule_engine import check_constraints
from src.export import export_to_dxf

def main(dwg_path: str, out_path: str = "output.dxf"):
    g = load_dwg(dwg_path)
    vec = encode_graph(g)
    # Build a trivial index with just this vector (in real case we’d have many)
    index = build_index(np.array([vec]))
    layout = generate_layout(vec)
    ok, msgs = check_constraints(layout)
    if not ok:
        raise RuntimeError("Constraint violation: " + ", ".join(msgs))
    return export_to_dxf(layout, out_path)

if __name__ == "__main__":
    import argparse, pathlib
    parser = argparse.ArgumentParser()
    parser.add_argument("dwg", help="Path to DWG/DXF file")
    parser.add_argument("-o", "--output", default="output.dxf")
    args = parser.parse_args()
    out = main(args.dwg, args.output)
    print(f"Exported layout to {out}")
