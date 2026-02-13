import ollama
import json
import re

class ObserverAgent:
    def __init__(self, model="llama3"):
        self.model = model

    def analyze_log(self, log_entry):
        #RTF
        prompt = f"""
        ROLE: You are a an expert security analyst that secializes in cloud and AI.
        TASK:Analyze the following log entry for security anomalies or brute-force attempts.
        LOG: {log_entry}
        FORMAT: Return JSON only: {{"threat_level": "Low/Med/High", "reason": "...", "suggested_action": "..."}}.
        STRICT: Do not include any conversational text, markdown, or analysis outside the JSON.
        """
        
        output = ollama.generate(self.model, prompt, options={'num_predict': 500, 'temperature': 0.1})
        raw_text = output['response'].strip()

        try:
            json_match = re.search(r'(\{.*\})', raw_text, re.DOTALL)
            
            if json_match:
                clean_json = json_match.group(1)
                return json.loads(clean_json)
            else:
                raise ValueError("No JSON found in response")
                
        except (json.JSONDecodeError, ValueError) as e:
            return {
                "threat_level": "Error",
                "reason": f"Parsing failed: {str(e)}",
                "raw_output": raw_text[:200] # Truncate for readability
            }


if __name__ == "__main__":
    observer = ObserverAgent()
    mock_log = "2026-02-12 14:00:01 - FAIL_LOGIN - IP: 192.168.1.50 - User: admin"
    print(f"BantAI Observer Analysis:\n{observer.analyze_log(mock_log)}")