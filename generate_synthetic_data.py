"""Generate example synthetic MRI-like arrays for pipeline testing."""
from src.brain_tumor_segmentation_system import generate_synthetic_data


if __name__ == "__main__":
    generate_synthetic_data(num_samples=50)
