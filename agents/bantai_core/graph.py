from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END
from agents.bantai_core.observer import ObserverAgent
from agents.bantai_core.architect import ArchitectAgent

class BantAIState(TypedDict):
    raw_log: str
    threat_analysis: Optional[dict]
    remediation_code: Optional[str]
    validation_errors: Optional[str]
    is_valid: bool
    iteration_count: int

def observer_node(state: BantAIState):
    print("🔍 [Node: Observer] Scanning logs...")
    agent = ObserverAgent()
    analysis = agent.analyze_log(state['raw_log'])
    
    return {
        "threat_analysis": analysis,
        "iteration_count": state.get("iteration_count", 0) + 1
    }

def architect_node(state: BantAIState):
    print("🏗️ [Node: Architect] Designing security fix...")
    agent = ArchitectAgent()
    # The architect needs the threat analysis from the state
    fix = agent.generate_remediation(state['threat_analysis'])
    
    return {"remediation_code": fix}

# Logic Gate (Router)
def should_remediate(state: BantAIState):
    analysis = state.get("threat_analysis", {})
    level = analysis.get("threat_level", "Low")
    
    if level in ["Med", "High", "Critical"]:
        return "remediate"  # Proceed to Architect
    return "stop"           # End the process

workflow = StateGraph(BantAIState)
workflow.add_node("observer", observer_node)
workflow.add_node("architect", architect_node)

workflow.set_entry_point("observer")

# Add conditional edges based on the should_remediate function
workflow.add_conditional_edges("observer", should_remediate, {'remediate': 'architect', 'stop': END})

# Connect architect to END
workflow.add_edge("architect", END)

# Compile the graph
app = workflow.compile()

if __name__ == "__main__":
    # Simulate a critical log entry
    input_state = {
        "raw_log": "2026-02-13 00:01:00 - CRIT - User: admin - Action: sudo_chmod_777 - IP: 192.168.1.50",
        "iteration_count": 0
    }
    
    print("aaaLaunching BantAI Autonomous Graph...")
    for output in app.stream(input_state):
        # This streams the output of each node as it finishes
        for key, value in output.items():
            print(f"\n--- Node [{key}] complete ---")
            if 'threat_analysis' in value:
                print(f"Analysis: {value['threat_analysis']}")
            if 'remediation_code' in value:
                print(f"Proposed Fix:\n{value['remediation_code']}")
