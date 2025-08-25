import cloudinary
from ..utils.constants import CLOUDINARY_SECRETS
import cloudinary.uploader
from cloudinary.utils import cloudinary_url


def set_cloudinary_config() -> None:
    """Set Cloudinary configuration."""
    cloudinary.config(
        cloud_name=CLOUDINARY_SECRETS.CLOUD_NAME.value,
        api_key=CLOUDINARY_SECRETS.API_KEY.value,
        api_secret=CLOUDINARY_SECRETS.API_SECRET.value,
        secure=True
    )

    # # Upload an image
    # upload_result = cloudinary.uploader.upload("https://res.cloudinary.com/demo/image/upload/getting-started/shoes.jpg",
    #                                            public_id="shoes")
    # print(upload_result["secure_url"])
    #
    # # Optimize delivery by resizing and applying auto-format and auto-quality
    # optimize_url, _ = cloudinary_url("shoes", fetch_format="auto", quality="auto")
    # print(optimize_url)
    #
    # # Transform the image: auto-crop to square aspect_ratio
    # auto_crop_url, _ = cloudinary_url("shoes", width=500, height=500, crop="auto", gravity="auto")
    # print(auto_crop_url)
