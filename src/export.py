# export.py – DXF export utility (placeholder)

def export_to_dxf(layout, path: str):
    # In a real implementation we would build a DXF with ezdxf
    with open(path, "w") as f:
        f.write("0\nSECTION\n2\nENTITIES\n0\nENDSEC\n0\nEOF\n")
    return path
