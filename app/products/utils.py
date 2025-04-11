import numpy as np
from io import BytesIO
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input

MODEL = ResNet50(weights='imagenet', include_top=False, pooling='avg')

def extract_features(image_path: str) -> bytes:
    """Extract ResNet50 features from product image"""
    try:
        # Load and preprocess image
        img = load_img(image_path, target_size=(224, 224))
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)
        
        # Extract features
        features = MODEL.predict(img_array)
        normalized = features.flatten() / np.linalg.norm(features)
        
        # Serialize to bytes
        buffer = BytesIO()
        np.save(buffer, normalized)
        return buffer.getvalue()
    except Exception as e:
        print(f"Feature extraction failed: {str(e)}")
        return None