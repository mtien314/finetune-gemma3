
## 📄 Design Document

> Pain Point to Solution Agent

> Author: MTien

> Date: 2025-07-19

---

## ✏️ 1. Agent Input Structure & Rationale

### ✅ Proposed Input Structure
```text
"We have no clear idea which customer touchpoints are causing the most frustration"

```

🧩 Rationale

Keep the input as plain text: simple, flexible, and can work across different channels.

The Agent only needs the raw user question or complaint to process and generate an answer.

Easier integration: no need to handle metadata like customer_id or channel at this stage.

## ✏️ 2. Agent Output Structure & Rationale

✅ Proposed Output Structure

```text
- Potential Filum.ai Solution: "Customer Journey Experience Analysis (Insights - Experience)"
– How it helps: Identifies friction points by analyzing feedback and operational data across the journey.
```
🧩 Rationale

Output as plain text keeps the system simple and easy to integrate with any front-end (web, chat, mobile).

No need for structured metadata (e.g., confidence score, suggested action) if the goal is only to reply directly.

Keeps latency low: the Agent just returns the answer text.

# ✏️ 3. Feature Knowledge Base Structure & Rationale

✅ Proposed Knowledge Base Structure


```text
[
  {
    "feature_id": "f001",
    "feature_name": "Journeys",
    "description": "Manage customer journeys and touchpoints.",
    "category": "Voice of Customer",
    "use_cases": [
      "Plan personalized customer journeys",
      "Optimize customer touchpoints"
    ],
    "keywords": ["journey mapping", "customer path", "touchpoints"]
  },
]
```
🧩 Rationale
 - **category**: groups features logically, helps improve search.

 - **use_cases**: directly match real user queries to relevant features.

 - **keywords**: support keyword and semantic search.

 - **feature_id** and **feature_name**: make it easy to show matched features in logs or UI

✏️ 4. Agent's Core Logic & Matching Approach

✅ Outline

- Receive the user’s plain text input.

- Convert the input to an embedding using a language model.

- Perform semantic search on the Knowledge Base to find the most relevant feature or use case.

- Use an LLM to generate a natural language answer based on the matched feature.

- Return the answer as plain text.

🧩 Rationale
- Input & output as plain text keeps integration simple.

- Using semantic search helps understand user intent beyond keywords.

- Generating the answer directly (without structured output) reduces complexity if the only goal is replying.

## 📦 Project Structure
```plaintext
mini-project/
├── main.py                # main file to run
├── requirements.txt       #list package
├── env.example            # file enviroment 
├── README.md              
└── core-settings/                   
    ├── __init__.py
    ├── settings.py
└── llm/
    ├── __init__.py                 
    ├── chromadb/
    ├── init_llm.py
    ├── init_vectordb.py
└── langgraph_handlers/
    ├── __init__.py                 
    ├── langgraph_edges.py
    ├── langgraph_nodes.py

```

## 🚀 Run code

### Step 1: Clone project
```bash
git clone https://github.com/mtien314/mini-project.git
cd mini-project
```

### Step 2: change file file env.example to .env
```bash
cp .env.example .env
```
### Step 3: Run file requirements.txt
```bash
pip install -r requirements.txt
```
## Step 4: run file main.py 
```bash
python main.py
```
