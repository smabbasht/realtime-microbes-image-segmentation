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
    }
});

document.getElementById('detectButton').addEventListener('click', function() {
    const imageUpload = document.getElementById('imageUpload');
    if (imageUpload.files.length > 0) {
        const formData = new FormData();
        formData.append('image', imageUpload.files[0]);
        // check if already there are two containers then overwrite the image in the second one, 
        // else create a new container


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
                    <img src="${data.processed}" alt="Segmented Image">
                </div>
            `;
        })
        .catch(error => console.error('Error:', error));
    } else {
        alert('Please upload an image first.');
    }
});

