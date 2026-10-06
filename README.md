# 🤖 SLM Lab

### Small Language Model Inference & Optimization Platform

SLM Lab is a local platform for experimenting with Small Language Models (SLMs).

The project provides a simple interface for running a small language model, controlling text generation, measuring inference performance, benchmarking the model, estimating memory usage, and evaluating generated responses.

---

## 🚀 Features

- Load and run a Small Language Model locally
- Text generation with configurable parameters
- Temperature and Top-p controls
- Maximum token control
- Generation time measurement
- Tokens-per-second measurement
- Model benchmarking across multiple runs
- Parameter count and memory estimation
- Keyword-based response evaluation
- Streamlit-based interactive interface
- CPU-compatible inference

---

## 🧠 Model

SLM Lab currently uses:

**Qwen/Qwen2.5-0.5B-Instruct**

The model contains approximately 0.5 billion parameters and is small enough to experiment with locally.

---

## 🏗️ Architecture

```text
                 ┌─────────────────────┐
                 │     Streamlit UI    │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    Model Loader     │
                 │      Qwen 0.5B      │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │     Inference       │
                 │ Text Generation     │
                 └──────────┬──────────┘
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
        ┌──────────┐  ┌───────────┐  ┌────────────┐
        │Benchmark │  │Evaluation │  │ Quantization│
        └──────────┘  └───────────┘  └────────────┘