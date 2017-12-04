/**
 * Created by Nurs on 03.07.2017.
 */

$(document).ready(function () {
    var fileInput = $('#advert_images');
    // var helpText = $('#file-counter');
    var uploadedImagesRow = $('#upload-images-row');
    var newFileArray = [];
    var form = $(fileInput).parent().parent();
    var removedImages = $('#id_removed_images');
    var uploadLink = $(form).attr('data-media-upload-url');
    var removeUploadedLink = $(form).attr('data-remove-uploaded-media-url');
    $(uploadedImagesRow).slideUp('fast');
    $(fileInput).on('change', function (event) {
        if ($(removedImages).val() !== '') {
            var alreadyRemovedImages = $(removedImages).val().split(',');
            alreadyRemovedImages.forEach(function (obj, i, element) {
                newFileArray.push(obj);
            });
        }
        if (newFileArray.length > 1) {
            var ids = '';
            newFileArray.forEach(function (obj, index, element) {
                ids = ids !== '' ? ids + ',' + obj : obj;
            });
            $.ajax({
                url: removeUploadedLink,
                method: 'POST',
                dataType: 'JSON',
                data: {'media_ids': ids},
                success: function (response) {
                    if (response.done) {
                        $(removedImages).val('');
                    }
                },
                error: function () {

                }
            });
        }
        newFileArray = [];
        $(uploadedImagesRow).html('');

        var formData = new FormData();
        $.each(this.files, function (i, file) {
            formData.append('file-' + i, file);
        });
        console.log(FormData);
        console.log(form.files);
        // formData.append('csrfmiddlewaretoken', getCookie('csrftoken'));

        $.ajax({
            url: uploadLink,
            data: formData,
            cache: false,
            contentType: false,
            processData: false,
            method: 'POST',
            dataType: 'JSON',
            success: function (response) {
                response.uploaded_files.forEach(function (obj, index, element) {
                    $(uploadedImagesRow).append('<div class="one-image" style="width: 100px;height: 100px;float: left;position:relative;" data-id="' + obj.id + '">' +
                        '<span class="remove-image" style="position:absolute; right: 5px;top: 5px">X</span>' +
                        '<img src="' + obj.url + '" style="width: 100%;height: 100%;object-fit: cover" ">' +
                        '</div>');
                    initRemoveButtons();
                    newFileArray.push(obj.id);
                    console.log(newFileArray)
                });
                $(uploadedImagesRow).slideDown('slow');
            },
            error: function () {
                console.log('Can\'t send upload request...');
            }
        });

    });

    $(form).on('submit', function (e) {
        e.preventDefault();
        var trueFileInput = $('#id_images');
        console.log(newFileArray);
        newFileArray.forEach(function (obj, index, element) {
            var value = $(trueFileInput).val();
            $(trueFileInput).val(value !== '' ? value + ',' + obj : obj);
        });
        console.log($(trueFileInput).val());
        console.log($(this).serialize())
        this.submit();
    });

    function initRemoveButtons() {
        var buttons = $('span.remove-image');

        $(buttons).each(function (i, obj) {
            $(obj).unbind().bind('click', function (event) {
                $(obj).parent().fadeOut('slow', function () {
                    var imageId = parseInt($(obj).parent().attr('data-id'));
                    newFileArray.splice(imageId, 1);
                    if (newFileArray.length > 1) {
                        $(fileInput).val(null);
                    }
                    var alreadyRemovedImages = $(removedImages).val();
                    $(removedImages).val(alreadyRemovedImages !== '' ? alreadyRemovedImages + ',' + imageId : imageId);
                    $(obj).parent().remove();
                });
            });
        });
    }
});