# ⚙️ IntelliRisk: AI-Powered Risk Evaluation Engine for Engineering Product Compliance

> A GenAI-powered compliance assistant that helps enterprises assess and streamline engineering product submissions against risk and safety regulations.

## 📌 Project Overview

**IntelliRisk** is an enterprise-grade Proof-of-Concept (PoC) system developed to assist compliance teams in identifying regulatory and safety risks associated with complex engineering products. Built using Google Gemini APIs, the system provides contextual evaluation, risk tagging, and actionable summaries that empower decision-makers to make informed choices — faster and with greater confidence.

The solution is part of a broader initiative to embed GenAI into enterprise workflows, reducing manual effort and accelerating time-to-compliance.

---

## 🧠 Core Capabilities

- ✅ **Risk Evaluation Engine**: Automatically parses technical specification documents and identifies compliance issues using Gemini models.
- 🧾 **Custom Prompting & RAG Pipelines**: Tailored prompts combined with Retrieval-Augmented Generation (RAG) to provide industry-specific, explainable insights.
- 🔍 **Entity Extraction**: Pulls out relevant parameters (e.g., product features, materials, safety constraints) to check alignment with regulatory norms.
- 💡 **Insightful Summarization**: Converts engineering jargon into understandable summaries for legal, technical, and business stakeholders.
- 📊 **Intelligent Recommendations**: Suggests actionable next steps (e.g., component replacement, documentation enhancement, regulation links).
- 🧩 **Multi-Agent Orchestration (optional extension)**: Can be scaled with LangGraph or CrewAI for distributed task handling and memory-based workflows.

---

## 🛠 Tech Stack

- **LLM Backend**: Google Gemini Pro API (via Vertex AI or REST interface)
- **Frontend**: Streamlit / Flask (customizable as per enterprise requirement)
- **RAG**: FAISS-based retrieval with document embeddings
- **Vector Store**: FAISS or Google Cloud Vertex Matching Engine
- **Prompt Engineering**: Role-based dynamic prompt templates
- **Hosting**: Google Cloud / Local Dockerized Deployment
- **Versioning**: GitHub + DVC (optional for model/data versioning)

---

## 🚀 How It Works

1. **Document Upload**:
   - Upload engineering design documents (PDFs, CSVs, technical specs).
2. **Contextual Parsing**:
   - Gemini parses input with custom instructions for extracting features and parameters.
3. **Risk Assessment**:
   - Evaluates documents for red flags using embedded knowledge + retrieved compliance policies.
4. **Output Generation**:
   - Generates a human-readable summary, potential risk tags, and mitigation suggestions.
5. **Export Options**:
   - Results can be downloaded as PDF reports or exported to downstream compliance systems.

---

## 📦 Installation & Usage

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/intellirisk.git
   cd intellirisk
2. **Create virtual environment**
```
python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```
3. **Install required packages**
```
pip install -r requirements.txt
```
4. 🔑 Add Gemini API Key
> Obtain your Google Gemini Pro API key from Google AI Studio.

Then, create a .env file in the project root and add:

```ini
GEMINI_API_KEY=your_api_key_here
```
Ensure python-dotenv is installed to auto-load it. If not:

```bash
pip install python-dotenv
```
5. 🛠️ Run the Application
```bash
python app.py
```
Open your browser and navigate to http://127.0.0.1:5000 to use IntelliRisk.

---

## 📌 Sample Use Case
- Client: A multinational engineering firm wants to submit a new industrial motor for global compliance evaluation.
- Input: Product spec sheet PDF with 30+ technical parameters.

### Output from IntelliRisk:

- Identified that thermal shielding material doesn’t comply with updated ISO standards.
- Recommended materials with links to suppliers.
- Suggested updated documentation sections with Gemini-generated content.

## 📚 Behind the Scenes
- This project was developed as part of a GenAI Solutioning Project focused on:
- Architecting multi-agent systems (LangChain, LangGraph, LLaMa Index, CrewAI)
- Developing domain-specific RAG pipelines
- Integrating Gemini with enterprise data layers
- Collaborating with product owners and client teams for technical PoCs

---

## 🔒 Data Privacy & Limitations
- No OpenAI APIs used.
- All processing is done with Google Gemini APIs.
- Ensure documents don’t contain sensitive PII before uploading.
- Not a replacement for human audit — acts as a GenAI-assisted compliance co-pilot.

---

## 🧠 Future Enhancements
- Multi-document evaluation and version control
- Real-time collaboration for compliance teams
- Integration with enterprise CRMs (SAP, Oracle)
- LangGraph-based multi-agent orchestration
- Support for voice-based document walkthroughs

---

## 🤝 Contributions
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 🪪 License
This project is licensed under the MIT License.

---

## 📫 Contact
For collaborations or enterprise inquiries: achyuth2004@gmail.com
