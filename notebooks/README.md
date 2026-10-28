# Notebook Roadmap

These notebooks are organized by project stage. Run them in numerical order and keep the same dataset split definitions throughout.

## Data exploration
1. `01_environment_and_dataset_audit.ipynb` — runtime, GPU, paths, metadata discovery.
2. `02_dataset_eda_and_labels.ipynb` — metadata schema, split sizes, label counts, imbalance.

## Feature analysis
3. `03_video_preprocessing.ipynb` — frame sampling and video cache design.
4. `04_audio_preprocessing.ipynb` — audio loading and log-mel features.
5. `05_cnn_features_and_visualization.ipynb` — frame visualization and CNN feature-map concepts.
6. `06_audio_video_feature_analysis.ipynb` — modality manifest alignment and leakage checks.

## Experiments
7. `07_activation_functions.ipynb`
8. `08_loss_functions.ipynb`
9. `09_optimizers_and_training.ipynb`
10. `10_video_only_baseline.ipynb`
11. `11_audio_only_baseline.ipynb`
12. `12_multimodal_fusion_model.ipynb`
13. `13_four_class_classification.ipynb`

## Model analysis
14. `14_final_evaluation.ipynb`
15. `15_ablation_studies.ipynb`
16. `16_model_explainability.ipynb`
17. `17_inference_demo.ipynb`

## Important notes
- These are initial, commented notebook scaffolds; model training requires the dataset paths, verified metadata schema, and feature manifests to be configured.
- The video/audio caches and manifests are generated artifacts and should not be committed if they contain large files or dataset-derived media.
- Never fit preprocessing statistics or select hyperparameters on the test split.
- Use stable sample IDs and preserve split boundaries to prevent leakage.
- In Colab, mount Google Drive and update `DATASET_ROOT`; on Windows, set it to your local LAV-DF folder.
- Run the first two notebooks before media decoding or model training.
