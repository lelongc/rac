/**
 * Code generation for exporting the created page
 */

/**
 * Generate HTML code from the canvas
 * @param {boolean} isPreview - Whether generating for preview (includes validation scripts)
 */
function generateHTMLCode(isPreview = false) {
  const pageTitle =
    $("#page-title").val() || "GFree English Course Registration";
  const language = $("#page-language").val() || "en";

  // Clone canvas content for modification
  const canvasContent = $("#canvas").clone();

  // Remove all component controls and classes
  canvasContent.find(".component-actions").remove();
  canvasContent
    .find(".canvas-component")
    .removeClass("canvas-component selected");
  canvasContent.find(".drop-placeholder").remove();

  // Remove modal components from the main container - we'll add them separately
  const modalComponents = canvasContent.find('[data-type="modal"]');
  modalComponents.remove();

  // Begin HTML document
  let html = `<!DOCTYPE html>
<html lang="${language}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${pageTitle}</title>
    <link rel="stylesheet" href="${
      isPreview
        ? "https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css"
        : "../css/bootstrap.min.css"
    }">
    <style>
        * {
            box-sizing: border-box;
            padding: 0;
            margin: 0;
            color: black;
        }

        body {
            font-size: 16px;
            line-height: 1.5;
        }

        #header {
            overflow: hidden;
        }
        
        #footer {
            background-color: #007bff;
            color: white;
            padding: 20px 0;
            margin-top: 20px;
            text-align: center;
        }
        
        #footer p {
            margin: 5px 0;
            color: white;
        }
    </style>
</head>

<body>
    <!-- Main container -->
    <div class="container" style="border: 1px solid black;">`;

  // Process banner and navbar components first
  const headerComponents = canvasContent.find(
    '[data-type="banner"], [data-type="navbar"]'
  );
  if (headerComponents.length) {
    headerComponents.each(function () {
      const component = $(this);
      if (component.data("type") === "banner") {
        html += `
        <!-- Header with banner -->
        <div id="header">
            ${component.find("#header").html()}
        </div>`;
      } else if (component.data("type") === "navbar") {
        html += `
        <!-- Navigation menu -->
        <div id="navbar">
            ${component.find("#navbar").html()}
        </div>`;
      }
    });
  }

  // Add section for table component
  const tableComponent = canvasContent.find('[data-type="table"]');
  if (tableComponent.length) {
    html += `
        <!-- Main content section -->
        <div id="section">
            ${tableComponent.find(".container").prop("outerHTML")}
        </div>`;
  }

  // Add footer component
  const footerComponent = canvasContent.find('[data-type="footer"]');
  if (footerComponent.length) {
    html += `
        <!-- Footer with student information -->
        ${footerComponent.find("#footer").prop("outerHTML")}`;
  }

  // Close main container
  html += `\n    </div>\n`;

  // Add modal components outside the main container
  const hasModal = modalComponents.length > 0;
  if (hasModal) {
    html += generateModalHTML();
  }

  // Add JavaScript libraries and scripts
  html += `
    <!-- JavaScript libraries -->
    <script src="${
      isPreview
        ? "https://code.jquery.com/jquery-3.7.1.min.js"
        : "../js/jquery-3.7.1.min.js"
    }"></script>
    <script src="${
      isPreview
        ? "https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/js/bootstrap.bundle.min.js"
        : "../js/bootstrap.bundle.min.js"
    }"></script>
    ${
      isPreview
        ? `<script>${generateJSCode()}</script>`
        : '<script src="../js/main.js"></script>'
    }
</body>
</html>`;

  return html;
}

/**
 * Generate a modal HTML based on modal settings
 */
function generateModalHTML() {
  // Get the modal component
  const modalComponent = $('#canvas .canvas-component[data-type="modal"]');

  // If there's no modal component, return empty string
  if (!modalComponent.length) return "";

  // Get modal settings
  const modalId = modalComponent.data("modal-id") || "myModal";
  const modalTitle = modalComponent.data("modal-title") || "THÔNG TIN ĐĂNG KÍ";
  const modalSubmit = modalComponent.data("submit-text") || "Đăng kí";
  const modalCancel = modalComponent.data("cancel-text") || "Hủy";
  const modalSize = modalComponent.data("modal-size") || "modal-lg";

  // Get the fields array
  const fields = modalComponent.data("fields") || [];

  // Build modal HTML with Bootstrap 5 structure
  let modalHtml = `
    <!-- Registration modal -->
    <div class="modal fade" id="${modalId}" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
        <div class="modal-dialog ${modalSize}">
            <div class="modal-content">
                <!-- Modal header -->
                <div class="modal-header">
                    <h2 class="modal-title" id="modalLabel">${modalTitle}</h2>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>

                <!-- Modal body with registration form -->
                <div class="modal-body">
                    <div class="form-group">`;

  // Add fields based on configuration
  fields.forEach((field) => {
    const isRequired = field.required ? "required" : "";
    const errorId = `er${field.id.substring(3)}`;

    switch (field.type) {
      case "text-field":
      case "email-field":
        modalHtml += `
                        <!-- ${field.label} -->
                        <div class="row mt-2">
                            <div class="col-3 text-end">
                                <label for="${field.id}" class="fw-normal">${
          field.label
        }</label>
                            </div>
                            <div class="col-9">
                                <input type="${
                                  field.type === "email-field"
                                    ? "email"
                                    : "text"
                                }" 
                                       id="${field.id}" 
                                       class="form-control"
                                       ${isRequired}
                                       ${
                                         field.placeholder
                                           ? `placeholder="${field.placeholder}"`
                                           : ""
                                       }>
                                <span id="${errorId}" class="text-danger small mt-1 d-block"></span>
                            </div>
                        </div>`;
        break;

      case "date-field":
        modalHtml += `
                        <!-- ${field.label} -->
                        <div class="row mt-2">
                            <div class="col-3 text-end">
                                <label for="${field.id}" class="fw-normal">${field.label}</label>
                            </div>
                            <div class="col-9">
                                <input type="date" 
                                       id="${field.id}" 
                                       class="form-control"
                                       ${isRequired}>
                                <span id="${errorId}" class="text-danger small mt-1 d-block"></span>
                            </div>
                        </div>`;
        break;

      case "select":
        modalHtml += `
                        <!-- ${field.label} -->
                        <div class="row mt-2">
                            <div class="col-3 text-end">
                                <label for="${field.id}" class="fw-normal">${field.label}</label>
                            </div>
                            <div class="col-9">
                                <select id="${field.id}" class="form-select" ${isRequired}>`;

        // Add options
        field.options.forEach((option) => {
          modalHtml += `
                                    <option value="${option.value}" data-name="${option.text}">${option.text}</option>`;
        });

        modalHtml += `
                                </select>
                                <span id="${errorId}" class="text-danger small mt-1 d-block"></span>
                            </div>
                        </div>`;
        break;

      case "readonly-field":
        modalHtml += `
                        <!-- ${field.label} -->
                        <div class="row mt-2">
                            <div class="col-3 text-end">
                                <label for="${field.id}" class="fw-normal">${field.label}</label>
                            </div>
                            <div class="col-9">
                                <input type="text" 
                                       id="${field.id}" 
                                       class="form-control" 
                                       readonly>
                            </div>
                        </div>`;
        break;

      case "radio-group":
        modalHtml += `
                        <!-- ${field.label} -->
                        <div class="row mt-2">
                            <div class="col-3 text-end">
                                <label class="fw-normal">${field.label}</label>
                            </div>
                            <div class="col-9">`;

        // Add radio options
        field.options.forEach((option) => {
          modalHtml += `
                                <div class="form-check">
                                    <input class="form-check-input" 
                                           type="radio" 
                                           name="${field.name}" 
                                           id="${option.id}" 
                                           value="${option.value}"
                                           ${option.checked ? "checked" : ""}>
                                    <label class="form-check-label" for="${
                                      option.id
                                    }">${option.text}</label>
                                </div>`;
        });

        modalHtml += `
                                <span id="${errorId}" class="text-danger small mt-1 d-block"></span>
                            </div>
                        </div>`;
        break;

      case "checkbox-group":
        modalHtml += `
                        <!-- ${field.label} -->
                        <div class="row mt-2">
                            <div class="col-3 text-end">
                                <label class="fw-normal">${field.label}</label>
                            </div>
                            <div class="col-9">`;

        // Add checkbox options
        field.options.forEach((option) => {
          modalHtml += `
                                <div class="form-check">
                                    <input class="form-check-input" 
                                           type="checkbox" 
                                           id="${option.id}" 
                                           value="${option.value}">
                                    <label class="form-check-label" for="${option.id}">${option.text}</label>
                                </div>`;
        });

        modalHtml += `
                                <span id="${errorId}" class="text-danger small mt-1 d-block"></span>
                            </div>
                        </div>`;
        break;
    }
  });

  // Close the modal HTML
  modalHtml += `
                    </div>
                </div>

                <!-- Modal footer -->
                <div class="modal-footer d-flex justify-content-end">
                    <button type="button" class="btn btn-success btn-sm me-2" onclick="DangKy()">${modalSubmit}</button>
                    <button type="button" class="btn btn-danger btn-sm" data-bs-dismiss="modal">${modalCancel}</button>
                </div>
            </div>
        </div>
    </div>`;

  return modalHtml;
}

/**
 * Generate JavaScript code for the page
 * Creates all necessary validation functions similar to the sample
 */
function generateJSCode() {
  // Get fields data from modal component
  const modalComponent = $('#canvas .canvas-component[data-type="modal"]');
  const fieldsArray = modalComponent.length
    ? modalComponent.data("fields")
    : [];

  // Create standard validation functions from the template
  let jsCode = `/**
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
  var regex = /^[A-Z][a-z]*(\\s+[A-Z][a-z]*)+$/;
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
  var regex = /^(09|03|08)\\d{8}$/;
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
  var regex = /@.*\\.com$/;
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
  return \`\${day}/\${month}/\${year}\`;
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
  var newRow = \`<tr>
                  <td>\${rowCount}</td>
                  <td>\${name}</td>
                  <td>\${formattedDate}</td>
                  <td>\${sdt}</td>
                  <td>\${email}</td>
                  <td>\${khoahocText}</td>
                  <td>\${hinhthuc}</td>
                  <td>\${skillsString}</td>
                </tr>\`;
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
$(function () {
  // Add real-time validation using .on()
  $("#txtName").on("blur", checkName);
  $("#txtNgaysinh").on("blur", checkDateOfBirth);
  $("#txtSDT").on("blur", checkPhoneNum);
  $("#txtEmail").on("blur", checkEmail);

  // For checkboxes, validate whenever any checkbox is clicked using .on()
  $("#chkListening, #chkReading, #chkWriting").on("click", checkSkills);

  // For radios, validate whenever any radio button is clicked using .on()
  $("input[name='hinhthuc']").on("click", checkStudyMethod);

  // Set initial value for thời gian học based on default selected course
  updateThoiGianHoc();

  // Update thời gian học when course selection changes using .on()
  $("#slKhoahoc").on("change", updateThoiGianHoc);
});`;

  return jsCode;
}

/**
 * Generate CSS code for the page
 */
function generateCSSCode() {
  return `/* Base styles */
* {
    box-sizing: border-box;
    padding: 0;
    margin: 0;
    color: black;
}

body {
    font-size: 16px;
    line-height: 1.5;
}

#header {
    overflow: hidden;
}

/* Additional custom styles can be added here */
.form-check {
    margin-bottom: 5px;
}

.table th {
    background-color: #f8f9fa;
}

@media (max-width: 768px) {
    .col-3.text-right {
        text-align: left !important;
    }
}`;
}
