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