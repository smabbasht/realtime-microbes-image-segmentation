document.getElementById('imageUpload').addEventListener('change', function(event) {
    const [file] = event.target.files;
    if (file) {
        const container = document.getElementById('result-container');
        container.innerHTML = `
            <div class="image-container">
                <div class="label">Uploaded Image</div>
                <img src="${URL.createObjectURL(file)}" alt="Uploaded Image">
            </div>
        `; // Display uploaded image
        // Enable detect button after uploading image
        document.getElementById('detectButton').disabled = false;
    }
});

document.getElementById('detectButton').addEventListener('click', function() {
    // Disable detect button when it's clicked
    this.disabled = true;

    const imageUpload = document.getElementById('imageUpload');
    if (imageUpload.files.length > 0) {
        const formData = new FormData();
        formData.append('image', imageUpload.files[0]);

        fetch('/detect', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('result-container');
            // Append or update the segmented image container with the title above
            container.innerHTML += `
                <div class="image-container">
                    <div class="label">Segmented Image</div>
                    <img src="${data.processed}?t=${new Date().getTime()}" alt="Segmented Image">
                </div>
            `;
        })
        .catch(error => {
            console.error('Error:', error);
            // Re-enable detect button on error
            document.getElementById('detectButton').disabled = false;
        });
    } else {
        alert('Please upload an image first.');
        // Re-enable detect button if no image is uploaded
        this.disabled = false;
    }
});

