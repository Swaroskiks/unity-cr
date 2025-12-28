import base64
import os
from pathlib import Path

def load_image_as_base64(filename: str) -> str:
    """
    Charge une image depuis le dossier seeds/images/ et la convertit en base64.
    
    Args:
        filename: Nom du fichier image (ex: 'question1.png')
    
    Returns:
        String base64 avec le préfixe data:image
    """
    images_dir = Path(__file__).parent / "images"
    image_path = images_dir / filename
    
    if not image_path.exists():
        print(f"Warning: Image {filename} not found at {image_path}")
        return None
    
    ext = image_path.suffix.lower()
    mime_types = {
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.gif': 'image/gif',
        '.webp': 'image/webp',
        '.svg': 'image/svg+xml'
    }
    mime_type = mime_types.get(ext, 'image/png')
    
    with open(image_path, 'rb') as f:
        image_data = f.read()
        base64_data = base64.b64encode(image_data).decode('utf-8')
    
    return f"data:{mime_type};base64,{base64_data}"
