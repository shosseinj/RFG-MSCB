# Experiments Audit

Scope: final experiment `one_seed_45_fafem_residual_frequency_guided_mscb_stage3_stronger_init_warmup_cosine`, seed 42. Evidence was evaluated in the requested priority order; `sections/04_experiments.tex` was treated only as the draft under audit.

| Item | Final verified value | Evidence source | Current manuscript value | Status |
|---|---|---|---|---|
| Final experiment | Exp.45 `one_seed_45_fafem_residual_frequency_guided_mscb_stage3_stronger_init_warmup_cosine`, seed 42 | `FINAL_EXPERIMENT_CONFIG.md`; `source_snapshots/final_checkpoint_metadata.json` | Not identified | STALE |
| Datasets | Kvasir-SEG, CVC-ClinicDB, CVC-300, CVC-ColonDB, ETIS-LaribPolypDB | `DATASET_SPLIT.md`; `EVALUATION_PROTOCOL.md` | Same five datasets | VERIFIED |
| Kvasir-SEG split | 900 train, 100 held-out validation/evaluation | `DATASET_SPLIT.md`; `source_snapshots/main_torch.py:210-217`; evaluation summary (100 samples) | 900 train; prose implies remaining samples are test, but table reports 500 test | CONTRADICTION |
| CVC-ClinicDB split | 550 train, 62 held-out validation/evaluation | `DATASET_SPLIT.md`; `source_snapshots/main_torch.py:219-226`; evaluation summary (62 samples) | 550 train, 62 test | STALE |
| Validation construction | Independent 90/10 split of each training dataset with `train_test_split(test_size=0.1, random_state=42, shuffle=True)`; held-out subsets merged | `DATASET_SPLIT.md`; `source_snapshots/main_torch.py:208-244` | 145 images selected from the already formed training set | STALE |
| External test sets | Full CVC-300 (60), CVC-ColonDB (380), and ETIS-LaribPolypDB (196); no role in training or selection | `DATASET_SPLIT.md`; `EVALUATION_PROTOCOL.md`; evaluation summary | Other three datasets used as test sets | VERIFIED |
| Input and preprocessing | 352 x 352 RGB; image bilinear resize and [0,1] scaling; mask nearest-neighbor resize and binarization; ImageNet encoder normalization | `DATASET_SPLIT.md`; `FINAL_MODEL_ARCHITECTURE.md` | 352 x 352 stated; interpolation/normalization omitted | VERIFIED |
| Optimizer | AdamW, betas (0.9, 0.999) | `FINAL_EXPERIMENT_CONFIG.md`; `source_snapshots/main_torch.py:3156-3170` | AdamW | VERIFIED |
| Decoder learning rate | 3.0e-4 | Checkpoint `optimizer_max_lrs.decoder`; `FINAL_EXPERIMENT_CONFIG.md` | Single LR 1.0e-4 | STALE |
| Refine-head learning rate | 4.5e-4 | Checkpoint `optimizer_max_lrs.refine`; `FINAL_EXPERIMENT_CONFIG.md` | Not reported | STALE |
| Encoder learning rates | Stage 4/3/2/1+stem: 3.0e-5 / 2.4e-5 / 1.92e-5 / 1.536e-5 | Checkpoint `optimizer_max_lrs`; `FINAL_EXPERIMENT_CONFIG.md` | Single LR 1.0e-4 | STALE |
| Layer-wise LR decay | 0.8 | Checkpoint `encoder_layer_decay`; Exp.45 runner | Not reported | STALE |
| Weight decay | Decoder 1.0e-4; encoder 5.0e-2; refine head 1.0e-2 | Exp.45 runner; training log; `source_snapshots/main_torch.py:3151-3165` | 4.0e-4 globally | STALE |
| Scheduler | Five-epoch linear warmup from factor 0.1 to 1.0, then cosine annealing through the remaining epochs to 1.0e-6 | Checkpoint `scheduler_type`; Exp.45 runner; `source_snapshots/main_torch.py:709-725` | Not reported | STALE |
| Epochs | 200 requested/completed; zero-based final epoch 199; best epoch 184 | Checkpoint metadata; training summary; Exp.45 runner | Approximate optimum at epoch 120 | STALE |
| Batch size | 24 | Exp.45 runner | 16 | STALE |
| Augmentation | Independent horizontal/vertical flips (0.5 each), rotation [-15,15] degrees (0.5), crop ratio [0.7,1.0] and resize (0.5), brightness/contrast [0.85,1.15] and saturation [0.9,1.1] jointly (0.5), 3 x 3 Gaussian blur (0.15), Gaussian noise SD 0.015 (0.25); frequency augmentation disabled | `DATASET_SPLIT.md`; `source_snapshots/main_torch.py:1837-2019`; checkpoint/log | Not reported | STALE |
| Loss | 0.55 Dice loss + 0.25 label-smoothed BCE-with-logits (smoothing 0.02) + 0.20 boundary-aware loss (kappa 5); focal-Tversky weight 0 | `FINAL_EXPERIMENT_CONFIG.md`; `source_snapshots/main_torch.py:3060-3103` | Empty loss subsection | STALE |
| Deep supervision | Disabled; zero auxiliary heads | Checkpoint architecture; Exp.45 runner; `FINAL_MODEL_ARCHITECTURE.md` | Later ablation prose says deep supervision is employed | CONTRADICTION |
| EMA | Enabled, decay 0.995; EMA weights used for validation scoring and saved best model | Training log; `source_snapshots/main_torch.py:3952-3960,4035-4041` | Not reported | STALE |
| Precision | AMP FP16 with GradScaler | Checkpoint `training_precision`; training log | Not reported | STALE |
| Gradient clipping | Global maximum norm 1.0 | Exp.45 runner; training log | Not reported | STALE |
| Pretrained weights | ConvNeXt-Tiny `convnext_tiny_22k_1k_384.pth`, logged as ImageNet encoder weights | Exp.45 runner; training log | Not reported | STALE |
| Freeze/unfreeze policy | No staged freeze; all 30,057,415 parameters trainable from epoch 1 | Exp.45 runner; training log; optimizer construction | Not reported | STALE |
| Sampling | Uniform | Checkpoint metadata | Not reported | STALE |
| Early stopping | Patience 30 from epoch 0 was configured; it did not trigger; run completed at maximum epochs | `FINAL_EXPERIMENT_CONFIG.md`; checkpoint `completion_reason=max_epochs` | Says early stopping supervised training and optimum was near epoch 120 | STALE |
| Validation selection procedure | EMA model evaluated on merged Kvasir-SEG/CVC-ClinicDB held-out set at threshold 0.45 | `FINAL_EXPERIMENT_CONFIG.md`; training code | Validation criterion described only as 145 images | STALE |
| Checkpoint-saving criterion | Save only when merged-validation IoU is strictly greater than the previous best | `source_snapshots/main_torch.py:3983-4041`; `FINAL_EXPERIMENT_CONFIG.md` | “Criterion for saving” not defined | STALE |
| Selected checkpoint | Epoch 184, validation IoU 0.8780511022 and Dice 0.9348011783 | Final checkpoint metadata | Approximate optimum near epoch 120 | STALE |
| Prediction threshold | Strict probability > 0.45 | `EVALUATION_PROTOCOL.md`; evaluation summary; `evaluation_core.py:130-155` | Not reported | STALE |
| Evaluation metrics | mDice, mIoU, S-measure, weighted F-measure, mean/max E-measure, MAE | `EVALUATION_PROTOCOL.md`; evaluation summary | Names Dice, IoU, S-measure, generic F-measure, E-measure, MAE | STALE |
| Dice/IoU implementation | Binary per-image Dice and IoU with smoothing 1e-6, then arithmetic mean over images | `EVALUATION_PROTOCOL.md`; `evaluation_core.py:91-98,153-169` | Formulas omit smoothing and incorrectly describe class averaging | STALE |
| SOD metric implementation | `py_sod_metrics` Smeasure, WeightedFmeasure, Emeasure curve mean/max, and MAE, stepped per image using uint8 probability and binary ground truth | `EVALUATION_PROTOCOL.md`; `evaluation_core.py:130-174` | Handwritten definitions; F-measure is not identified as weighted; S-measure equation is malformed | STALE |
| TTA | Disabled | Evaluation summary `tta=false`; Exp.45 runner | Not reported | STALE |
| External-data selection leakage | None; external datasets never influence checkpoint selection | `DATASET_SPLIT.md`; `EVALUATION_PROTOCOL.md` | Not stated | STALE |
| Trainable parameters | 30,057,415 (30,057,415 total) | Evaluation summary; `FINAL_MODEL_ARCHITECTURE.md`; training log | Not stated in implementation details; empty ablation parameter cells | STALE |
| Hardware | NOT VERIFIED | `FINAL_EXPERIMENT_CONFIG.md` reports no final-run GPU evidence | GeForce RTX 3090 24 GB | NOT VERIFIED |
| Framework | PyTorch 2.5.1+cu124 | Final checkpoint environment extraction in `FINAL_EXPERIMENT_CONFIG.md` | “pytorch framework,” no version | STALE |

## 1. Correct settings

- The five dataset names are correct.
- The training counts of 900 Kvasir-SEG and 550 CVC-ClinicDB images are correct.
- The use of AdamW is correct.
- The 352 x 352 input size is correct.
- The manuscript names most metric families, but weighted F-measure and both mean and maximum E-measure require precise naming.

## 2. Stale manuscript values

- The validation split description is stale. The final code independently holds out 10% of Kvasir-SEG and CVC-ClinicDB before merging their training and validation subsets.
- The Kvasir-SEG table entry of 500 test images is incompatible with both the dataset total and final evaluation count of 100.
- The global learning rate 1.0e-4, global weight decay 4.0e-4, batch size 16, and approximate epoch 120 are not the final Exp.45 settings.
- The RTX 3090 statement is unsupported by the final-run evidence and must be removed.
- The metric formulas and descriptions do not match the final implementation, particularly per-image aggregation, smoothing, weighted F-measure, and E-measure curve summaries.
- The unsupported ablation prose and empty placeholder table describe modules, including deep supervision, that are disabled in the selected architecture.

## 3. Missing information

- The draft omits parameter-group learning rates and weight decays, layer-wise LR decay, scheduler/warmup, exact loss, augmentation, EMA, AMP, gradient clipping, pretrained weights, freeze policy, threshold, checkpoint criterion, TTA policy, parameter count, and exact metric aggregation.
- It does not state that external datasets are excluded from checkpoint selection.

## 4. Contradictions

- Within the manuscript, Kvasir-SEG is reported as 1000 total and 900 train but 500 test; the final evidence shows 100 held-out images.
- The manuscript says deep supervision is employed, whereas checkpoint architecture metadata and the Exp.45 runner specify zero deep-supervision heads.
- Within the evidence package, checkpoint field `encoder_stages_unfrozen=0` is a legacy progress field that conflicts semantically with `unfreeze_schedule=none`. The Exp.45 runner, optimizer construction, and training log explicitly establish that all parameters were trainable from epoch 1; therefore the resolved final policy is no freezing.
- Checkpoint fields `cosine_t0=8` and `cosine_t_mult=2` exist but are inactive under the selected `warmup_cosine` scheduler. They must not be reported as final scheduler settings.

## 5. Information that cannot be verified

- Hardware/GPU model: **NOT VERIFIED**.
- A standalone installed `py_sod_metrics` package version: **NOT VERIFIED**.
- CUDA/cuDNN runtime details beyond the checkpoint-extracted PyTorch build string: **NOT VERIFIED**.

## 6. Manuscript changes recommended

- Replace the dataset prose/table with the exact 900/100 and 550/62 splits and full external-test counts.
- Replace implementation details with the final Exp.45 optimizer groups, warmup-cosine schedule, 200 epochs, batch size 24, augmentation, EMA, AMP, clipping, pretraining, and no-freeze policy.
- Add the exact three-term loss and explicitly exclude focal-Tversky and deep supervision from the final run.
- Replace generic metric derivations with the verified per-image Dice/IoU formulas and identify the `py_sod_metrics` implementations without inventing package defaults.
- Add a model-selection subsection distinguishing merged internal validation from external evaluation and documenting threshold 0.45, strict IoU improvement, epoch 184, and disabled TTA.
- Remove unsupported hardware and placeholder ablation claims. Preserve the existing scientific result/comparison tables in this task.
