var currentUser = document.getElementById('userSelection').value;
var displayedImages = [];
var noMorePic = false;
var imageCount = 0;
var imageList = [];

fetch('/current_user', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: 'username=' + encodeURIComponent(currentUser),
})

fetch('/get_used_images')
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        displayedImages = data;
    })
    .catch(function (error) {
        console.error('Error:', error);
    });

fetch('/number_of_images')
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        imageCount = data.length;
        imageList = data.image_files;
    })
    .catch(function (error) {
        console.error('Error:', error);
    });

function changeUser() {
    currentUser = document.getElementById('userSelection').value;

    fetch('/current_user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'username=' + encodeURIComponent(currentUser),
    })

    fetch('/get_used_images')
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            displayedImages = data;
            if (displayedImages.length == imageCount) {
                noMorePic = true;
                disableButtons();
                changeImage();
            } else {
                noMorePic = false;
                enableButtons();
                changeImage();
            }
        })
        .catch(function (error) {
            console.error('Error:', error);
        });
}

function getImageTag() {
    if (displayedImages.length == imageCount) {
        noMorePic = true;
        return '<p id="no-more-images">No more images to show</p>';
    }

    var randomImage;
    do {
        randomImage = imageList[Math.floor(Math.random() * imageCount)];
        var imageNameWithoutExtension = randomImage.replace(/\.[^/.]+$/, "");
    } while (displayedImages.includes(imageNameWithoutExtension));

    displayedImages.push(imageNameWithoutExtension);
    console.log(displayedImages);

    var testImage = new Image();
    testImage.src = 'static/images/' + randomImage;
    console.log(testImage);

    if (testImage.width > 0) {
        return '<img src="' + testImage.src + '"/>';
    } else {
        return '<img src="' + testImage.src + '" alt="Oh no, the image is broken!"/>';
    }
}

function changeImage() {
    var imageContainer = document.getElementById('image-container');
    imageContainer.innerHTML = getImageTag();
    document.getElementById('myCheckbox').checked = false;

    if (noMorePic) {
        disableButtons();
    }
}

function disableButtons() {
    var buttons = document.querySelectorAll('.button-container button');
    buttons.forEach(function (button) {
        button.disabled = true;
    });
}

function enableButtons() {
    var buttons = document.querySelectorAll('.button-container button');
    buttons.forEach(function (button) {
        button.disabled = false;
    });
}

window.addEventListener('load', function () {
    changeImage();
});

function recordFeedback(feedbackValue) {
    var comments = document.getElementById('comments').value;
    var imageName = displayedImages[displayedImages.length - 1];
    var isCheckboxChecked = document.getElementById('myCheckbox').checked;

    fetch('/record_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'username=' + encodeURIComponent(currentUser) + '&score=' + encodeURIComponent(feedbackValue) + '&comments=' + encodeURIComponent(comments) + '&imageName=' + encodeURIComponent(imageName) + "&hard=" + encodeURIComponent(isCheckboxChecked),
    })
        .then(response => response.text())
        .then(data => {
            changeImage();
            document.getElementById('comments').value = '';
        })
        .catch(error => {
            console.error('Error:', error);
        });
}