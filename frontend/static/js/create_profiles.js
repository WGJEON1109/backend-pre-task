$(document).ready(function () {
    getLabels();

    // 라벨 생성 클릭 시
    $("#createLabelBtn").on("click", function () {
        var labelName = $("#label-name").val();

        var data = {
            name: labelName
        };
        console.log(data);
        $.ajax({
            url: '/api/labels',
            type: 'POST',
            dataType: 'json',
            data: data,
            success: function (response) {
                console.log("라벨 생성 성공:", response);
                $("#label").val(labelName);
                $("#addLabelModal").modal("hide");
                getLabels();
            },
            error: function (error) {
                console.error('Error:', error);
            }
        });
    });

    // 저장 버튼 클릭 시
    $("#createProfileBtn").on("click", function () {
        // 필수 입력 필드 확인
        var requiredFields = ["name", "email", "phone"];
        var isFormValid = true;
        var token = localStorage.getItem("token");

        for (var i = 0; i < requiredFields.length; i++) {
            var fieldValue = $("#" + requiredFields[i]).val();
            if (fieldValue.trim() === "") {
                alert(requiredFields[i] + " 필드를 입력해주세요.");
                isFormValid = false;
                break;
            }
        }
        if (isFormValid) {
            var name = $("#name").val();
            var email = $("#email").val();
            var phone = $("#phone").val();
            var company = $("#company").val();
            var position = $("#position").val();
            var memo = $("#memo").val();
            var label = $("#labels").val();
            var address = $("#address").val();
            var birthday = $("#birthday").val();
            var website = $("#website").val();
            console.log(label);
            var labels_data = [];
            if (label !== "") {
                label_data = label.split(' ');
                var labels_data = [];
                label_data.forEach(function (item) {
                    labels_data.push({ name: item });
                });
            }

            console.log(labels_data);
            if (birthday === "") {
                birthday = null;
            }

            var data = {
                name: name,
                email: email,
                phone: phone,
                company: company,
                position: position,
                memo: memo,
                labels: labels_data,
                address: address,
                birthday: birthday,
                website: website
            };
            $.ajax({
                url: '/api/profiles',
                type: 'POST',
                dataType: 'json',
                data: JSON.stringify(data),
                // contentType: 'application/json',
                beforeSend: function (xhr) {
                    xhr.setRequestHeader("Content-type", "application/json");
                    xhr.setRequestHeader("Authorization", "Bearer " + token);
                },
                success: function (response) {
                    alert("저장 성공");
                    console.log("연락처 저장 성공:", response);
                },
                error: function (request, status, error) {
                    alert("code:" + request.status + "\n" + "message:" + request.responseText + "\n" + "error:" + error);
                    console.log(request.responseText);
                }
            });
        }
    });

    // 라벨 선택 시
    $("#labels").on("input", function () {
        var inputText = $(this).val();
        var labels = inputText.split(" ").filter(label => label !== '');
        var output = '';
        labels.forEach(function (label) {
            output += '<span class="badge badge-primary badge-lg mr-2">' + label + '</span>';
        });
        $("#labelSuggestions").html(output);
    });

    // 라벨 불러오기
    function getLabels() {
        $.ajax({
            url: '/api/labels',
            type: 'GET',
            dataType: 'json',
            success: function (labels) {
                var labelSuggestions = $("#labelSuggestions");
                labelSuggestions.empty();
                labels.forEach(function (label) {
                    var suggestion = $('<span class="badge badge-primary badge-lg mr-2">' + label.name + '</span>');
                    suggestion.on("click", function () {
                        var currentLabels = $("#labels").val();
                        var newLabel = $(this).text();
                        if (currentLabels === '') {
                            $("#labels").val(newLabel);
                        } else {
                            $("#labels").val(currentLabels + ' ' + newLabel);
                        }
                    });
                    suggestion.css('cursor', 'pointer');
                    labelSuggestions.append(suggestion);
                });
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

    checkLoginStatus();


});

function goBack() {
    window.location.href = "/";
}
