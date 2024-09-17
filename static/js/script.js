document.getElementById('image-upload').addEventListener('change', function (e) {
    var reader = new FileReader();
    reader.onload = function (event) {
        document.getElementById('preview-image').src = event.target.result;
    };
    reader.readAsDataURL(e.target.files[0]);
});
