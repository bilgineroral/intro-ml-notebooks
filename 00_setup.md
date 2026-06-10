# Environment Setup

Welcome! Before running any course notebook, you need to set up a Python environment for this project. **You only need to do this once.**

These steps will:
1. **Create** the `segmentation` environment,
2. **Install** every library we need into it,
3. **Register** it as a Jupyter kernel,
4. **Verify** that everything imported correctly.

> **Note:** Run these commands in a terminal in order.

---

## Before you start

- You need `conda` installed. If it's not already installed, first install
  **Miniconda** from
  <https://www.anaconda.com/docs/getting-started/miniconda/install/overview>
  and then come back.
- The downloads are large, so don't worry if it takes a while.

---

## Step 1 — Create the environment

This makes a brand-new, empty environment with just Python inside it.

```bash
conda create -y -n segmentation python=3.11
```

---

## Step 2 — Install the libraries

This installs every library we need for the notebooks:

```bash
conda run --no-capture-output -n segmentation pip install torch==2.6.0 torchvision==0.21.0
conda run --no-capture-output -n segmentation pip install segmentation-models-pytorch
conda run --no-capture-output -n segmentation pip install albumentations
conda run --no-capture-output -n segmentation pip install numpy matplotlib pillow opencv-python scikit-image
conda run --no-capture-output -n segmentation pip install tqdm tensorboard
conda run --no-capture-output -n segmentation pip install scikit-learn seaborn plotly
conda run --no-capture-output -n segmentation pip install jupyter notebook
```

---

## Step 3 — Register the Jupyter kernel

This makes the environment selectable as a kernel inside Jupyter / VS Code.

```bash
conda run -n segmentation python -m ipykernel install --user --name segmentation --display-name "segmentation"
```

---

## Step 4 — Verify everything installed

Verify everything installed correctly by running the `verify_env.py` script:

```bash
conda run --no-capture-output -n segmentation python verify_env.py
```

Example output (versions may differ slightly):

```
Installed packages
------------------------------------------
torch                          2.6.0
torchvision                    0.21.0
segmentation_models_pytorch    0.5.0
albumentations                 2.0.8
numpy                          2.4.6
matplotlib                     3.10.9
PIL                            12.2.0
cv2                            4.13.0
skimage                        0.26.0
sklearn                        1.9.0
seaborn                        0.13.2
tqdm                           4.68.1
tensorboard                    2.20.0
------------------------------------------

Environment is ready.
```

---

## Step 5 — Select the `segmentation` kernel

From now on, every course notebook should run on this environment.

**VS Code:** open a notebook, click the kernel name in the **top-right**, and choose **`segmentation`**.
