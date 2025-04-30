/**
 * Validate the name field
 * Requirements: Not empty, each word must start with uppercase (e.g., Le Van An)
 */
function checkName() {
  var name = $("#txtName").val();

  // Check if name is empty
  if (name.trim() === "") {
    $("#erName").text("Họ tên không được để trống");
    return false;
  }

  // Use regex to validate name format: words starting with uppercase, followed by lowercase
  // Must have at least two words separated by spaces
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

/**
 * Validate the date of birth field
 * Requirements: Not empty, must be before current date
 */
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

/**
 * Validate the phone number field
 * Requirements: Not empty, 10 digits starting with 09, 03, or 08
 */
function checkPhoneNum() {
  var phone = $("#txtSDT").val();

  // Check if phone is empty
  if (phone.trim() === "") {
    $("#erSDT").text("Số điện thoại không được để trống");
    return false;
  }

  // Check phone format: 10 digits starting with 09, 03, or 08
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

/**
 * Validate the email field
 * Requirements: Must contain @ and end with .com
 */
function checkEmail() {
  var email = $("#txtEmail").val();

  // Check email format: must contain @ and end with .com
  var regex = /@.*\.com$/;
  if (!regex.test(email)) {
    $("#erEmail").text("Email phải chứa @ và kết thúc với .com");
    return false;
  }

  $("#erEmail").text("");
  return true;
}

/**
 * Validate the study method selection
 * Requirements: At least one option must be selected
 */
function checkStudyMethod() {
  // Check if a study method is selected
  if (!$("input[name='hinhthuc']:checked").length) {
    $("#erHinhthuc").text("Vui lòng chọn hình thức học");
    return false;
  }
  $("#erHinhthuc").text("");
  return true;
}

/**
 * Validate the skills selection
 * Requirements: At least one skill must be selected
 */
function checkSkills() {
  // Check if at least one skill is selected
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

/**
 * Update the study duration field based on selected course
 */
function updateThoiGianHoc() {
  var selectedCourse = $("#slKhoahoc option:selected");
  var duration = selectedCourse.val();

  // Update the thời gian học textbox
  $("#txtThoiGianHoc").val(duration + " tháng");
}

/**
 * Format date from yyyy-mm-dd to dd/mm/yyyy
 */
function formatDate(dateString) {
  if (!dateString) return "";
  const date = new Date(dateString);
  const day = date.getDate().toString().padStart(2, "0");
  const month = (date.getMonth() + 1).toString().padStart(2, "0");
  const year = date.getFullYear();
  return `${day}/${month}/${year}`;
}

/**
 * Register a new course enrollment
 * Validates all fields before proceeding
 */
function DangKy() {
  // Check all validations and store results
  var nameValid = checkName();
  var dobValid = checkDateOfBirth();
  var phoneValid = checkPhoneNum();
  var emailValid = checkEmail();
  var methodValid = checkStudyMethod();
  var skillsValid = checkSkills();

  // Only proceed if all validations pass
  if (
    !nameValid ||
    !dobValid ||
    !phoneValid ||
    !emailValid ||
    !methodValid ||
    !skillsValid
  ) {
    return; // Stop if any validation fails
  }

  // Gather form data
  var name = $("#txtName").val();
  var sdt = $("#txtSDT").val();
  var ngaysinh = $("#txtNgaysinh").val();
  var email = $("#txtEmail").val();
  var khoahocText = $("#slKhoahoc option:selected").text();
  var hinhthuc = $('input[name="hinhthuc"]:checked').val();

  // Collect selected skills
  var skills = [];
  if ($("#chkListening").is(":checked")) skills.push($("#chkListening").val());
  if ($("#chkReading").is(":checked")) skills.push($("#chkReading").val());
  if ($("#chkWriting").is(":checked")) skills.push($("#chkWriting").val());
  var skillsString = skills.join(", ");

  // Format the date for display
  var formattedDate = formatDate(ngaysinh);

  // Add new row to the table
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

  // Hide the modal using Bootstrap 5
  var myModalEl = document.getElementById("myModal");
  var modal = bootstrap.Modal.getInstance(myModalEl);
  modal.hide();

  // Reset form
  $(
    '#myModal input[type="text"], #myModal input[type="email"], #myModal input[type="date"]'
  ).val("");
  $('#myModal input[type="checkbox"]').prop("checked", false);
  $("#radioCenter").prop("checked", true);
  $("#slKhoahoc").val("3");
  updateThoiGianHoc(); // Update thời gian học after resetting the form

  // Clear error messages
  $("#erName, #erNgaysinh, #erSDT, #erEmail, #erHinhthuc, #erSkills").text("");
}

// Initialize when the document is ready
$(document).ready(function () {
  // Add real-time validation
  $("#txtName").blur(checkName);
  $("#txtNgaysinh").blur(checkDateOfBirth);
  $("#txtSDT").blur(checkPhoneNum);
  $("#txtEmail").blur(checkEmail);

  // For checkboxes, validate whenever any checkbox is clicked
  $("#chkListening, #chkReading, #chkWriting").click(checkSkills);

  // For radios, validate whenever any radio button is clicked
  $("input[name='hinhthuc']").click(checkStudyMethod);

  // Set initial value for thời gian học based on default selected course
  updateThoiGianHoc();

  // Update thời gian học when course selection changes
  $("#slKhoahoc").change(updateThoiGianHoc);
});
