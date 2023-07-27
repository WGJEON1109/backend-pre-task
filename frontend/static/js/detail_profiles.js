$(document).ready(function () {

    function getContactIdFromUrl() {
        const queryString = window.location.search;
        // console.log(queryString);
        const urlParams = new URLSearchParams(queryString);
        return urlParams.get('id');
    }

    function showContactDetails(contactId) {
        $.ajax({
            url: '/api/profiles/' + contactId,
            type: 'GET',
            dataType: 'json',
            success: function (contact) {
                $('#contact-name').text(contact.name);
                $('#contact-email').text(contact.email);
                $('#contact-phone').text(contact.phone);
                $('#contact-position').text(contact.position);
                $('#contact-company').text(contact.company);
                $('#contact-memo').text(contact.memo);
                $('#contact-birthday').text(contact.birthday);
                $('#contact-address').text(contact.address);
                $('#contact-website').text(contact.website);

                $('#contact-labels').empty();
                if (contact.labels.length > 0) {
                    contact.labels.forEach(function (label) {
                        $('#contact-labels').append('<span class="badge badge-primary mr-1">' + label.name + '</span>');
                    });
                }
                var profilePhotoContainer = document.getElementById('profile-photo-container');
                var img = document.createElement('img');

                var photoUrl = contact.photo_url;
                img.src = photoUrl;
                img.className = 'img-thumbnail';
                img.id = 'profile-photo';
                img.alt = '프로필 사진';
                img.width = 300;
                img.height = 300;
                profilePhotoContainer.appendChild(img);
            },
            error: function (error) {
                console.error('Error:', error);
            }
        });
    }

    // 로그아웃 버튼 출력 함수
    function checkLoginStatus() {
        var token = localStorage.getItem('token');

        if (token) {
            var logoutBtn = document.createElement('button');
            logoutBtn.setAttribute('id', 'logoutBtn');
            logoutBtn.setAttribute('class', 'btn btn-primary float-right');
            logoutBtn.textContent = '로그아웃';
            logoutBtn.addEventListener('click', function () {
                localStorage.removeItem('token');
                $.ajax({
                    url: '/api/auth', // API URL
                    type: 'DELETE',
                    dataType: 'json',
                    beforeSend: function (xhr) {
                        xhr.setRequestHeader("Content-type", "application/json");
                        xhr.setRequestHeader("Authorization", "Bearer " + token);
                    },
                    success: function (data) {
                        location.href = '/login';
                    },
                    error: function (error) {
                        console.error('Error:', error);
                    }
                });

            });

            var logoutBtnContainer = document.getElementById('logoutBtnContainer');
            if (logoutBtnContainer) {
                logoutBtnContainer.appendChild(logoutBtn);
            }
        }
    }

    // 페이지가 로드되면 연락처 ID를 가져와서 상세정보를 표시합니다.
    window.onload = function () {
        var contactId = getContactIdFromUrl();

        // console.log(contact_id)
        if (contactId) {
            showContactDetails(contactId);
        }
    };
    checkLoginStatus();

});

function goBack() {
    window.history.back();
}

function updateProfile() {
    var contactId = "여기에_연락처_ID_가_들어가야합니다";
    window.location.href = "/edit-contact/" + contactId;
}