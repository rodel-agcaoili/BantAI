# 🛡️ BantAI: The Autonomous Cloud Guardian

**BantAI** (from the Filipino word *Bantay*, meaning guardian) is a stateful, multi-agent AI system designed to hunt and remediate cloud security threats in real-time. 

Built as a privacy-first research project at the intersection of **AI, Cybersecurity, and AIOps**, BantAI leverages local LLMs to ensure sensitive security logs never leave the enterprise perimeter.

---

## 🧠 System Architecture

BantAI uses **LangGraph** to orchestrate a sophisticated "Sensing-to-Remediation" workflow. Unlike linear scripts, BantAI maintains a persistent state, allowing agents to collaborate and self-correct.

```mermaid
graph TD
    subgraph Local_Environment [Privacy-First Stack]
        Ollama[(🤖 Ollama Brain<br/>Llama3 & CodeLlama)]
        Logs[📄 Mock Cloud Logs]
    end

    subgraph BantAI_Brain [LangGraph Orchestrator]
        Start((Start)) --> Observer[🕵️ Observer Node]
        Observer --> Router{Threat Found?}
        
        Router -- Low Threat --> End((Stop))
        Router -- Med/High --> Architect[🏗️ Architect Node]
        
        Architect --> Validator[🛠️ Validator Tool]
        Validator -- Pass --> Remediation[✅ Apply HCL Fix]
        Validator -- Fail --> Architect
    end

    Logs --> Observer
    Ollama <--> Observer
    Ollama <--> Architect
    Remediation --> End

    style Start fill:#f9f,stroke:#333
    style End fill:#f9f,stroke:#333
    style Observer fill:#bbf,stroke:#333
    style Architect fill:#bbf,stroke:#333
    style Validator fill:#ffb,stroke:#333
    style Ollama fill:#dfd,stroke:#333

🚀 Key Features
Privacy-First AI: Integrated with Ollama for 100% local inference. No sensitive logs are sent to 3rd-party APIs.

Stateful Orchestration: Built on LangGraph to manage complex, non-linear decision-making and agent memory.

Automated Remediation: Moves from "Alerting" to "Acting" by generating production-ready Terraform (HCL) code.

AIOps Ready: Containerized with Docker and built with a modular architecture for easy transition to Kubernetes.

🛠️ Technical Stack
Language: Python 3.11

AI Engine: Ollama (Llama 3 for logic, CodeLlama for HCL generation)

Orchestration: LangGraph / LangChain

Infrastructure: Terraform & Docker

Testing: Pytest & Custom Chaos Engine

🏁 Getting Started
Clone the Repo:

Bash
git clone [https://github.com/your-username/bantai.git](https://github.com/your-username/bantai.git)
cd bantai
Start the Brain:
Ensure Ollama is running, then:

Bash
docker compose up -d
docker exec -it bantai-brain ollama pull llama3
docker exec -it bantai-brain ollama pull codellama
Launch the Sentinel:

Bash
docker compose run bantai-agent python -m agents.bantai_core.graph

👨‍💻 About the Author
Developed by Rodel, a Sr. Cloud Engineer and AI Researcher. This project represents a fusion of my work in Global Information Security and the Georgia Tech OMSCS program.