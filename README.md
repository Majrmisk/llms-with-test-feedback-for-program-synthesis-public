# LLMs with Test Feedback for Program Synthesis

A command‐line tool for iteratively generating and validating Python functions using local Huggingface LLMs designed to run on the [MUNI Aura server](https://www.fi.muni.cz/tech/unix/aura.html.cs).

Given a natural language description and unit tests, it runs the model, executes tests, and feeds back failures until the code passes or a limit is reached.

This repo is part of a bachelor’s thesis at Masaryk University and includes a suite of prompt+test tasks across nine categories on which the pipeline was evaluated.

---

## Installation & Setup

1. Clone the repo  

2. Install dependencies  

   pip install -r requirements.txt  

3. Download models (example for Qwen-7B)  

   git clone https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct 

4. Configure paths  
   - In `code/config.py`, set `MODEL_PATH` to your model folder

---

## Usage example

```
# Single-mode: one prompt/test pair
python --single -m 0 prompt.txt tests.py

# Folder-mode: process all subfolders of `examples`
python --folder -m 1 examples output.txt
```  

Run `python code/main.py --help` to see all options.

---

## Structure
```
.
├── code
│   ├── cli
│   │   └── parser.py
│   ├── llm
│   │   └── llm_manager.py
│   ├── prompts
│   │   ├── main_prompt.py
│   │   └── prompt_manager.py
│   ├── tester
│   │   ├── conftest.py
│   │   └── test_runner.py
│   ├── config.py
│   └── main.py
├── tasks                        # text prompts + test definitions
│   ├── main
│   └── unclear_prompts
└── LLMs_with_Test_Feedback.pdf  # Thesis PDF
```

---

## Libraries Used

- torch - GPU-accelerated model execution

- transformers - Hugging Face model loading & tokenization

- pytest - automated test runner

---

## License
This project is licensed under the [Apache License 2.0](./LICENSE).
