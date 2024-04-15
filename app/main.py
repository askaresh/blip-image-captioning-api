from fastapi import FastAPI, File, UploadFile, HTTPException
import logging.config
from .model import load_model, generate_caption
from .utils import load_image_from_file
from .config import settings

app = FastAPI()

# Load the BLIP model once when the app starts
model, processor = load_model(settings.blip_model_name)

# Configure logging
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

# Example root path handler
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Image Captioning API!"}

@app.post("/caption")
async def caption(image: UploadFile = File(...), text: str = None):
    try:
        if image.content_type not in ["image/jpeg", "image/png"]:
            raise HTTPException(status_code=400, detail="Invalid image format")

        loaded_image = load_image_from_file(await image.read())
        caption = generate_caption(model, processor, loaded_image, text)
        return {"caption": caption}
    except Exception as e:
        logger.exception("Error in /caption endpoint")
        raise HTTPException(status_code=500, detail="Internal server error")
    finally:
        await image.close()