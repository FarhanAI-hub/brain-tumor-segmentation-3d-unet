# 3D Brain Tumor Segmentation Using 3D U-Net

A Python/PyTorch project for volumetric brain-tumor segmentation from multi-modal MRI. The implementation includes a 3D U-Net model, a BraTS 2020 NIfTI dataset loader, synthetic-data utilities, training and validation routines, Dice-based metrics, checkpoint saving, visualisation utilities, and a Tkinter desktop interface.

> **Research/education only.** This software is not a medical device and must not be used to make clinical decisions. It has not been validated for diagnosis or treatment. Always consult qualified medical professionals.

## Project structure

```text
brain-tumor-segmentation-3d-unet/
├── app.py                         # Launch the desktop GUI
├── train.py                       # Train the model from the command line
├── generate_synthetic_data.py     # Generate synthetic test arrays
├── test_brats_loader.py           # Check the BraTS data loader
├── requirements.txt
├── LICENSE
├── .gitignore
├── README.md
├── src/
│   ├── __init__.py
│   └── brain_tumor_segmentation_system.py  # Model, dataset, training, GUI
├── data/
│   └── BraTS2020/README.md         # Put your dataset here
├── checkpoints/                   # Saved model weights (not committed)
├── logs/                          # Training logs (not committed)
└── outputs/                       # Plots/results (not committed)
```

## Main components

- **Input modalities:** four MRI channels (FLAIR, T1, T1ce and T2).
- **Network:** 3D U-Net encoder-decoder with skip connections.
- **Output channels:** three segmentation channels, used for Whole Tumor (WT), Tumor Core (TC) and Enhancing Tumor (ET).
- **Loss:** weighted combination of `BCEWithLogitsLoss` and a Dice loss term (`SimpleBSCLoss` in the source).
- **Dataset:** BraTS-style NIfTI loader, plus synthetic data generation for software/pipeline testing.
- **Interface:** Tkinter GUI for loading and visualising inputs and predictions.

### Important implementation note

The accompanying course report describes an enhanced architecture using Multi-scale Input Enhancement (MIE), Spatial Information Encoding (SIE), and Boundary-sensitive Convolution (BSC). The uploaded Python implementation currently defines a conventional 3D U-Net (`BrainTumorSegmentationModel`) and a combined BCE/Dice loss (`SimpleBSCLoss`); the source code does not define separate MIE or SIE modules. This repository preserves the supplied implementation rather than claiming those report-described modules are present in the code.

## Requirements

- Python 3.9 or newer (Python 3.10/3.11 recommended)
- PyTorch 2.1 or newer
- A supported operating system with Tkinter available for the desktop GUI
- GPU is optional; training automatically selects CUDA when available, otherwise CPU
- BraTS 2020 data is optional and must be obtained separately

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/brain-tumor-segmentation-3d-unet.git
cd brain-tumor-segmentation-3d-unet
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install PyTorch and dependencies

Install the PyTorch build suitable for your machine from the official selector: https://pytorch.org/get-started/locally/

Then install the remaining project dependencies:

```bash
pip install -r requirements.txt
```

If PyTorch was already installed using the official selector, pip will normally keep the compatible installed build. If you encounter a version/CUDA conflict, install the appropriate PyTorch build again using the official instructions.

## Usage

### Launch the desktop application

```bash
python app.py
```

The GUI uses Tkinter. On some Linux distributions, Tkinter must be installed through the operating system package manager.

### Train using synthetic data (pipeline smoke test only)

```bash
python train.py --dataset synthetic --epochs 2 --batch_size 1 --num_samples 8
```

Synthetic data is randomly generated and is **not** real MRI data. Results from synthetic training must not be presented as clinical or BraTS benchmark performance.

### Train using BraTS 2020

1. Obtain the BraTS 2020 dataset from its authorised source.
2. Extract it so each patient has a folder containing the required modality files (`flair`, `t1`, `t1ce`, `t2`, `seg`).
3. Place the patient folders under `data/BraTS2020/`, or pass the actual dataset path.
4. Run:

```bash
python train.py --dataset brats --brats_path data/BraTS2020 --epochs 50 --batch_size 1
```

Adjust batch size and crop size according to available GPU/CPU memory. The current training routine uses the same dataset object for its training and validation loaders; create a proper held-out validation split before reporting generalisation metrics.

### Generate synthetic Numpy files

```bash
python generate_synthetic_data.py
```

### Test the BraTS loader

```bash
python test_brats_loader.py
```

## Training arguments

| Argument | Default | Description |
|---|---:|---|
| `--epochs` | `50` | Number of training epochs |
| `--batch_size` | `2` | Batch size |
| `--lr` | `0.001` | Adam learning rate |
| `--weight_decay` | `0.00001` | Weight decay |
| `--in_channels` | `4` | Input MRI channels |
| `--out_channels` | `3` | Segmentation output channels |
| `--base_channels` | `16` | Base feature channels |
| `--dataset` | `synthetic` | `synthetic` or `brats` |
| `--num_samples` | `100` | Synthetic dataset sample count |
| `--brats_path` | `data/BraTS2020` | BraTS dataset directory |
| `--alpha` | `0.5` | BCE/Dice loss weighting parameter |
| `--save_interval` | `10` | Save checkpoint every N epochs |

Run `python train.py --help` to see the command-line options.

## Outputs

- Model checkpoints are written to `checkpoints/`.
- Training plots are written to `outputs/`.
- Training logs are written under `logs/`.

Large datasets, trained weights, and generated artefacts are excluded from Git by `.gitignore`. Keep backups of important model weights separately.

## Data, privacy and reproducibility

Do not commit patient data, identifiable scans, private credentials, or large model weights to a public repository. Confirm the dataset licence/terms before using or redistributing BraTS files. Record the dataset version, split, random seed, software versions, hardware, and training configuration when publishing results.

## Citation / authorship

If you use or adapt this project, please cite the associated course project/report and acknowledge the author. Add a formal BibTeX citation here if a publication or DOI is assigned to this specific project.

## License

Released under the MIT License. See [LICENSE](LICENSE).
