
from flask import Blueprint, render_template, request
from PIL import Image, UnidentifiedImageError

from services.ocr_service import extract_text


document_bp = Blueprint("documents", __name__)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}


def allowed_file(filename):
    """Check whether the uploaded filename has an allowed extension."""

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@document_bp.route("/read-document", methods=["POST"])
def read_document():

    # Check whether the user selected a file.
    if "image_file" not in request.files:
        return render_template(
            "result.html",
            error="No document was selected."
        )

    uploaded_file = request.files["image_file"]

    # Check whether the file is empty.
    if uploaded_file.filename == "":
        return render_template(
            "result.html",
            error="Please select a document image."
        )

    # Check the file extension.
    if not allowed_file(uploaded_file.filename):
        return render_template(
            "result.html",
            error="Please upload a PNG, JPG, JPEG or WEBP image."
        )

    try:
        # Open the uploaded image directly without saving it.
        image = Image.open(uploaded_file.stream)

        # Verify that the uploaded file is a valid image.
        image.load()

        # Extract written text using our OCR service.
        extracted_text = extract_text(image)

        return render_template(
            "result.html",
            extracted_text=extracted_text,
            filename=uploaded_file.filename
        )

    except (UnidentifiedImageError, OSError):
        return render_template(
            "result.html",
            error="The uploaded file is not a valid or readable image."
        )

    except Exception:
        return render_template(
            "result.html",
            error="Something went wrong while reading the document. Please try again."
        )
