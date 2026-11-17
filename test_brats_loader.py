"""Quick check that the BraTS folder can be read by the dataset loader."""
from src.brain_tumor_segmentation_system import test_brats_loader


if __name__ == "__main__":
    test_brats_loader()
