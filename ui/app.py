import streamlit as st
from src.ingest import load_dwg
from src.generator import generate_layout
from src.retrieval import encode_graph
from src.export import export_to_dxf

st.title("Retail Layout Generator (Vercel‑ready)")

uploaded = st.file_uploader("Upload a DWG/DXF file", type=["dwg", "dxf"])
if uploaded:
    # Save to a temporary path
    temp_path = f"/tmp/{uploaded.name}"
    with open(temp_path, "wb") as f:
        f.write(uploaded.getbuffer())
    st.success(f"File saved to {temp_path}")
    # Load and process
    g = load_dwg(temp_path)
    vec = encode_graph(g)
    layout = generate_layout(vec)
    st.json(layout)
    # Export button
    if st.button("Export DXF"):
        out_path = f"/tmp/{uploaded.name.split('.')[0]}_generated.dxf"
        export_to_dxf(layout, out_path)
        with open(out_path, "rb") as f:
            st.download_button("Download DXF", f, file_name=out_path.split('/')[-1])
