import json
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

class Item(BaseModel):
    file: str

app = FastAPI()

@app.post("/process")
def process_excel_file(item: Item):
    data = json.loads(item.file)
    log = data['log_type']
    classification = data['classification_type']
    
    result = {"log_type": {}, "classification_type": {}}
    
    log_vals = list(dict(log).values())
    unique_log_vals = list(set(log_vals))
    for log_type in unique_log_vals:
        result["log_type"][log_type] = log_vals.count(log_type)
    
    classification_vals = list(dict(classification).values())
    unique_classification_vals = list(set(classification_vals))
    for classification_type in unique_classification_vals:
        result["classification_type"][classification_type] = classification_vals.count(classification_type)
        
    return result