# a manager class that can
# load an autogen flow run an autogen flow and return the response to the client


from typing import Dict
import autogen

from uniswap import answer_uniswap_question
from .marketer import MarketerAgent
from .utils import parse_token_usage
import time


class Manager(object):
    def __init__(self) -> None:

        pass

    def run_flow(self, prompt: str, flow: str = "default") -> None:
        autogen.ChatCompletion.start_logging(compact=False)
        config_list = autogen.config_list_openai_aoai()

        llm_config = {
            "seed": 42,  # seed for caching and reproducibility
            "config_list": config_list,  # a list of OpenAI API configurations
            "temperature": 0,
            "function": [{
                "name":"answer_uniswap_question",
                "description": "Ответ на любой Uniswape вопрос",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "question": {
                            "type": "string",
                            "description": "Вопрос, который следует задать согласно uniswap",
                        },
                    },
                    "required": ["question"],
                },
            }], # temperature for sampling
            "use_cache": True,  # whether to use cache
        }
        # Копирайтер пишет текст рекламы на тему продукта которого укажет пользователь
        copywriter = autogen.AssistantAgent(
            name="Копирайтер",
            max_consecutive_auto_reply=3, llm_config=llm_config,
            system_message=f"Создаёт рекламу для какого либо продукта",
        )
        # маркетолог должен проанализировать и дать список рекомендаций на основе pdf книги
        marketer = MarketerAgent(name="Маркетолог",
                                 max_consecutive_auto_reply=3,
                                 llm_config=llm_config,
                                 system_message="Анализирует созданную рекламу Копирайтером и дайт рекомендацию согласно full_documents")
        # create a UserProxyAgent instance named "user_proxy"
        user_proxy = autogen.UserProxyAgent(
            name="user_proxy",
            human_input_mode="NEVER",
            llm_config=llm_config,
            max_consecutive_auto_reply=3,
            is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
            code_execution_config={
                "work_dir": "scratch/coding",
                "use_docker": False
            },
            system_message=f"Копирайтер напиши рекламу про {prompt}",function_map={"answer_uniswap_question": answer_uniswap_question},
        )
        groupchat = autogen.GroupChat(agents=[user_proxy,copywriter,marketer],messages=[],max_round=4)
        manager =autogen.GroupChatManager(groupchat=groupchat,llm_config=llm_config)
        start_time = time.time()
        user_proxy.initiate_chat(
            manager,
            message=prompt,
        )

        messages = user_proxy.chat_messages[manager]
        logged_history = autogen.ChatCompletion.logged_history
        autogen.ChatCompletion.stop_logging()
        response = {
            "messages": messages[1:],
            "usage": parse_token_usage(logged_history),
            "duration": time.time() - start_time,
        }
        return response
