/**
 * Web Builder Application
 * Creates customizable forms with validation and table updates
 */

// Store all form fields
let formFields = [];
let selectedFieldIndex = -1;
let commonRegexPatterns = {
  name: "^[A-Z][a-z]*(s+[A-Z][a-z]*)+$", // Mỗi từ bắt đầu bằng chữ hoa
  phone: "^(09|03|08)\\d{8}$", // 10 số bắt đầu với 09, 03, 08
  phoneFormatted: "^0\\d{3}\\.\\d{3}\\.\\d{3}$", // Định dạng 0XXX.XXX.XXX
  email: "@.*\\.com$", // Chứa @ và kết thúc với .com
  emailDetail: "^[a-zA-Z0-9_]{3,}@gmail\\.com$", // name_email@gmail.com
  address: "^[A-Za-z0-9\\/]+$", // Chỉ cho phép chữ, số và dấu /
  nameUppercase: "^[A-ZÀ-Ỹ][a-zà-ỹ]+$", // Từ viết hoa chữ đầu
};

// Initialize application when the document is ready
$(document).ready(function () {
  // Handle template selection
  $(".select-template").on("click", function () {
    const templateName = $(this).data("template");
    loadTemplate(templateName);
  });

  // Handle start from scratch
  $("#startFromScratch").on("click", function () {
    // Hide template selection and show builder interface
    $(".template-card").removeClass("selected");
    showBuilderInterface();
  });

  // Set up field type change handler
  $("#fieldType").on("change", function () {
    const fieldType = $(this).val();
    if (fieldType === "radio" || fieldType === "checkbox") {
      $("#optionsContainer").removeClass("d-none");
    } else {
      $("#optionsContainer").addClass("d-none");
    }
  });

  // Handle adding options for radio/checkbox
  $("#optionsContainer button").on("click", function () {
    const optionValue = $(this).siblings("input").eq(0).val().trim();
    const optionLabel = $(this).siblings("input").eq(1).val().trim();

    if (optionValue && optionLabel) {
      const optionItem = $(`
                <div class="option-item">
                    <span class="me-2">${optionLabel} (${optionValue})</span>
                    <button type="button" class="btn btn-sm btn-outline-danger btn-remove-option">✕</button>
                </div>
            `);

      $("#optionsList").append(optionItem);
      $(this).siblings("input").val("");
    }
  });

  // Handle removing options
  $("#optionsList").on("click", ".btn-remove-option", function () {
    $(this).parent().remove();
  });

  // Populate regex dropdown with common patterns
  populateRegexPatterns();

  // Add field to the form builder
  $("#addField").on("click", addFieldToBuilder);

  // Select a field when clicked
  $("#formBuilder").on("click", ".form-field", function () {
    $(".form-field").removeClass("selected");
    $(this).addClass("selected");
    selectedFieldIndex = $(this).data("field-index");
  });

  // Handle field movement
  $("#moveFieldUp").on("click", moveFieldUp);
  $("#moveFieldDown").on("click", moveFieldDown);
  $("#removeField").on("click", removeSelectedField);

  // Handle submit button addition
  $("#addSubmitButton").on("click", addSubmitButton);

  // Apply visual changes
  $("#applyChanges").on("click", applyStyleChanges);

  // Generate and show code
  $("#generateCode").on("click", generateAndShowCode);

  // Preview website
  $("#previewWebsite").on("click", previewWebsite);
});

// Load a template
function loadTemplate(templateName) {
  if (templates[templateName]) {
    const template = templates[templateName];

    // Update form fields based on template
    formFields = [];

    // Add template styling
    $("#websiteTitle").val(template.title);
    $("#headerBgColor").val(template.headerBgColor);
    $("#headerTextColor").val(template.headerTextColor);
    $("#formBgColor").val(template.formBgColor);
    $("#formBorderColor").val(template.formBorderColor);
    $("#footerBgColor").val(template.footerBgColor);
    $("#footerTextColor").val(template.footerTextColor);
    $("#footerText").val(template.footerText);

    // Apply template styling
    window.webConfig = {
      websiteTitle: template.title,
      headerBgColor: template.headerBgColor,
      headerTextColor: template.headerTextColor,
      formBgColor: template.formBgColor,
      formBorderColor: template.formBorderColor,
      footerBgColor: template.footerBgColor,
      footerTextColor: template.footerTextColor,
      footerText: template.footerText,
    };

    // Add template fields
    template.fields.forEach((field) => {
      formFields.push(field);
    });

    // Highlight selected template
    $(".template-card").removeClass("selected");
    $(`.template-card[data-template="${templateName}"]`).addClass("selected");

    // Update table headers if provided
    if (template.tableHeaders && template.tableHeaders.length > 0) {
      // Store the headers for later use
      window.customTableHeaders = template.tableHeaders;
    }

    // Show the builder interface
    showBuilderInterface();

    // Refresh the form builder
    refreshFormBuilder();
  }
}

// Show builder interface after template selection
function showBuilderInterface() {
  $(".row:first").hide();
  $("#builder-interface").show();
}

// Populate dropdown with regex patterns
function populateRegexPatterns() {
  // Create a datalist for regex patterns
  const datalist = $("<datalist id='regexPatterns'></datalist>");

  // Add common patterns
  for (const [key, value] of Object.entries(commonRegexPatterns)) {
    datalist.append(`<option value="${value}">${key}</option>`);
  }

  // Append datalist to the page
  $("body").append(datalist);

  // Link the input to the datalist
  $("#validationRegex").attr("list", "regexPatterns");
}

// Add a new field to the form builder
function addFieldToBuilder() {
  const fieldType = $("#fieldType").val();
  const fieldLabel = $("#fieldLabel").val().trim();
  const fieldName = $("#fieldName").val().trim();
  const fieldPlaceholder = $("#fieldPlaceholder").val().trim();
  const validationRegex = $("#validationRegex").val().trim();
  const errorMessage = $("#errorMessage").val().trim();
  const isRequired = $("#requiredField").prop("checked");

  if (!fieldLabel || !fieldName) {
    alert("Vui lòng nhập nhãn và ID cho trường!");
    return;
  }

  // Get options for radio/checkbox
  let options = [];
  if (fieldType === "radio" || fieldType === "checkbox") {
    $("#optionsList .option-item").each(function () {
      const text = $(this).find("span").text();
      const value = text.match(/\((.*?)\)$/)[1];
      const label = text.replace(/ \((.*?)\)$/, "");
      options.push({ value, label });
    });

    if (options.length === 0) {
      alert("Vui lòng thêm ít nhất một tùy chọn!");
      return;
    }
  }

  const newField = {
    type: fieldType,
    label: fieldLabel,
    name: fieldName,
    placeholder: fieldPlaceholder,
    regex: validationRegex,
    errorMessage: errorMessage || "Dữ liệu không hợp lệ!",
    required: isRequired,
    options: options,
  };

  // Add to fields array
  formFields.push(newField);

  // Update the form display
  renderFormField(newField, formFields.length - 1);

  // Update table headers
  updateTableHeaders();

  // Clear the form
  $(
    "#fieldLabel, #fieldName, #fieldPlaceholder, #validationRegex, #errorMessage"
  ).val("");
  $("#requiredField").prop("checked", false);
  $("#optionsList").empty();
  $("#optionsContainer").addClass("d-none");
  $("#fieldType").val("text");

  // Generate code
  generateCode();
}

// Render a single form field
function renderFormField(field, index) {
  let fieldHTML = "";

  // Create the field container
  fieldHTML = `<div class="form-field" data-field-index="${index}">`;

  // Add label
  fieldHTML += `<label for="${field.name}" class="form-label">${field.label}${
    field.required ? ' <span class="text-danger">*</span>' : ""
  }</label>`;

  // Add the input based on type
  if (
    field.type === "text" ||
    field.type === "email" ||
    field.type === "tel" ||
    field.type === "date" ||
    field.type === "file"
  ) {
    fieldHTML += `
            <input type="${field.type}" class="form-control" id="${
      field.name
    }" name="${field.name}" 
                   placeholder="${field.placeholder}" ${
      field.required ? "required" : ""
    }>
            <div class="invalid-feedback">${field.errorMessage}</div>
        `;
  } else if (field.type === "select") {
    fieldHTML += `<select class="form-select" id="${field.name}" name="${
      field.name
    }" ${field.required ? "required" : ""}>`;
    field.options.forEach((option) => {
      fieldHTML += `<option value="${option.value}">${option.label}</option>`;
    });
    fieldHTML += `</select>
            <div class="invalid-feedback">${field.errorMessage}</div>
        `;
  } else if (field.type === "radio") {
    field.options.forEach((option) => {
      fieldHTML += `
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="${
                      field.name
                    }" 
                           id="${field.name}_${option.value}" value="${
        option.value
      }" ${field.required ? "required" : ""}>
                    <label class="form-check-label" for="${field.name}_${
        option.value
      }">${option.label}</label>
                </div>
            `;
    });
    fieldHTML += `<div class="invalid-feedback">${field.errorMessage}</div>`;
  } else if (field.type === "checkbox") {
    field.options.forEach((option) => {
      fieldHTML += `
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" name="${field.name}[]" 
                           id="${field.name}_${option.value}" value="${option.value}">
                    <label class="form-check-label" for="${field.name}_${option.value}">${option.label}</label>
                </div>
            `;
    });
    fieldHTML += `<div class="invalid-feedback">${field.errorMessage}</div>`;
  }

  fieldHTML += `</div>`;

  // Append to the form builder
  $("#formBuilder").append(fieldHTML);
}

// Update table headers based on form fields
function updateTableHeaders() {
  // Start with STT header
  $("#tableHeader").empty().append("<th>STT</th>");

  // Use custom headers if provided, otherwise generate from form fields
  if (window.customTableHeaders && window.customTableHeaders.length > 0) {
    // Skip the first entry if it's "STT" since we already added it
    const startIndex = window.customTableHeaders[0] === "STT" ? 1 : 0;
    for (let i = startIndex; i < window.customTableHeaders.length; i++) {
      $("#tableHeader").append(`<th>${window.customTableHeaders[i]}</th>`);
    }
  } else {
    formFields.forEach((field) => {
      $("#tableHeader").append(`<th>${field.label}</th>`);
    });
  }
}

// Move the selected field up
function moveFieldUp() {
  if (selectedFieldIndex > 0) {
    const temp = formFields[selectedFieldIndex];
    formFields[selectedFieldIndex] = formFields[selectedFieldIndex - 1];
    formFields[selectedFieldIndex - 1] = temp;

    refreshFormBuilder();
    selectedFieldIndex--;
    $(".form-field").eq(selectedFieldIndex).addClass("selected");
  }
}

// Move the selected field down
function moveFieldDown() {
  if (selectedFieldIndex >= 0 && selectedFieldIndex < formFields.length - 1) {
    const temp = formFields[selectedFieldIndex];
    formFields[selectedFieldIndex] = formFields[selectedFieldIndex + 1];
    formFields[selectedFieldIndex + 1] = temp;

    refreshFormBuilder();
    selectedFieldIndex++;
    $(".form-field").eq(selectedFieldIndex).addClass("selected");
  }
}

// Remove the selected field
function removeSelectedField() {
  if (selectedFieldIndex >= 0) {
    formFields.splice(selectedFieldIndex, 1);
    refreshFormBuilder();
    selectedFieldIndex = -1;
  }
}

// Refresh the entire form builder
function refreshFormBuilder() {
  $("#formBuilder").empty();
  formFields.forEach((field, index) => {
    renderFormField(field, index);
  });
  updateTableHeaders();
  generateCode();
}

// Add a submit button to the form
function addSubmitButton() {
  // Check if a submit button already exists
  if ($("#formBuilder button[type='submit']").length > 0) {
    return;
  }

  const submitButton = `
        <div class="form-field" data-field-index="submit">
            <button type="submit" class="btn btn-primary">Gửi</button>
        </div>
    `;

  $("#formBuilder").append(submitButton);
  generateCode();
}

// Apply style changes from the configuration form
function applyStyleChanges() {
  // Get values
  const websiteTitle = $("#websiteTitle").val();
  const headerBgColor = $("#headerBgColor").val();
  const headerTextColor = $("#headerTextColor").val();
  const formBgColor = $("#formBgColor").val();
  const formBorderColor = $("#formBorderColor").val();
  const footerBgColor = $("#footerBgColor").val();
  const footerTextColor = $("#footerTextColor").val();

  // Store in a global config object
  window.webConfig = {
    websiteTitle,
    headerBgColor,
    headerTextColor,
    formBgColor,
    formBorderColor,
    footerBgColor,
    footerTextColor,
    footerText: $("#footerText").val(),
  };

  // Generate updated code
  generateCode();
}

// Generate HTML, CSS, and JavaScript code
function generateCode() {
  const config = window.webConfig || {
    websiteTitle: "Website Builder",
    headerBgColor: "#0d6efd",
    headerTextColor: "#ffffff",
    formBgColor: "#ffffff",
    formBorderColor: "#000000",
    footerBgColor: "#0d6efd",
    footerTextColor: "#ffffff",
    footerText: "MSSV: 23630851 | Họ tên: Lê Thành Long",
  };

  // Generate HTML
  const htmlCode = generateHTML(config);
  $("#htmlCode").text(htmlCode);

  // Generate CSS
  const cssCode = generateCSS(config);
  $("#cssCode").text(cssCode);

  // Generate JavaScript
  const jsCode = generateJavaScript();
  $("#jsCode").text(jsCode);
}

// Generate the HTML code
function generateHTML(config) {
  let formFieldsHTML = "";
  formFields.forEach((field) => {
    formFieldsHTML += generateFieldHTML(field);
  });

  const submitButtonHTML = `
    <div class="row mt-3">
        <div class="col-12">
            <button type="submit" class="btn btn-primary">Gửi</button>
        </div>
    </div>`;

  return `<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${config.websiteTitle}</title>
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="container" id="main-container">
        <!-- Header -->
        <header id="header">
            <h1>${config.websiteTitle}</h1>
        </header>
        
        <!-- Main content -->
        <div class="row" id="content">
            <div class="col-md-6">
                <!-- Form -->
                <div id="form-container">
                    <h3>Đăng ký thông tin</h3>
                    <form id="registrationForm">
                        ${formFieldsHTML}
                        ${submitButtonHTML}
                    </form>
                </div>
            </div>
            
            <div class="col-md-6">
                <!-- Table -->
                <div id="table-container">
                    <h3>Danh sách đăng ký</h3>
                    <table class="table table-bordered" id="dataTable">
                        <thead>
                            <tr>
                                <th>STT</th>
                                ${formFields
                                  .map((field) => `<th>${field.label}</th>`)
                                  .join("")}
                            </tr>
                        </thead>
                        <tbody>
                            <!-- Data will be added here -->
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        
        <!-- Footer -->
        <footer id="footer">
            <p>${config.footerText}</p>
        </footer>
    </div>

    <script src="js/jquery-3.7.1.min.js"></script>
    <script src="js/bootstrap.bundle.min.js"></script>
    <script src="js/script.js"></script>
</body>
</html>`;
}

// Generate a single field's HTML
function generateFieldHTML(field) {
  let html = `<div class="mb-3 row">
    <label for="${field.name}" class="col-sm-4 col-form-label">${field.label}${
    field.required ? ' <span class="text-danger">*</span>' : ""
  }</label>
    <div class="col-sm-8">`;

  if (
    field.type === "text" ||
    field.type === "email" ||
    field.type === "tel" ||
    field.type === "date"
  ) {
    html += `
        <input type="${field.type}" class="form-control" id="${
      field.name
    }" name="${field.name}" 
               placeholder="${field.placeholder}" ${
      field.required ? "required" : ""
    }>
        <div class="invalid-feedback">${field.errorMessage}</div>`;
  } else if (field.type === "radio") {
    field.options.forEach((option) => {
      html += `
        <div class="form-check">
            <input class="form-check-input" type="radio" name="${field.name}" 
                   id="${field.name}_${option.value}" value="${option.value}" ${
        field.required ? "required" : ""
      }>
            <label class="form-check-label" for="${field.name}_${
        option.value
      }">${option.label}</label>
        </div>`;
    });
    html += `<div class="invalid-feedback">${field.errorMessage}</div>`;
  } else if (field.type === "checkbox") {
    field.options.forEach((option) => {
      html += `
        <div class="form-check">
            <input class="form-check-input" type="checkbox" name="${field.name}[]" 
                   id="${field.name}_${option.value}" value="${option.value}">
            <label class="form-check-label" for="${field.name}_${option.value}">${option.label}</label>
        </div>`;
    });
    html += `<div class="invalid-feedback">${field.errorMessage}</div>`;
  }

  html += `
    </div>
</div>`;

  return html;
}

// Generate the CSS code
function generateCSS(config) {
  return `body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 0;
}

#main-container {
    border: 2px solid ${config.formBorderColor};
    margin-top: 20px;
    margin-bottom: 20px;
    background-color: ${config.formBgColor};
}

#header {
    background-color: ${config.headerBgColor};
    color: ${config.headerTextColor};
    padding: 20px;
    text-align: center;
    margin-bottom: 20px;
}

#content {
    padding: 0 20px;
}

#footer {
    background-color: ${config.footerBgColor};
    color: ${config.footerTextColor};
    text-align: center;
    padding: 15px 0;
    margin-top: 20px;
}

.text-danger {
    color: #dc3545;
}

/* Table styles */
#dataTable {
    width: 100%;
    margin-top: 20px;
}

#dataTable th {
    background-color: #f8f9fa;
}

/* Form validation */
.form-control.is-invalid {
    border-color: #dc3545;
    padding-right: calc(1.5em + 0.75rem);
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12' width='12' height='12' fill='none' stroke='%23dc3545'%3e%3ccircle cx='6' cy='6' r='4.5'/%3e%3cpath stroke-linejoin='round' d='M5.8 3.6h.4L6 6.5z'/%3e%3ccircle cx='6' cy='8.2' r='.6' fill='%23dc3545' stroke='none'/%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right calc(0.375em + 0.1875rem) center;
    background-size: calc(0.75em + 0.375rem) calc(0.75em + 0.375rem);
}

.invalid-feedback {
    display: none;
    width: 100%;
    margin-top: 0.25rem;
    font-size: 0.875em;
    color: #dc3545;
}

.form-control.is-invalid ~ .invalid-feedback {
    display: block;
}`;
}

// Generate the JavaScript code
function generateJavaScript() {
  let validationFunctions = "";
  let fieldValidators = "";

  formFields.forEach((field) => {
    if (field.regex) {
      validationFunctions += generateValidationFunction(field);
      fieldValidators += `        ${
        field.name
      }Valid = check${capitalizeFirstLetter(field.name)}();\n`;
    }
  });

  return `$(document).ready(function() {
    // Add form validation listeners
${generateValidationListeners()}
    
    // Handle form submission
    $("#registrationForm").on("submit", function(e) {
        e.preventDefault();
        
        // Validate all fields
${fieldValidators}        
        // Check if all validations pass
        if (${generateValidationCheckCondition()}) {
            // All valid, add to table
            addToTable();
            
            // Reset form
            this.reset();
            $(".is-invalid").removeClass("is-invalid");
        }
    });
});

${validationFunctions}

/**
 * Add data from form to the table
 */
function addToTable() {
    // Get form data
${generateFormDataCollection()}
    
    // Add new row to table
    const rowCount = $("#dataTable tbody tr").length + 1;
    const newRow = \`<tr>
        <td>\${rowCount}</td>
${generateTableCells()}
    </tr>\`;
    
    $("#dataTable tbody").append(newRow);
}`;
}

// Generate validation function for a field
function generateValidationFunction(field) {
  let functionName = `check${capitalizeFirstLetter(field.name)}`;

  if (field.type === "radio") {
    return `
/**
 * Validate the ${field.label} selection
 */
function ${functionName}() {
    if (!$("input[name='${field.name}']:checked").length) {
        $("#${field.name}_${field.options[0].value}").addClass("is-invalid");
        return false;
    }
    $("input[name='${field.name}']").removeClass("is-invalid");
    return true;
}
`;
  } else if (field.type === "checkbox") {
    return `
/**
 * Validate the ${field.label} selection
 */
function ${functionName}() {
    if (!$("input[name='${field.name}[]']:checked").length) {
        $("input[name='${field.name}[]']").addClass("is-invalid");
        return false;
    }
    $("input[name='${field.name}[]']").removeClass("is-invalid");
    return true;
}
`;
  } else {
    return `
/**
 * Validate the ${field.label} field
 */
function ${functionName}() {
    var value = $("#${field.name}").val();
    
    // Check if value is empty and field is required
    if (${field.required} && value.trim() === "") {
        $("#${field.name}").addClass("is-invalid");
        return false;
    }
    
    // Check against regex pattern if not empty
    if (value.trim() !== "") {
        var regex = /${field.regex}/;
        if (!regex.test(value)) {
            $("#${field.name}").addClass("is-invalid");
            return false;
        }
    }
    
    $("#${field.name}").removeClass("is-invalid");
    return true;
}
`;
  }
}

// Generate validation listeners
function generateValidationListeners() {
  let listeners = "";

  formFields.forEach((field) => {
    if (field.regex) {
      if (field.type === "radio") {
        listeners += `    $("input[name='${
          field.name
        }']").on("change", check${capitalizeFirstLetter(field.name)});\n`;
      } else if (field.type === "checkbox") {
        listeners += `    $("input[name='${
          field.name
        }[]']").on("change", check${capitalizeFirstLetter(field.name)});\n`;
      } else {
        listeners += `    $("#${
          field.name
        }").on("blur", check${capitalizeFirstLetter(field.name)});\n`;
      }
    }
  });

  return listeners;
}

// Generate condition to check if all validations pass
function generateValidationCheckCondition() {
  const validationChecks = formFields
    .filter((field) => field.regex)
    .map((field) => `${field.name}Valid`)
    .join(" && ");

  return validationChecks || "true";
}

// Generate code to collect form data
function generateFormDataCollection() {
  let collection = "";

  formFields.forEach((field) => {
    if (field.type === "radio") {
      collection += `    const ${field.name} = $("input[name='${field.name}']:checked").val();\n`;
    } else if (field.type === "checkbox") {
      collection += `    const ${field.name} = [];\n`;
      collection += `    $("input[name='${field.name}[]']:checked").each(function() {\n`;
      collection += `        ${field.name}.push($(this).val());\n`;
      collection += `    });\n`;
    } else {
      collection += `    const ${field.name} = $("#${field.name}").val();\n`;
    }
  });

  return collection;
}

// Generate table cells for form data
function generateTableCells() {
  let cells = "";

  formFields.forEach((field) => {
    if (field.type === "checkbox") {
      cells += `        <td>\${${field.name}.join(", ")}</td>\n`;
    } else if (field.type === "date") {
      cells += `        <td>\${formatDate(${field.name})}</td>\n`;
    } else {
      cells += `        <td>\${${field.name}}</td>\n`;
    }
  });

  return cells;
}

// Helper function to capitalize the first letter of a string
function capitalizeFirstLetter(string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
}

// Generate and show complete code for export
function generateAndShowCode() {
  // Generate all code
  const config = window.webConfig || {
    websiteTitle: "Website Builder",
    headerBgColor: "#0d6efd",
    headerTextColor: "#ffffff",
    formBgColor: "#ffffff",
    formBorderColor: "#000000",
    footerBgColor: "#0d6efd",
    footerTextColor: "#ffffff",
    footerText: "MSSV: 23630851 | Họ tên: Lê Thành Long",
  };

  const htmlCode = generateHTML(config);
  const cssCode = generateCSS(config);
  const jsCode = generateJavaScript();

  // Display in the export modal
  $("#exportHtmlCode").text(htmlCode);
  $("#exportCssCode").text(cssCode);
  $("#exportJsCode").text(jsCode);

  // Show the modal
  new bootstrap.Modal(document.getElementById("exportModal")).show();
}

// Create a preview of the website
function previewWebsite() {
  const config = window.webConfig || {
    websiteTitle: "Website Builder",
    headerBgColor: "#0d6efd",
    headerTextColor: "#ffffff",
    formBgColor: "#ffffff",
    formBorderColor: "#000000",
    footerBgColor: "#0d6efd",
    footerTextColor: "#ffffff",
    footerText: "MSSV: 23630851 | Họ tên: Lê Thành Long",
  };

  const htmlCode = generateHTML(config);
  const cssCode = generateCSS(config);
  const jsCode = generateJavaScript();

  // Create a full HTML document with inline CSS and JS
  const previewDoc = `
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>${config.websiteTitle} - Preview</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            ${cssCode}
        </style>
    </head>
    <body>
        <div class="container" id="main-container">
            <!-- Header -->
            <header id="header">
                <h1>${config.websiteTitle}</h1>
            </header>
            
            <!-- Main content -->
            <div class="row" id="content">
                <div class="col-md-6">
                    <!-- Form -->
                    <div id="form-container">
                        <h3>Đăng ký thông tin</h3>
                        <form id="registrationForm">
                            ${formFields
                              .map((field) => generateFieldHTML(field))
                              .join("")}
                            <div class="row mt-3">
                                <div class="col-12">
                                    <button type="submit" class="btn btn-primary">Gửi</button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
                
                <div class="col-md-6">
                    <!-- Table -->
                    <div id="table-container">
                        <h3>Danh sách đăng ký</h3>
                        <table class="table table-bordered" id="dataTable">
                            <thead>
                                <tr>
                                    <th>STT</th>
                                    ${formFields
                                      .map((field) => `<th>${field.label}</th>`)
                                      .join("")}
                                </tr>
                            </thead>
                            <tbody>
                                <!-- Data will be added here -->
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
            
            <!-- Footer -->
            <footer id="footer">
                <p>${config.footerText}</p>
            </footer>
        </div>

        <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
        <script>
            ${jsCode}
            
            // Helper function for date formatting
            function formatDate(dateString) {
                if (!dateString) return "";
                const date = new Date(dateString);
                const day = date.getDate().toString().padStart(2, "0");
                const month = (date.getMonth() + 1).toString().padStart(2, "0");
                const year = date.getFullYear();
                return \`\${day}/\${month}/\${year}\`;
            }
        </script>
    </body>
    </html>
    `;

  // Set the preview iframe content
  const iframe = document.getElementById("previewFrame");
  iframe.srcdoc = previewDoc;

  // Show the preview modal
  new bootstrap.Modal(document.getElementById("previewModal")).show();
}

// Download code as ZIP
$("#downloadZip").on("click", function () {
  const config = window.webConfig || {
    websiteTitle: "Website Builder",
    headerBgColor: "#0d6efd",
    headerTextColor: "#ffffff",
    formBgColor: "#ffffff",
    formBorderColor: "#000000",
    footerBgColor: "#0d6efd",
    footerTextColor: "#ffffff",
    footerText: "MSSV: 23630851 | Họ tên: Lê Thành Long",
  };

  const htmlCode = generateHTML(config);
  const cssCode = generateCSS(config);
  const jsCode = generateJavaScript();

  // Create a new JSZip instance
  const zip = new JSZip();

  // Add files to the ZIP
  zip.file("index.html", htmlCode);

  // Add CSS folder and file
  const cssFolder = zip.folder("css");
  cssFolder.file("style.css", cssCode);

  // Add JS folder and file
  const jsFolder = zip.folder("js");
  jsFolder.file("script.js", jsCode);

  // Generate and download ZIP
  zip.generateAsync({ type: "blob" }).then(function (content) {
    saveAs(content, "website.zip");
  });
});
