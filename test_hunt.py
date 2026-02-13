# test_hunt.py
from agents.bantai_core.observer import ObserverAgent
from agents.bantai_core.architect import ArchitectAgent

def run_simulation():
    observer = ObserverAgent()
    architect = ArchitectAgent()
    
    # Simulating a Critical Log Entry
    critical_log = "2026-02-12 09:12:00 - CRIT - User: admin - Action: sudo_chmod_777_root - IP: 192.168.1.50"
    
    # Detection Phase
    print(f"[Observer] Analyzing Log: {critical_log}")
    threat_info = observer.analyze_log(critical_log)
    
    # Decision Phase
    if threat_info.get('threat_level') in ['Med', 'High', 'Critical']:
        print(f"[Observer] Threat Identified: {threat_info['reason']}")
        
        # Remediation Phase
        print(f"[Architect] Designing Security Fix...")
        fix_code = architect.generate_remediation(threat_info)
        
        print(f"\n✅ BantAI PROPOSED FIX (Terraform):\n{fix_code}")
    else:
        print("✅ [Observer] No significant threat detected.")

if __name__ == "__main__":
    run_simulation()