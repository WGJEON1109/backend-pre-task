$(document).ready(function () {
    var profiles_list = [];

    function loadContacts() {
        var token = localStorage.getItem('token');
        $.ajax({
            url: '/api/profiles', // API URL
            type: 'GET',
            dataType: 'json',
            beforeSend: function (xhr) {
                xhr.setRequestHeader("Content-type", "application/json");
                xhr.setRequestHeader("Authorization", "Bearer " + token);
            },
            success: function (data) {
                profiles_list = data;
                displayContacts(data); // 데이터 출력
            },
            error: function (error) {
                console.error('Error:', error);
            }
        });
    }

    function displayContacts(contacts) {
        var contactList = $('#contact-list');
        contactList.empty();

        for (var i = 0; i < contacts.length; i++) {
            var contact = contacts[i];
            var labelsHtml = ''; // 라벨을 배열로 처리하여 출력
            for (var j = 0; j < contact.labels.length; j++) {
                labelsHtml += '<span class="badge badge-primary mr-2">' + contact.labels[j].name + '</span>';
            }

            var row = ` 
                <tr data-id=${contact.id}>
                    <td>${contact.name}</td>
                    <td>${contact.email}</td>
                    <td>${contact.phone}</td>
                    <td>${contact.position}, ${contact.company}</td>
                    <td>${labelsHtml}</td>
                </tr>
            `;             // 각 주소록 데이터를 테이블 행으로 구성하여 화면에 추가
            contactList.append(row);
        }
    }

    function sortProfilesList(field, order) {
        profiles_list.sort(function (a, b) {
            if (field === "id") {
                var valA = a["id"]
                var valB = b["id"]
            } else {
                var valA = a[field].toUpperCase();
                var valB = b[field].toUpperCase();
            }
            if (valA < valB) {
                return order === 'asc' ? -1 : 1;
            } else if (valA > valB) {
                return order === 'asc' ? 1 : -1;
            }
            return 0;
        });

        displayContacts(profiles_list);
    }

    $(".sortable").on("click", function () {
        var field = $(this).data("field");
        var order = $(this).data("order") || "asc";
        if (order === "asc") {
            $(this).data("order", "desc");
            $(this).find(".sort-icon").removeClass("fa-sort").addClass("fa-sort-down");
        } else if (order === "desc") {
            $(this).data("order", "clear");
            $(this).find(".sort-icon").removeClass("fa-sort-down").addClass("fa-sort-up");
        }
        $(this).siblings(".sortable").data("order", null);
        $(this).siblings(".sortable").find(".sort-icon").removeClass('fa-sort-up').removeClass('fa-sort-down').addClass('fa-sort');

        if (order === 'clear') {
            sortProfilesList('id', 'asc'); // 기본 정렬 순서로 정렬해
            $(this).data('order', null); // 데이터 속성을 null로 설정하여 정렬 상태를 해제
            $(this).find('.sort-icon').removeClass('fa-sort-up').removeClass('fa-sort-down').addClass('fa-sort');
        } else {
            sortProfilesList(field, order);
        }
    });

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

    checkLoginStatus();
    loadContacts();

});

// 상세보기 이벤트 리스너
$('tbody').on('click', 'tr', function () {
    // console.log($(this).data('id'));
    var contactId = $(this).data('id');
    window.location.href = '/detail?id=' + contactId;
});

function goToCreate() {
    window.location.href = '/create';
};



