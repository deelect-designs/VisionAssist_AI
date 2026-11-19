
import pytesseract

from PIL import Image, ImageOps


# Tell Python where Tesseract is installed on Windows.
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def extract_text(image):
    """
    Extract written text from an uploaded image.

    Args:
        image: A Pillow Image object.

    Returns:
        Extracted text as a string.
    """

    if not isinstance(image, Image.Image):
        raise TypeError("The supplied file must be an image.")

    # Convert the image into a format suitable for OCR.
    image = image.convert("RGB")

    # Improve image readability before text recognition.
    processed_image = ImageOps.grayscale(image)
    processed_image = ImageOps.autocontrast(processed_image)

    # Extract English text using Tesseract.
    extracted_text = pytesseract.image_to_string(
        processed_image,
        lang="eng",
        config="--psm 6"
    )

    return extracted_text.strip()
