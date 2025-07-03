# Super-Resolution on DIV2K with SRCNN and ImprovedSRCNN

This project implements and compares deep learning models for single-image super-resolution, following the guidelines of the [DIV2K dataset](https://data.vision.ee.ethz.ch/cvl/DIV2K/). Both a vanilla SRCNN and an improved SRCNN variant are trained and evaluated. The codebase also includes dataset preprocessing and reproducible evaluation scripts.

## Project Structure

- `super_resolution_final.ipynb` — Main Jupyter/Colab notebook for model training, evaluation, and result visualization.
- `preprocessing/` — Scripts to crop, downsample, and visualize dataset images.
  - `crop_and_downsample.py`
  - `preprocess_visualization.py`
- `README.md` — This file.

## Dataset Preparation

1. **Download** the DIV2K dataset from the official site.
2. Use `preprocessing/crop_and_downsample.py` to generate cropped HR and paired LR (bicubic ×4) images.
3. Optionally, use `preprocessing/preprocess_visualization.py` to visualize and verify preprocessing steps.

## Training and Evaluation

Open `super_resolution_final.ipynb` and run all cells in order:
- **Data Loading**: Loads preprocessed DIV2K images.
- **Model Definitions**: SRCNN and ImprovedSRCNN (deeper, PReLU activations).
- **Training**: Train both models from scratch or load saved weights.
- **Evaluation**: Quantitative (PSNR, SSIM, FID) and qualitative (image visualization) analysis.

## Results

Key findings (averaged over 3 runs, validation set):
- **Vanilla SRCNN**: PSNR = 26.69 ± 0.08, SSIM = 0.7713 ± 0.0010, FID = 34.47 ± 0.58
- **Improved SRCNN**: PSNR = 27.47 ± 0.04, SSIM = 0.7937 ± 0.0009, FID = 29.13 ± 0.22

The improved model outperforms the baseline in all metrics.

## Reproducibility

- All code is compatible with Google Colab and PyTorch.
- Random seeds are set for repeatability.
- Data preprocessing is modular and script-based.

