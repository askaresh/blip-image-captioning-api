from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    blip_model_name: str = "Salesforce/blip-image-captioning-large"

settings = Settings()

# In config.py
print(dir())  # See what symbols are available at the end of the file
