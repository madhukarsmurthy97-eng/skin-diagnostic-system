import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image

class SkinClassifier:
    def __init__(self):
        self.classes = [
            "Acne", "Eczema", "Psoriasis", "Rosacea",
            "Fungal Infection", "Vitiligo", "Healthy"
        ]

        # Transfer Learning – ResNet18
        self.model = models.resnet18(pretrained=True)
        self.model.fc = torch.nn.Linear(
            self.model.fc.in_features, len(self.classes)
        )
        self.model.eval()

        self.transform = transforms.Compose([
            transforms.Resize((224,224)),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )
        ])

    def predict(self, image: Image.Image):
        image = self.transform(image).unsqueeze(0)

        with torch.no_grad():
            outputs = self.model(image)
            probs = torch.softmax(outputs, dim=1)

        conf, idx = torch.max(probs, 1)
        return self.classes[idx.item()], round(conf.item(), 3)
