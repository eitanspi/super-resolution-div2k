# Super-Resolution on DIV2K with SRCNN and ImprovedSRCNN

**Author:** Eitan Spivak  
**Student ID:** 311391866

This project implements and compares two deep learning models—vanilla SRCNN and an improved SRCNN—for single-image super-resolution using the DIV2K dataset. The repository includes code for dataset preprocessing, model training, evaluation, and visualization, all organized for reproducibility and ease of use.

---

## Project Structure

- `super_resolution_final.ipynb` — Main Jupyter/Colab notebook for data loading, training, evaluation, and visualization.
- `preprocessing/` — Scripts for image preparation and quality checking:
  - `crop_and_downsample.py`: Crops and downsamples HR images, generates paired LR images.
  - `preprocess_visualization.py`: Visualizes original, cropped, and downsampled images.
- `README.md` — This file.

---

## Dataset Preparation

1. **Download** the DIV2K dataset from the [official source](https://data.vision.ee.ethz.ch/cvl/DIV2K/).
2. Run:
    ```bash
    python preprocessing/crop_and_downsample.py
    ```
   This will create cropped HR images and bicubic ×4 LR images in new folders.
3. (Optional) Run:
    ```bash
    python preprocessing/preprocess_visualization.py
    ```
   to visualize and confirm the correctness of preprocessing.

---

## Training and Evaluation

1. Open `super_resolution_final.ipynb` in Jupyter or Google Colab.
2. Run all cells in order:
   - Loads prepared DIV2K images.
   - Defines and trains both SRCNN and ImprovedSRCNN models.
   - Evaluates models using PSNR, SSIM, and FID.
   - Visualizes best and worst-case results.

All code uses relative paths and runs from start to finish without manual intervention.

---

## Results

| Model            | PSNR             | SSIM             | FID             |
|------------------|------------------|------------------|-----------------|
| Vanilla SRCNN    | 26.69 ± 0.08     | 0.7713 ± 0.0010  | 34.47 ± 0.58    |
| Improved SRCNN   | 27.47 ± 0.04     | 0.7937 ± 0.0009  | 29.13 ± 0.22    |

The improved model shows consistent gains over the vanilla baseline across all metrics.

---

## Reproducibility

- All scripts are modular, commented, and use only relative paths.
- Code is compatible with Google Colab and standard Python environments.
- Random seeds are set for repeatability.

---

## License

For academic and educational use only.

---

