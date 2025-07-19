import streamlit as st
import os
import docx
from risk_agent_backend import (
    build_or_load_faiss, docx_to_documents, csv_to_documents, risk_evaluator,
    docx_path, csv_path, docx_store_dir, csv_store_dir, llm
)

st.set_page_config(
    page_title="Risk Evaluation Dashboard",
    page_icon="⚠️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Product Risk Evaluation Dashboard")
st.write(
    "Upload your product/component name and evaluate risk based on requirements and historical data."
)

@st.cache_resource
def get_indices():
    """Load indices once for performance."""
    docx_docs = docx_to_documents(docx_path)
    csv_docs = csv_to_documents(csv_path)
    faiss_docx = build_or_load_faiss(docx_docs, docx_store_dir, which="docx")
    faiss_csv = build_or_load_faiss(csv_docs, csv_store_dir, which="csv")
    return faiss_docx, faiss_csv

faiss_docx, faiss_csv = get_indices()

st.sidebar.header("Risk Evaluation Controls")
component_name = st.sidebar.text_input("Component/Product Name", value="brake cable")
output_dir = os.path.dirname(docx_store_dir)
if st.sidebar.button("Generate Risk Evaluation Report"):
    with st.spinner("Evaluating risk and generating report ..."):
        output_path = os.path.join(
            output_dir, f"risk_report_{component_name.replace(' ', '_')}.docx"
        )
        # Evaluate & create report using backend
        risk_evaluator(
            product_name=component_name,
            faiss_store_docx=faiss_docx,
            faiss_store_csv=faiss_csv,
            llm=llm,
            output_report_path=output_path
        )
        st.success(f"Risk Evaluation Report generated at: {output_path}")

        def docx_to_txt(path):
            doc = docx.Document(path)
            return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])

        with st.expander("Show Report Preview", expanded=True):
            st.text(docx_to_txt(output_path))

        st.download_button(
            label="Download Report (.docx)",
            data=open(output_path, 'rb'),
            file_name=f"risk_report_{component_name.replace(' ','_')}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

st.markdown("---")

st.subheader("Component Requirements & History (Preview)")
if st.sidebar.checkbox("Show requirements preview"):
    docx_docs = docx_to_documents(docx_path)
    st.write("**First 5 DOCX requirement paragraphs:**")
    st.write(docx_docs[:5])

if st.sidebar.checkbox("Show product history preview"):
    csv_docs = csv_to_documents(csv_path)
    st.write("**First 5 product history rows:**")
    st.write(csv_docs[:5])
