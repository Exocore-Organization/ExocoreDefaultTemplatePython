import os
import json

def normalize_path(path):
    # Normalize path: remove multiple slashes and trailing slashes (except root)
    while '//' in path:
        path = path.replace('//', '/')
    if path != '/' and path.endswith('/'):
        path = path[:-1]
    return path or '/'

def extract_routes(app):
    routes = []
    for route in app.routes:
        if hasattr(route, 'methods'):
            for method in route.methods:
                if method in ['HEAD', 'OPTIONS']:
                    continue
                routes.append({
                    'method': method,
                    'path': normalize_path(route.path)
                })
    routes.sort(key=lambda x: (x['path'], x['method']))
    return routes

def generate_and_save_routes(app, output_path='../exocore-web/models/routes.json'):
    routes = extract_routes(app)
    data = {'routes': routes}

    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
        print(f'[paths_routes.py] Created output directory: {output_dir}')

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        print(f'[paths_routes.py] Successfully saved {len(routes)} routes to {output_path}')
    except Exception as e:
        print(f'[paths_routes.py] Error saving routes to {output_path}: {e}')