# Retail Layout Generator

A proof‑of‑concept project that ingests DWG/DXF files, extracts a layout graph, and uses a GNN + Stable‑Diffusion ControlNet pipeline to generate new layout proposals. The UI is built with Streamlit.

## Quick start (local)
```bash
pip install -r requirements.txt
streamlit run ui/app.py
```

Deploy on Vercel with the included Dockerfile.
