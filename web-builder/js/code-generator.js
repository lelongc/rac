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
        <div class="modal fade" id="${modalId}">
            <div class="modal-dialog ${modalSize}">
                <div class="modal-content">
                    <!-- Modal header -->
                    <div class="modal-header">
                        <h2>${modalTitle}</h2>
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
                                <div class="col-3 text-right">
                                    <label for="${
                                      field.id
                                    }" class="font-weight-normal">${
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
                                <div class="col-3 text-right">
                                    <label for="${field.id}" class="font-weight-normal">${field.label}</label>
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
                                <div class="col-3 text-right">
                                    <label for="${field.id}" class="font-weight-normal">${field.label}</label>
                                </div>
                                <div class="col-9">
                                    <select id="${field.id}" class="form-control" ${isRequired}>`;

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
                                <div class="col-3 text-right">
                                    <label for="${field.id}" class="font-weight-normal">${field.label}</label>
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
                                <div class="col-3 text-right">
                                    <label class="font-weight-normal">${field.label}</label>
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
                                               ${
                                                 option.checked ? "checked" : ""
                                               }>
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
                                <div class="col-3 text-right">
                                    <label class="font-weight-normal">${field.label}</label>
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
                        <button type="button" class="btn btn-success btn-sm mr-2" onclick="DangKy()">${modalSubmit}</button>
                        <button type="button" class="btn btn-danger btn-sm" data-bs-dismiss="modal">${modalCancel}</button>
                    </div>
                </div>
            </div>
        </div>`;

  return modalHtml;
}

/**
 * Generate JavaScript code for the page
 * Updates needed for custom modal fields
 */
function generateJSCode() {
  // Get fields data from modal component
  const modalComponent = $('#canvas .canvas-component[data-type="modal"]');
  const fieldsArray = modalComponent.length
    ? modalComponent.data("fields")
    : [];

  let jsCode = "";

  // Helper function to check if a field exists
  const hasField = (identifier) => {
    return fieldsArray.some(
      (field) => field.id === identifier || field.type === identifier
    );
  };

  // Generate validation functions for each field type
  fieldsArray.forEach((field) => {
    if (field.validation) {
      let validationCode = `\n/**\n * Validate the ${field.label} field\n */\n`;
      validationCode += `function ${field.validation.function}() {\n`;
      validationCode += `    var value = $("#${field.id}").val();\n\n`;

      // Add empty check if required
      if (field.required) {
        validationCode += `    // Check if empty\n`;
        validationCode += `    if (value.trim() === "") {\n`;
        validationCode += `        $("#er${field.id.substring(3)}").text("${
          field.label
        } không được để trống");\n`;
        validationCode += `        return false;\n`;
        validationCode += `    }\n\n`;
      }

      // Add regex validation if specified
      if (field.validation.regex) {
        validationCode += `    // Check format using regex\n`;
        validationCode += `    var regex = ${field.validation.regex};\n`;
        validationCode += `    if (!regex.test(value)) {\n`;
        validationCode += `        $("#er${field.id.substring(3)}").text("${
          field.validation.message
        }");\n`;
        validationCode += `        return false;\n`;
        validationCode += `    }\n\n`;
      }

      // Special case for date of birth
      if (field.type === "date-field") {
        validationCode += `    // Check if date is in the past\n`;
        validationCode += `    var today = new Date();\n`;
        validationCode += `    var inputDate = new Date(value);\n`;
        validationCode += `    if (inputDate >= today) {\n`;
        validationCode += `        $("#er${field.id.substring(3)}").text("${
          field.label
        } phải là ngày trong quá khứ");\n`;
        validationCode += `        return false;\n`;
        validationCode += `    }\n\n`;
      }

      validationCode += `    $("#er${field.id.substring(3)}").text("");\n`;
      validationCode += `    return true;\n`;
      validationCode += `}\n`;

      jsCode += validationCode;
    }
  });

  // Add helper functions
  jsCode += `
/**
 * Format date from yyyy-mm-dd to dd/mm/yyyy
 */
function formatDate(dateString) {
    if (!dateString) return '';
    const date = new Date(dateString);
    const day = date.getDate().toString().padStart(2, '0');
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const year = date.getFullYear();
    return \`\${day}/\${month}/\${year}\`;
}

/**
 * Update course duration based on selection
 */
function updateThoiGianHoc() {
    var selectedCourse = $("#slKhoahoc option:selected");
    var duration = selectedCourse.val();
    $("#txtThoiGianHoc").val(duration + " tháng");
}
`;

  // Generate DangKy function
  jsCode += `
/**
 * Register function - validates and adds data to table
 */
function DangKy() {
    // Run all validations first
    var isValid = true;
`;

  // Add validation checks
  fieldsArray.forEach((field) => {
    if (field.validation) {
      jsCode += `    isValid = ${field.validation.function}() && isValid;\n`;
    }
  });

  jsCode += `
    // Stop if any validation failed
    if (!isValid) return;

    // Collect form data
    var data = {
`;

  // Add data collection for each field
  fieldsArray.forEach((field) => {
    switch (field.type) {
      case "checkbox-group":
        jsCode += `        skills: $('input[type="checkbox"]:checked').map(function() {\n`;
        jsCode += `            return $(this).val();\n`;
        jsCode += `        }).get().join(', '),\n`;
        break;
      case "radio-group":
        jsCode += `        hinhthuc: $('input[name="${field.name}"]:checked').val(),\n`;
        break;
      case "select":
        jsCode += `        ${field.id.substring(2).toLowerCase()}: $('#${
          field.id
        } option:selected').text(),\n`;
        break;
      case "date-field":
        jsCode += `        ${field.id
          .substring(3)
          .toLowerCase()}: formatDate($('#${field.id}').val()),\n`;
        break;
      default:
        jsCode += `        ${field.id.substring(3).toLowerCase()}: $('#${
          field.id
        }').val(),\n`;
    }
  });

  jsCode += `    };\n\n`;

  // Generate table row HTML
  jsCode += `    // Add new row to table
    var rowCount = $('#memberList tbody tr').length + 1;
    var newRow = '<tr><td>' + rowCount + '</td>';
`;

  // Add cell for each field in correct order
  const fieldOrder = [
    "name",
    "ngaysinh",
    "sdt",
    "email",
    "khoahoc",
    "hinhthuc",
    "skills",
  ];
  fieldOrder.forEach((field) => {
    jsCode += `    newRow += '<td>' + (data.${field} || '') + '</td>';\n`;
  });

  jsCode += `    newRow += '</tr>';\n\n`;

  // Complete the function
  jsCode += `    // Add row and close modal
    $('#memberList tbody').append(newRow);
    bootstrap.Modal.getInstance(document.getElementById('myModal')).hide();

    // Reset form
    $('#myModal input[type="text"], #myModal input[type="email"], #myModal input[type="date"]').val('');
    $('#myModal input[type="checkbox"]').prop('checked', false);
    $('#radioCenter').prop('checked', true);
    $('#slKhoahoc').val('3');
    updateThoiGianHoc();

    // Clear validation messages
    $('.text-danger').text('');
}

// Document ready handler
$(document).ready(function() {
    // Add blur validation handlers
`;

  // Add validation handlers
  fieldsArray.forEach((field) => {
    if (field.validation) {
      jsCode += `    $('#${field.id}').blur(${field.validation.function});\n`;
    }
  });

  // Add special handlers
  jsCode += `
    // Checkbox validation
    $('input[type="checkbox"]').click(checkSkills);
    
    // Radio validation
    $('input[name="hinhthuc"]').click(checkStudyMethod);
    
    // Course duration update
    updateThoiGianHoc();
    $('#slKhoahoc').change(updateThoiGianHoc);
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
