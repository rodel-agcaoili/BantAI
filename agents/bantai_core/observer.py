import ollama
import json


class ObserverAgent:
    def __init__(self, model="llama3"):
        self.model = model

    def analyze_log(self, log_entry):
        #RTF
        prompt = f"""
        ROLE: You are a an expert security analyst that secializes in cloud and AI.
        TASK:Analyze the following log entry for security anomalies or brute-force attempts.
        LOG: {log_entry}
        FORMAT: Return ONLY a JSON object with keys 'threat_level' (Low/Medium/High), 'reason', and 'suggested_action'.
        """
        
        response = ollama.generate(self.model, prompt)
        return json.loads(response)


if __name__ == "__main__":
    observer = ObserverAgent()
    mock_log = "2026-02-12 14:00:01 - FAIL_LOGIN - IP: 192.168.1.50 - User: admin"
    print(f"BantAI Observer Analysis:\n{observer.analyze_log(mock_log)}")