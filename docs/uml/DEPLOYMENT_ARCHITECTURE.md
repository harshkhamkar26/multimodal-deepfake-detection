# UML-06 — Deployment Architecture

## 1. Purpose

Define the intended execution topology while keeping deployment choices flexible until the implementation and compute assessment are complete.

## 2. Research / Training Deployment

```text
┌──────────────────────────── Research Workstation / GPU ────────────────────────────┐
│                                                                                    │
│  Experiment Runner                                                                │
│       │                                                                            │
│       ├── Dataset Manifest / Approved Split                                       │
│       ├── Video Training Pipeline ───────► GPU/CPU                                │
│       ├── Audio Training Pipeline ───────► GPU/CPU                                │
│       ├── Fusion Training Pipeline ──────► GPU/CPU                                │
│       └── Evaluation / Metrics                                                     │
│                    │                                                               │
│                    ▼                                                               │
│              Results / Model Artifacts                                             │
└────────────────────────────────────────────────────────────────────────────────────┘
                         │
                         │ versioned / explicitly registered
                         ▼
                  Model Artifact Store
```

## 3. Inference Deployment

```text
┌──────────────────┐
│ User Browser     │
└────────┬─────────┘
         │ HTTPS / API request
         ▼
┌─────────────────────────────┐
│ Application / API Server    │
│ input validation            │
│ inference orchestration     │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ Inference Runtime           │
│ video pipeline              │
│ audio pipeline              │
│ fusion                      │
│ prediction                  │
│ explainability              │
└──────────────┬──────────────┘
               │
               ├──────────────► Model Artifact Store
               │
               ▼
┌─────────────────────────────┐
│ Result / Temporary Storage  │
└─────────────────────────────┘
```

## 4. Security and Operational Boundaries

- Uploaded media is treated as untrusted input.
- File size, format, duration, and processing limits are enforced before expensive inference.
- Secrets/configuration are supplied through environment or deployment configuration and are never committed.
- Raw user uploads should not be retained longer than required by the application policy.
- Model artifacts are versioned and associated with the preprocessing/configuration assumptions under which they were trained.

## 5. Deployment Options

The architecture supports:

- local research/demo deployment;
- a single GPU server;
- containerized deployment;
- separate API and inference workers if required by load.

The project will select the simplest deployment that satisfies the demonstration and research requirements. Distributed/cloud infrastructure is not a requirement for the research contribution.
