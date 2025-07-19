
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
