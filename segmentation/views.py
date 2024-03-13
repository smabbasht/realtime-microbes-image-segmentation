from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.conf import settings
import os
import time

# Simulated image processing function


def segment_image(image):
    # @Hussain add your logic here, return the processed_image, model_folder ka
    # path main ne bnadia hai for your ease.
    model_folder = "model"
    processed_image = image  # do something here
    return processed_image


@csrf_exempt
def process_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']

        # check number of files in media folder
        media_folder = os.path.join(settings.MEDIA_ROOT)
        files = len(os.listdir(media_folder))
        filename = "model_output_" + str(files) + ".png"

        processed_image = segment_image(image)
        save_path = os.path.join(settings.MEDIA_ROOT, filename)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        if os.path.exists(save_path):
            os.remove(save_path)
        # Save the "processed" image to the specified path
        with open(save_path, 'wb+') as destination:
            for chunk in processed_image.chunks():
                destination.write(chunk)

        processed_image_url = os.path.join(
            settings.MEDIA_URL, filename)

        return JsonResponse({
            'processed': processed_image_url,
        })

    else:
        return JsonResponse({'error': 'No image uploaded'}, status=400)


def dashboard(request):
    return render(request, 'segmentation/dashboard.html')
