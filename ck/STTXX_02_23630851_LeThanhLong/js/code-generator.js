/**
 * Code Generator Module for GFree English Course Web Builder
 * Generates complete HTML, CSS, and JavaScript code from the page model
 */

const CodeGenerator = (function () {
  /**
   * Main function to generate code from data model
   * @param {Object} pageModel - The page model manager instance
   * @returns {Object} Object containing HTML, CSS, and JS code as strings
   */
  function generateCode(pageModel = window.pageModelManager) {
    // Get components from the model
    const components = pageModel.getComponents();
    const metadata = pageModel.metadata || { title: "GFree English Course" };

    // Generate the code parts
    const htmlCode = generateHTML(components, metadata);
    const cssCode = generateCSS(components);
    const jsCode = generateJS(components);

    return {
      html: htmlCode,
      css: cssCode,
      js: jsCode,
    };
  }

  /**
   * Generate the complete HTML code
   * @param {Array} components - Array of components
   * @param {Object} metadata - Page metadata
   * @returns {string} Complete HTML code
   */
  function generateHTML(components, metadata) {
    // Start with HTML structure
    let html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${metadata.title || "GFree English Course"}</title>
    <link rel="stylesheet" href="../css/bootstrap.min.css">
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <div class="container" style="border: 1px solid black">
`;

    // Generate HTML for each component
    components.forEach((component) => {
      switch (component.type) {
        case "header":
          html += generateHeaderHTML(component);
          break;
        case "nav":
          html += generateNavHTML(component);
          break;
        case "table":
          html += generateTableHTML(component);
          break;
        case "modal":
          html += generateModalHTML(component);
          break;
        case "footer":
          html += generateFooterHTML(component);
          break;
      }
    });

    // Close main container
    html += `    </div>

    <!-- JavaScript libraries -->
    <script src="../js/jquery-3.7.1.min.js"></script>
    <script src="../js/bootstrap.bundle.min.js"></script>
    <script src="../js/script.js"></script>
</body>
</html>`;

    return html;
  }

  /**
   * Generate HTML for header component
   * @param {Object} component - Header component
   * @returns {string} HTML code
   */
  function generateHeaderHTML(component) {
    return `
    <!-- Header with banner -->
    <div id="header">
        <div class="row" style="width: 100%">
            <img src="${component.logoUrl}" alt="Banner" style="width: 100%; height: auto; display: block">
        </div>
    </div>
`;
  }

  /**
   * Generate HTML for navigation component
   * @param {Object} component - Navigation component
   * @returns {string} HTML code
   */
  function generateNavHTML(component) {
    // Generate nav items HTML from the items array
    const navItems = component.items
      .map(
        (item) =>
          `            <li class="nav-item">
                <a class="nav-link" href="${item.url}">${item.text}</a>
            </li>`
      )
      .join("\n");

    // Add register button if needed, with customized properties
    const registerButton = component.includeRegisterButton
      ? `            <li class="nav-item">
                <button class="btn ${
                  component.registerButtonClass || "btn-danger"
                } ${component.registerButtonSize || "btn-sm"} text-white" 
                        data-bs-toggle="modal" data-bs-target="#myModal">
                    ${component.registerButtonText || "Đăng ký"}
                </button>
            </li>`
      : "";

    return `
    <!-- Navigation menu -->
    <div id="navbar">
        <nav class="navbar navbar-expand-sm navbar-light bg-light">
            <div class="container-fluid">
                <ul class="navbar-nav">
${navItems}
${registerButton}
                </ul>
            </div>
        </nav>
    </div>
`;
  }

  /**
   * Generate HTML for table component
   * @param {Object} component - Table component
   * @returns {string} HTML code
   */
  function generateTableHTML(component) {
    // Generate table header columns
    const tableHeaders = component.columns
      .map((col) => `                <th>${col}</th>`)
      .join("\n");

    return `
    <!-- Main content section -->
    <div id="section">
        <div class="container">
            <!-- Table title -->
            <div class="row my-3">
                <h3>${component.title}</h3>
            </div>

            <!-- Registration table -->
            <table class="table ${
              component.showBorder ? "table-bordered" : ""
            }" id="${component.tableId || "memberList"}">
                <thead class="bg-light">
                    <tr>
${tableHeaders}
                    </tr>
                </thead>
                <tbody>
                    <!-- Registration data will be inserted here -->
                </tbody>
            </table>
        </div>
    </div>
`;
  }

  /**
   * Generate HTML for modal registration component
   * @param {Object} component - Modal component
   * @returns {string} HTML code
   */
  function generateModalHTML(component) {
    // Generate form fields HTML
    let formFieldsHTML = "";

    if (component.formFields && component.formFields.length > 0) {
      component.formFields.forEach((field) => {
        switch (field.type) {
          case "text":
          case "email":
          case "number":
          case "date":
            formFieldsHTML += generateInputFieldHTML(field);
            break;
          case "select":
            formFieldsHTML += generateSelectFieldHTML(field);
            break;
        }
      });
    }

    // Generate radio groups HTML
    if (component.radioGroups && component.radioGroups.length > 0) {
      component.radioGroups.forEach((group) => {
        formFieldsHTML += generateRadioGroupHTML(group);
      });
    }

    // Generate checkbox groups HTML
    if (component.checkboxGroups && component.checkboxGroups.length > 0) {
      component.checkboxGroups.forEach((group) => {
        formFieldsHTML += generateCheckboxGroupHTML(group);
      });
    }

    return `
    <!-- Registration modal -->
    <div class="modal fade" id="${
      component.modalId || "myModal"
    }" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <!-- Modal header -->
                <div class="modal-header">
                    <h2 class="modal-title" id="modalLabel">${
                      component.title
                    }</h2>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>

                <!-- Modal body with registration form -->
                <div class="modal-body">
                    <div class="form-group">
${formFieldsHTML}
                    </div>
                </div>

                <!-- Modal footer -->
                <div class="modal-footer d-flex justify-content-end">
                    <button type="button" class="btn btn-success btn-sm me-2" onclick="DangKy()">
                        ${component.registerBtnText || "Đăng kí"}
                    </button>
                    <button type="button" class="btn btn-danger btn-sm" data-bs-dismiss="modal">
                        ${component.cancelBtnText || "Hủy"}
                    </button>
                </div>
            </div>
        </div>
    </div>
`;
  }

  /**
   * Generate HTML for a standard input field
   * @param {Object} field - Field configuration
   * @returns {string} HTML code
   */
  function generateInputFieldHTML(field) {
    const readonly = field.readonly ? " readonly" : "";
    const placeholder = field.placeholder
      ? ` placeholder="${field.placeholder}"`
      : "";

    return `
                        <!-- ${field.label} -->
                        <div class="row mt-2">
                            <div class="col-3 text-end">
                                <label for="${field.id}" class="fw-normal">${
      field.label
    }</label>
                            </div>
                            <div class="col-9">
                                <input type="${field.type}" id="${
      field.id
    }" class="form-control"${readonly}${placeholder}>
                                <span id="er${field.id.replace(
                                  "txt",
                                  ""
                                )}" class="text-danger small mt-1 d-block"></span>
                            </div>
                        </div>`;
  }

  /**
   * Generate HTML for a select dropdown field
   * @param {Object} field - Field configuration
   * @returns {string} HTML code
   */
  function generateSelectFieldHTML(field) {
    // Generate options
    let optionsHTML = "";
    if (field.options && field.options.length > 0) {
      optionsHTML = field.options
        .map((option) => {
          const dataAttr = option["data-name"]
            ? ` data-name="${option["data-name"]}"`
            : "";
          return `                                <option value="${option.value}"${dataAttr}>${option.text}</option>`;
        })
        .join("\n");
    }

    return `
                        <!-- ${field.label} -->
                        <div class="row mt-2">
                            <div class="col-3 text-end">
                                <label for="${field.id}" class="fw-normal">${field.label}</label>
                            </div>
                            <div class="col-9">
                                <select id="${field.id}" class="form-select">
${optionsHTML}
                                </select>
                            </div>
                        </div>`;
  }

  /**
   * Generate HTML for a radio button group
   * @param {Object} group - Radio group configuration
   * @returns {string} HTML code
   */
  function generateRadioGroupHTML(group) {
    // Generate radio options
    let optionsHTML = "";
    if (group.options && group.options.length > 0) {
      optionsHTML = group.options
        .map((option) => {
          const checked = option.checked ? " checked" : "";
          return `                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="${group.name}" id="${option.id}" value="${option.value}"${checked}>
                                    <label class="form-check-label" for="${option.id}">${option.label}</label>
                                </div>`;
        })
        .join("\n");
    }

    return `
                        <!-- ${group.label} -->
                        <div class="row mt-2">
                            <div class="col-3 text-end">
                                <label for="${group.id}" class="fw-normal">${
      group.label
    }</label>
                            </div>
                            <div class="col-9">
${optionsHTML}
                                <span id="er${group.id.replace(
                                  "radio",
                                  ""
                                )}" class="text-danger small mt-1 d-block"></span>
                            </div>
                        </div>`;
  }

  /**
   * Generate HTML for a checkbox group
   * @param {Object} group - Checkbox group configuration
   * @returns {string} HTML code
   */
  function generateCheckboxGroupHTML(group) {
    // Generate checkbox options
    let optionsHTML = "";
    if (group.options && group.options.length > 0) {
      optionsHTML = group.options
        .map((option) => {
          const checked = option.checked ? " checked" : "";
          return `                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" id="${option.id}" value="${option.value}"${checked}>
                                    <label class="form-check-label" for="${option.id}">${option.label}</label>
                                </div>`;
        })
        .join("\n");
    }

    return `
                        <!-- ${group.label} -->
                        <div class="row mt-2">
                            <div class="col-3 text-end">
                                <label for="${group.id}" class="fw-normal">${group.label}</label>
                            </div>
                            <div class="col-9">
${optionsHTML}
                                <span id="er${group.id}" class="text-danger small mt-1 d-block"></span>
                            </div>
                        </div>`;
  }

  /**
   * Generate HTML for footer component
   * @param {Object} component - Footer component
   * @returns {string} HTML code
   */
  function generateFooterHTML(component) {
    // Get student info
    const studentInfo = component.studentInfo || {
      name: "Lê Thanh Long",
      studentId: "23630851",
      className: "DHKTPM18A",
    };

    return `
    <!-- Footer with student information -->
    <div id="footer">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <h5 class="text-white">Thông tin sinh viên</h5>
                    <p>Họ tên: ${studentInfo.name}</p>
                    <p>Mã sinh viên: ${studentInfo.studentId}</p>
                    <p>Mã lớp: ${studentInfo.className}</p>
                </div>
            </div>
        </div>
    </div>
`;
  }

  /**
   * Generate CSS code based on components
   * @param {Array} components - Array of components
   * @returns {string} CSS code
   */
  function generateCSS(components) {
    // Start with basic styles
    let css = `/* GFree English Course - Generated Styles */

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

`;

    // Add component-specific styles
    components.forEach((component) => {
      if (component.type === "footer") {
        // Get footer styles
        const bgColor = component.styles.backgroundColor || "#0d6efd";
        const textColor = component.styles.color || "white";

        css += `#footer {
    background-color: ${bgColor};
    color: ${textColor};
    padding: 20px 0;
    margin-top: 20px;
    text-align: center;
}

#footer p, #footer h5 {
    margin: 5px 0;
    color: ${textColor};
}

`;
      }
    });

    return css;
  }

  /**
   * Generate JavaScript code based on components
   * @param {Array} components - Array of components
   * @returns {string} JavaScript code
   */
  function generateJS(components) {
    // Find the modal component if it exists
    const modalComponent = components.find((c) => c.type === "modal");

    // If no modal component, return minimal JS
    if (!modalComponent) {
      return `// GFree English Course - Generated JavaScript

// Document ready function
$(function() {
    // Add your custom JavaScript here
});`;
    }

    // Get the form fields
    const formFields = modalComponent.formFields || [];
    const radioGroups = modalComponent.radioGroups || [];
    const checkboxGroups = modalComponent.checkboxGroups || [];

    // Generate validation functions based on field types
    let validationFunctions = "";
    let eventBindings = "";

    // Check if we have a name field to add validation
    const nameField = formFields.find((f) => f.id === "txtName");
    if (nameField) {
      validationFunctions += generateNameValidationFunction();
      eventBindings += `  $("#txtName").on("blur", checkName);\n`;
    }

    // Check if we have a date of birth field to add validation
    const dobField = formFields.find((f) => f.id === "txtNgaysinh");
    if (dobField) {
      validationFunctions += generateDobValidationFunction();
      eventBindings += `  $("#txtNgaysinh").on("blur", checkDateOfBirth);\n`;
    }

    // Check if we have a phone field to add validation
    const phoneField = formFields.find((f) => f.id === "txtSDT");
    if (phoneField) {
      validationFunctions += generatePhoneValidationFunction();
      eventBindings += `  $("#txtSDT").on("blur", checkPhoneNum);\n`;
    }

    // Check if we have an email field to add validation
    const emailField = formFields.find((f) => f.id === "txtEmail");
    if (emailField) {
      validationFunctions += generateEmailValidationFunction();
      eventBindings += `  $("#txtEmail").on("blur", checkEmail);\n`;
    }

    // Check if we have radio groups to add validation
    if (radioGroups.length > 0) {
      // We'll assume the first radio group is for study method
      validationFunctions += generateStudyMethodValidationFunction();
      eventBindings += `  $("input[name='${radioGroups[0].name}']").on("click", checkStudyMethod);\n`;
    }

    // Check if we have checkbox groups to add validation
    if (checkboxGroups.length > 0) {
      // We'll assume the first checkbox group is for skills
      validationFunctions += generateSkillsValidationFunction();

      // Get checkbox IDs for event binding
      const checkboxIds = checkboxGroups[0].options
        .map((o) => `#${o.id}`)
        .join(", ");
      eventBindings += `  $("${checkboxIds}").on("click", checkSkills);\n`;
    }

    // Check if we need the update time function
    const courseField = formFields.find((f) => f.id === "slKhoahoc");
    const timeField = formFields.find((f) => f.id === "txtThoiGianHoc");
    if (courseField && timeField) {
      validationFunctions += generateUpdateThoiGianHocFunction();
      eventBindings += `  // Set initial value for thời gian học based on default selected course\n`;
      eventBindings += `  updateThoiGianHoc();\n\n`;
      eventBindings += `  // Update thời gian học when course selection changes\n`;
      eventBindings += `  $("#slKhoahoc").on("change", updateThoiGianHoc);\n`;
    }

    // Generate the complete JavaScript code
    const js = `/**
 * GFree English Course - Generated JavaScript
 */

${validationFunctions}
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
  var nameValid = true, dobValid = true, phoneValid = true, 
      emailValid = true, methodValid = true, skillsValid = true;
  
  // Run validation functions if they exist
  if (typeof checkName === 'function') nameValid = checkName();
  if (typeof checkDateOfBirth === 'function') dobValid = checkDateOfBirth();
  if (typeof checkPhoneNum === 'function') phoneValid = checkPhoneNum();
  if (typeof checkEmail === 'function') emailValid = checkEmail();
  if (typeof checkStudyMethod === 'function') methodValid = checkStudyMethod();
  if (typeof checkSkills === 'function') skillsValid = checkSkills();

  // Only proceed if all validations pass
  if (!nameValid || !dobValid || !phoneValid || !emailValid || !methodValid || !skillsValid) {
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
  if (typeof updateThoiGianHoc === 'function') updateThoiGianHoc(); // Update thời gian học after resetting the form

  // Clear error messages
  $("#erName, #erNgaysinh, #erSDT, #erEmail, #erHinhthuc, #erSkills").text("");
}

// Initialize when the document is ready
$(function() {
${eventBindings}
});`;

    return js;
  }

  /**
   * Generate name validation function
   * @returns {string} JavaScript function
   */
  function generateNameValidationFunction() {
    return `/**
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

`;
  }

  /**
   * Generate date of birth validation function
   * @returns {string} JavaScript function
   */
  function generateDobValidationFunction() {
    return `/**
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

`;
  }

  /**
   * Generate phone validation function
   * @returns {string} JavaScript function
   */
  function generatePhoneValidationFunction() {
    return `/**
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

`;
  }

  /**
   * Generate email validation function
   * @returns {string} JavaScript function
   */
  function generateEmailValidationFunction() {
    return `/**
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

`;
  }

  /**
   * Generate study method validation function
   * @returns {string} JavaScript function
   */
  function generateStudyMethodValidationFunction() {
    return `/**
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

`;
  }

  /**
   * Generate skills validation function
   * @returns {string} JavaScript function
   */
  function generateSkillsValidationFunction() {
    return `/**
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

`;
  }

  /**
   * Generate update time function
   * @returns {string} JavaScript function
   */
  function generateUpdateThoiGianHocFunction() {
    return `/**
 * Update the study duration field based on selected course
 */
function updateThoiGianHoc() {
  var selectedCourse = $("#slKhoahoc option:selected");
  var duration = selectedCourse.val();

  // Update the thời gian học textbox
  $("#txtThoiGianHoc").val(duration + " tháng");
}

`;
  }

  /**
   * Show the generated code in a modal
   */
  function showGeneratedCode() {
    const codeFiles = generateCode();

    // Create or get modal
    let codeModal = document.getElementById("code-preview-modal");
    if (!codeModal) {
      codeModal = document.createElement("div");
      codeModal.id = "code-preview-modal";
      codeModal.className = "modal fade";
      codeModal.tabIndex = -1;
      codeModal.innerHTML = `
                <div class="modal-dialog modal-xl">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">Generated Code</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body p-0">
                            <nav>
                                <div class="nav nav-tabs" id="code-tab" role="tablist">
                                    <button class="nav-link active" id="html-tab" data-bs-toggle="tab" data-bs-target="#html" type="button" role="tab" aria-controls="html" aria-selected="true">HTML</button>
                                    <button class="nav-link" id="css-tab" data-bs-toggle="tab" data-bs-target="#css" type="button" role="tab" aria-controls="css" aria-selected="false">CSS</button>
                                    <button class="nav-link" id="js-tab" data-bs-toggle="tab" data-bs-target="#js" type="button" role="tab" aria-controls="js" aria-selected="false">JavaScript</button>
                                </div>
                            </nav>
                            <div class="tab-content" id="code-tab-content">
                                <div class="tab-pane fade show active" id="html" role="tabpanel" aria-labelledby="html-tab">
                                    <pre class="m-0 p-3"><code id="html-code"></code></pre>
                                </div>
                                <div class="tab-pane fade" id="css" role="tabpanel" aria-labelledby="css-tab">
                                    <pre class="m-0 p-3"><code id="css-code"></code></pre>
                                </div>
                                <div class="tab-pane fade" id="js" role="tabpanel" aria-labelledby="js-tab">
                                    <pre class="m-0 p-3"><code id="js-code"></code></pre>
                                </div>
                            </div>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-primary" id="download-code-btn">Download Files</button>
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        </div>
                    </div>
                </div>
            `;
      document.body.appendChild(codeModal);

      // Add event listener for download button
      document
        .getElementById("download-code-btn")
        .addEventListener("click", function () {
          downloadGeneratedFiles(codeFiles);
        });
    }

    // Update code content
    document.getElementById("html-code").textContent = codeFiles.html;
    document.getElementById("css-code").textContent = codeFiles.css;
    document.getElementById("js-code").textContent = codeFiles.js;

    // Show the modal
    const modal = new bootstrap.Modal(codeModal);
    modal.show();
  }

  /**
   * Generate downloadable files
   * @param {Object} codeFiles - Object containing HTML, CSS, and JS code
   */
  function downloadGeneratedFiles(codeFiles) {
    // Create a ZIP file using JSZip (this would require the JSZip library)
    if (typeof JSZip !== "undefined") {
      const zip = new JSZip();

      // Add files to the ZIP
      zip.file("index.html", codeFiles.html);

      // Create css folder
      const cssFolder = zip.folder("css");
      cssFolder.file("style.css", codeFiles.css);

      // Create js folder
      const jsFolder = zip.folder("js");
      jsFolder.file("script.js", codeFiles.js);

      // Generate the ZIP file
      zip.generateAsync({ type: "blob" }).then(function (content) {
        // Create download link
        const link = document.createElement("a");
        link.href = URL.createObjectURL(content);
        link.download = "GFreeEnglishCourse.zip";
        link.click();
      });
    } else {
      // If JSZip is not available, offer individual file downloads
      downloadSingleFile(codeFiles.html, "index.html");
      downloadSingleFile(codeFiles.css, "style.css");
      downloadSingleFile(codeFiles.js, "script.js");
    }
  }

  /**
   * Download a single file
   * @param {string} content - File content
   * @param {string} filename - File name
   */
  function downloadSingleFile(content, filename) {
    const blob = new Blob([content], { type: "text/plain;charset=utf-8" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = filename;
    link.click();
  }

  // Return public API
  return {
    generateCode,
    showGeneratedCode,
  };
})();

// Set up preview button when document is ready
document.addEventListener("DOMContentLoaded", function () {
  // Find the preview button and attach event listener
  const previewBtn = document.querySelector("button:has(.bi-play-fill)");
  if (previewBtn) {
    previewBtn.addEventListener("click", CodeGenerator.showGeneratedCode);
  }

  // Find the save button and attach event listener if needed
  const saveBtn = document.querySelector("button:has(.bi-save)");
  if (saveBtn) {
    saveBtn.addEventListener("click", function () {
      // First save the current model
      const modelJson = window.pageModelManager.saveModel(true);
      localStorage.setItem("gfree-builder-model", modelJson);

      // Then show the generated code
      CodeGenerator.showGeneratedCode();
    });
  }
});
