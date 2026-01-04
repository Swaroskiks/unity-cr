import os
from flask import Blueprint, request, jsonify, send_file

files_bp = Blueprint('files', __name__)

CONTENT_DIR = os.path.join(os.getcwd(), 'content')

@files_bp.route('/files', methods=['GET'])
def list_files():
    """List all files in the content directory recursively."""
    files_list = []
    for root, dirs, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith('.md'):
                rel_path = os.path.relpath(os.path.join(root, file), CONTENT_DIR)
                files_list.append(rel_path)
    return jsonify(files_list), 200

@files_bp.route('/files/<path:filename>', methods=['GET'])
def get_file(filename):
    """Get the content of a specific file."""
    file_path = os.path.join(CONTENT_DIR, filename)
    if not os.path.exists(file_path):
        return "File not found", 404
    
    with open(file_path, 'r') as f:
        content = f.read()
    return jsonify({"content": content}), 200

@files_bp.route('/files', methods=['POST'])
def save_file():
    """Save content to a file."""
    data = request.get_json()
    filename = data.get('filename')
    content = data.get('content')
    
    if not filename or content is None:
        return "Missing filename or content", 400
    
    file_path = os.path.join(CONTENT_DIR, filename)
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, 'w') as f:
        f.write(content)
        
    return "File saved", 200

@files_bp.route('/images/<path:filename>', methods=['GET'])
def get_image(filename):
    """Serve an image file."""
    return send_file(os.path.join(CONTENT_DIR, filename))

@files_bp.route('/images', methods=['POST'])
def upload_image():
    """Upload an image file."""
    if 'file' not in request.files:
        return "No file part", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
        
    if file:
        filename = file.filename
        # Save to content/images or root of content if you prefer. 
        # Let's save to content/images for organization, creating it if needed.
        images_dir = os.path.join(CONTENT_DIR, 'images')
        os.makedirs(images_dir, exist_ok=True)
        
        file_path = os.path.join(images_dir, filename)
        file.save(file_path)
        
        # Return the relative path or URL that the frontend should use
        return jsonify({"url": f"/images/images/{filename}"}), 200
@files_bp.route('/audio/<path:filename>', methods=['GET'])
def get_audio(filename):
    """Serve an audio file."""
    return send_file(os.path.join(CONTENT_DIR, filename))

@files_bp.route('/audio', methods=['POST'])
def upload_audio():
    """Upload an audio file."""
    if 'file' not in request.files:
        return "No file part", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
        
    if file:
        filename = file.filename
        audio_dir = os.path.join(CONTENT_DIR, 'audio')
        os.makedirs(audio_dir, exist_ok=True)
        
        file_path = os.path.join(audio_dir, filename)
        file.save(file_path)
        
        return jsonify({"url": f"/audio/audio/{filename}"}), 200
