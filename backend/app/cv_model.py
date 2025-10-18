# cv_model.py

import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import io

class CVModel:
    """
    Lightweight computer vision model using pretrained ResNet18.
    Used to extract visual features or predict basic categories.
    """
    def __init__(self, device=None):
        self.device = device or ('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = models.resnet18(pretrained=True)
        self.model.eval()
        self.model.to(self.device)

        # Define image transformation pipeline
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])
        ])

    def infer_image_bytes(self, image_bytes):
        """
        Runs inference on an image passed as bytes.
        Returns top prediction label index and probability.
        """
        img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
        x = self.transform(img).unsqueeze(0).to(self.device)

        with torch.no_grad():
            outputs = self.model(x)
            probs = torch.nn.functional.softmax(outputs, dim=1)
            top1 = torch.argmax(probs, dim=1).item()

        return {
            "imagenet_label_index": int(top1),
            "confidence_score": float(probs[0, top1].cpu().numpy())
        }
