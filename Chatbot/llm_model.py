from llama_cpp import Llama
from llama_cpp_agent.llm_agent import LlamaCppAgent
from llama_cpp_agent.messages_formatter import MessagesFormatterType


class LlmModel:
    def __init__(self, LLM_MODEL_PATH, n_gpu_layers=35, f16_kv=True, use_mlock=False, embedding=False,
                 n_threads=8, n_batch=1024, n_ctx=8192, offload_kqv=True,
                 last_n_tokens_size=1024, verbose=True, seed=-1):
        self.main_model = Llama(
            model_path=LLM_MODEL_PATH,
            n_gpu_layers=n_gpu_layers,
            f16_kv=f16_kv,
            use_mlock=use_mlock,
            embedding=embedding,
            n_threads=n_threads,
            n_batch=n_batch,
            n_ctx=n_ctx,
            offload_kqv=offload_kqv,
            last_n_tokens_size=last_n_tokens_size,
            verbose=verbose,
            seed=seed,
        )

    def get_response(self, system_prompt, user_input):
        llama_cpp_agent = LlamaCppAgent(self.main_model, debug_output=False,
                                        system_prompt=system_prompt,
                                        predefined_messages_formatter_type=MessagesFormatterType.CHATML)

        response = llama_cpp_agent.get_chat_response(user_input, temperature=0.7, print_output=False)
        return response


