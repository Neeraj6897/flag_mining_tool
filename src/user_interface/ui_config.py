import os
from configparser import ConfigParser

os.environ["SSL_CERT_FILE"] = "./cacert.pem"

class Config:
    def __init__(self, config_file="./Agentic_AI/FlagMiningTool/flag_mining_tool/src/user_interface/ui_config.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        return self.config['DEFAULT'].get("USECASE_OPTIONS").split(", ")
    
    def get_groq_model_options(self):
        return self.config['DEFAULT'].get("GROQ_MODEL_OPTIONS").split(", ")
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")