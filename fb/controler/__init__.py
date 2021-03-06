from time import sleep
import os, json

def manage_tasks(id:str):
    print(f"Start tasks {id}")
    with open(f"orders/{id}.json", 'w') as f:
        props = json.loads(f)
        props['status'] = 'working'
        f.write(json.dump(props))
    
        sleep(delay)
        
    with open(f"orders/{id}.json", 'w') as f:
        props['status'] = 'finished'
        f.write(json.dump(props))
    print(f"End tasks {id}")

def create_order(id:str, props:dict):
    if os.path.exists(f"orders/{id}.json"):
        return {'success': False, 'content': 'Order already exist'}
    else:
        props['status'] = 'wating'
        with open(f"orders/{id}.json", 'w') as f:
            f.write(json.dump(dict))
        return {'success': True}

def task_status(id:str):
    with open(f"orders/{id}.json", 'w') as f:
        return json.loads(f)['status']