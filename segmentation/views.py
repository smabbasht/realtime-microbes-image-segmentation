from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.core.files.base import ContentFile
from django.conf import settings
import os
import time


# Simulated image processing function
def segment_image(image):
    # For now, it simply returns the image file as is
    # Replace this with your actual image processing logic
    # add 3 secs wait
    return image


@csrf_exempt
def process_image(request):
    if request.method == 'POST' and request.FILES['image']:
        # Read the uploaded image file
        image = request.FILES['image']

        # Simulate image processing (replace with actual logic later)
        processed_image = segment_image(image)

        # Define path for saving the processed image
        save_path = os.path.join(settings.MEDIA_ROOT, 'model_output.png')

        # Ensure the directory exists
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Save the "processed" image to the specified path
        with open(save_path, 'wb+') as destination:
            for chunk in processed_image.chunks():
                destination.write(chunk)

        # Generate the URL for the saved image
        processed_image_url = os.path.join(
            settings.MEDIA_URL, 'model_output.png')

        # Respond with the URL to the processed image
        return JsonResponse({
            'processed': processed_image_url,
        })

    else:
        return JsonResponse({'error': 'No image uploaded'}, status=400)


def dashboard(request):
    return render(request, 'segmentation/dashboard.html')
