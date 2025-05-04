function checkName() {
  var name = $("#txtName").val();

  if (name.trim() === "") {
    $("#erName").text("Họ tên không được để trống");
    return false;
  }

  var regex = /^[A-Z][a-z]*(\s+[A-Z][a-z]*)+$/;
  if (!regex.test(name)) {
    $("#erName").text(
      "Mỗi từ phải bắt đầu bằng chữ hoa và phần còn lại viết thường"
    );
    return false;
  }

  $("#erName").text("");
  return true;
}

function checkDateOfBirth() {
  var dob = $("#txtNgaysinh").val();
  var today = new Date();
  var dobDate = new Date(dob);

  if (dob === "") {
    $("#erNgaysinh").text("Ngày sinh không được rỗng");
    return false;
  } else if (dobDate >= today) {
    $("#erNgaysinh").text("Ngày sinh phải trước ngày hiện tại");
    return false;
  } else {
    $("#erNgaysinh").text("");
    return true;
  }
}

function checkPhoneNum() {
  var phone = $("#txtSDT").val();

  if (phone.trim() === "") {
    $("#erSDT").text("Số điện thoại không được để trống");
    return false;
  }

  var regex = /^(09|03|08)\d{8}$/;
  if (!regex.test(phone)) {
    $("#erSDT").text(
      "Số điện thoại phải có 10 số và bắt đầu với 09, 03 hoặc 08"
    );
    return false;
  }

  $("#erSDT").text("");
  return true;
}

function checkEmail() {
  var email = $("#txtEmail").val();

  var regex = /@.*\.com$/;
  if (!regex.test(email)) {
    $("#erEmail").text("Email phải chứa @ và kết thúc với .com");
    return false;
  }

  $("#erEmail").text("");
  return true;
}

function checkStudyMethod() {
  if (!$("input[name='hinhthuc']:checked").length) {
    $("#erHinhthuc").text("Vui lòng chọn hình thức học");
    return false;
  }
  $("#erHinhthuc").text("");
  return true;
}

function checkSkills() {
  if (
    !$("#chkListening").is(":checked") &&
    !$("#chkReading").is(":checked") &&
    !$("#chkWriting").is(":checked")
  ) {
    $("#erSkills").text("Vui lòng chọn ít nhất một kỹ năng cần luyện");
    return false;
  }
  $("#erSkills").text("");
  return true;
}

function updateThoiGianHoc() {
  var selectedCourse = $("#slKhoahoc option:selected");
  var duration = selectedCourse.val();

  $("#txtThoiGianHoc").val(duration + " tháng");
}

function formatDate(dateString) {
  if (!dateString) return "";
  const date = new Date(dateString);
  const day = date.getDate().toString().padStart(2, "0");
  const month = (date.getMonth() + 1).toString().padStart(2, "0");
  const year = date.getFullYear();
  return `${day}/${month}/${year}`;
}

function DangKy() {
  var nameValid = checkName();
  var dobValid = checkDateOfBirth();
  var phoneValid = checkPhoneNum();
  var emailValid = checkEmail();
  var methodValid = checkStudyMethod();
  var skillsValid = checkSkills();

  if (
    !nameValid ||
    !dobValid ||
    !phoneValid ||
    !emailValid ||
    !methodValid ||
    !skillsValid
  ) {
    return;
  }

  var name = $("#txtName").val();
  var sdt = $("#txtSDT").val();
  var ngaysinh = $("#txtNgaysinh").val();
  var email = $("#txtEmail").val();
  var khoahocText = $("#slKhoahoc option:selected").text();
  var hinhthuc = $('input[name="hinhthuc"]:checked').val();

  var skills = [];
  if ($("#chkListening").is(":checked")) skills.push($("#chkListening").val());
  if ($("#chkReading").is(":checked")) skills.push($("#chkReading").val());
  if ($("#chkWriting").is(":checked")) skills.push($("#chkWriting").val());
  var skillsString = skills.join(", ");

  var formattedDate = formatDate(ngaysinh);

  var rowCount = $("#memberList tbody tr").length + 1;
  var newRow = `<tr>
                  <td>${rowCount}</td>
                  <td>${name}</td>
                  <td>${formattedDate}</td>
                  <td>${sdt}</td>
                  <td>${email}</td>
                  <td>${khoahocText}</td>
                  <td>${hinhthuc}</td>
                  <td>${skillsString}</td>
                </tr>`;
  $("#memberList tbody").append(newRow);

  var myModalEl = document.getElementById("myModal");
  var modal = bootstrap.Modal.getInstance(myModalEl);
  modal.hide();

  $(
    '#myModal input[type="text"], #myModal input[type="email"], #myModal input[type="date"]'
  ).val("");
  $('#myModal input[type="checkbox"]').prop("checked", false);
  $("#radioCenter").prop("checked", true);
  $("#slKhoahoc").val("3");
  updateThoiGianHoc();

  $("#erName, #erNgaysinh, #erSDT, #erEmail, #erHinhthuc, #erSkills").text("");
}

$(function () {
  $("#txtName").on("blur", checkName);
  $("#txtNgaysinh").on("blur", checkDateOfBirth);
  $("#txtSDT").on("blur", checkPhoneNum);
  $("#txtEmail").on("blur", checkEmail);

  $("#chkListening, #chkReading, #chkWriting").on("click", checkSkills);

  $("input[name='hinhthuc']").on("click", checkStudyMethod);

  updateThoiGianHoc();

  $("#slKhoahoc").on("change", updateThoiGianHoc);
});
