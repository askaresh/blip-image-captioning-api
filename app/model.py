import logging
from transformers import BlipProcessor, BlipForConditionalGeneration

logger = logging.getLogger(__name__)

def load_model(model_name):
    try:
        # Load the pre-trained BLIP model for image-to-text captioning
        processor = BlipProcessor.from_pretrained(model_name)
        model = BlipForConditionalGeneration.from_pretrained(model_name)
        logger.info(f"Loaded model: {model_name}")
        return model, processor
    except Exception as e:
        logger.exception(f"Error loading model: {model_name}")
        raise e

def generate_caption(model, processor, image, text=None):
    try:
        # Prepare the inputs for captioning
        if text is not None:
            # Conditional image captioning
            inputs = processor(image, text, return_tensors="pt")
        else:
            # Unconditional image captioning
            inputs = processor(image, return_tensors="pt")

        # Generate the caption
        out = model.generate(**inputs, max_new_tokens=200)
        caption = processor.decode(out[0], skip_special_tokens=True)
        logger.info(f"Generated caption: {caption}")

        return caption
    except Exception as e:
        logger.exception("Error during caption generation")
        raise e