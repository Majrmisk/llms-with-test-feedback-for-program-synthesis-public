import torch
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM
)
from config import LLM_MAX_NEW_TOKENS


class LlmManager:
    def __init__(self, llm_dir: str):
        self.llm_dir = llm_dir
        self.tokenizer = None
        self.model = None
        self.load_llm()

    def load_llm(self) -> None:
        if (not torch.cuda.is_available()):
            raise EnvironmentError("Error loading LLM: GPUs not available.")

        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.llm_dir)
            self.model = self.__load_model()
        except Exception as e:
            raise RuntimeError(f"Error loading LLM: {e}")

    def generate_response(self, prompt: str) -> str:
        try:
            inputs = self.tokenizer(
                [prompt],
                return_tensors="pt"
            ).to(self.model.device)

            generated_ids = self.model.generate(
                **inputs,
                max_new_tokens=LLM_MAX_NEW_TOKENS,
            )
            generated_ids = [
                output_ids[len(input_ids):]
                for input_ids, output_ids in
                zip(inputs.input_ids, generated_ids)
            ]
            return self.tokenizer.batch_decode(
                generated_ids,
                skip_special_tokens=True)[0]

        except Exception as e:
            raise RuntimeError(f"LLM generation error: {e}")

    def __load_model(self):
        best_gpu = self.__get_free_gpu()

        try:
            return torch.compile(AutoModelForCausalLM.from_pretrained(
                self.llm_dir,
                torch_dtype=torch.bfloat16,
                device_map={"": best_gpu},
                attn_implementation="flash_attention_2"
            ))
        except (torch.OutOfMemoryError):
            print("Could not load model onto one GPU, trying auto device map.")
            torch.cuda.empty_cache()

        return torch.compile(AutoModelForCausalLM.from_pretrained(
            self.llm_dir,
            torch_dtype=torch.bfloat16,
            device_map="auto",
            attn_implementation="flash_attention_2"
        ))

    def __get_free_gpu(self) -> None:
        num_gpus = torch.cuda.device_count()
        if num_gpus == 0:
            raise EnvironmentError("Error loading LLM: GPUs not available.")

        free_memories = {
            i: torch.cuda.mem_get_info(i)[0] for i in range(num_gpus)}
        return max(free_memories, key=free_memories.get)
