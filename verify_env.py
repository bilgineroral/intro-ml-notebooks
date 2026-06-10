import importlib

print("Installed packages")
print("-" * 42)

import torch, torchvision
print(f"{'torch':30s} {torch.__version__}")
print(f"{'torchvision':30s} {torchvision.__version__}")

# import name -> (some differ from the pip name, e.g. pillow imports as PIL)
modules = [
    "segmentation_models_pytorch",
    "albumentations",
    "numpy",
    "matplotlib",
    "PIL",
    "cv2",
    "skimage",
    "sklearn",
    "seaborn",
    "plotly",
    "tqdm",
    "tensorboard",
]
for name in modules:
    mod = importlib.import_module(name)
    print(f"{name:30s} {getattr(mod, '__version__', 'ok')}")

print("-" * 42)

print("\nEnvironment is ready.")
