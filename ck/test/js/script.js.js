/**
 * GFree English Course - Generated JavaScript
 */

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
  var nameValid = true,
    dobValid = true,
    phoneValid = true,
    emailValid = true,
    methodValid = true,
    skillsValid = true;

  // Run validation functions if they exist
  if (typeof checkName === "function") nameValid = checkName();
  if (typeof checkDateOfBirth === "function") dobValid = checkDateOfBirth();
  if (typeof checkPhoneNum === "function") phoneValid = checkPhoneNum();
  if (typeof checkEmail === "function") emailValid = checkEmail();
  if (typeof checkStudyMethod === "function") methodValid = checkStudyMethod();
  if (typeof checkSkills === "function") skillsValid = checkSkills();

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
  if (typeof updateThoiGianHoc === "function") updateThoiGianHoc(); // Update thời gian học after resetting the form

  // Clear error messages
  $("#erName, #erNgaysinh, #erSDT, #erEmail, #erHinhthuc, #erSkills").text("");
}

// Initialize when the document is ready
$(function () {
  $("input[name='hinhthuc']").on("click", checkStudyMethod);
  $("#chkListening, #chkReading, #chkWriting").on("click", checkSkills);
  // Set initial value for thời gian học based on default selected course
  updateThoiGianHoc();

  // Update thời gian học when course selection changes
  $("#slKhoahoc").on("change", updateThoiGianHoc);
});
