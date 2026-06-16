from flask import Blueprint, jsonify, render_template, request

main_bp = Blueprint('main', __name__)

# Simulated in-memory database
ITEMS_DB = [
    {"id": 1, "name": "Security Scanner", "status": "Active"},
    {"id": 2, "name": "Linter", "status": "Pending"},
]

# 1. UI Route
@main_bp.route('/')
def index():
    return render_template('index.html')

# 2. API Route: Get all items (GET)
@main_bp.route('/api/items', methods=['GET'])
def get_items():
    return jsonify({"status": "success", "data": ITEMS_DB}), 200

# 3. API Route: Create an item (POST)
@main_bp.route('/api/items', methods=['POST'])
def create_item():
    data = request.get_json() or {}
    
    if 'name' not in data or 'status' not in data:
        return jsonify({"status": "error", "message": "Missing required fields"}), 400
    
    new_item = {
        "id": len(ITEMS_DB) + 1,
        "name": data['name'],
        "status": data['status']
    }
    ITEMS_DB.append(new_item)
    return jsonify({"status": "success", "data": new_item}), 201

# 4. Health Check Route (Crucial for DevSecOps/CD pipelines)
@main_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "version": "1.0.0"}), 200