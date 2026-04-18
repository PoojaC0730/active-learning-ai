import json
import logging

logger = logging.getLogger(__name__)

def parse_json(response):
    if response is None:
        return None
    try:
        start_idx = response.find('{')
        end_idx = response.rfind('}')
        
        if start_idx != -1 and end_idx != -1 and start_idx < end_idx:
            json_str = response[start_idx:end_idx+1]
            return json.loads(json_str)
        else:
            logger.error(f"Failed to find JSON braces in response. Raw response snippet: {str(response)[:500]}...")
            return None
    except Exception as e:
        logger.error(f"Failed to parse extracted JSON. Error: {e}. Raw response snippet: {str(response)[:500]}...")
        return None
