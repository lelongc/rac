/**
 * Field Editor for Modal Form Fields
 */

// Global variables for field editor
let currentModalComponent = null;
let currentFieldIndex = null;
let fieldsTemp = [];
const fieldEditorModal = $("#field-editor-modal");
const newFieldModal = $("#new-field-modal");

/**
 * Initialize the field editor
 */
function initFieldEditor() {
  // Open field editor when edit fields button is clicked
  $(document).on("click", ".edit-modal-fields-btn", function (e) {
    e.preventDefault();
    e.stopPropagation();

    // Get the parent modal component
    currentModalComponent = $(this).closest(
      '.canvas-component[data-type="modal"]'
    );

    if (currentModalComponent) {
      // Get fields from component data
      fieldsTemp = JSON.parse(
        JSON.stringify(currentModalComponent.data("fields") || [])
      );

      // Reset selection
      currentFieldIndex = null;

      // Populate the field list
      refreshFieldList();

      // Show the field editor modal
      fieldEditorModal.modal("show");
    }
  });

  // Handle add new field button
  $("#add-new-field-btn").on("click", function () {
    newFieldModal.modal("show");
  });

  // Handle add field button in the new field modal
  $("#add-field-btn").on("click", function () {
    const fieldType = $("#new-field-type").val();
    const fieldLabel = $("#new-field-label").val();

    if (fieldLabel.trim() === "") {
      alert("Vui lòng nhập nhãn cho trường!");
      return;
    }

    // Create new field object based on type
    const newField = createNewFieldObject(fieldType, fieldLabel);

    // Add to temporary fields array
    fieldsTemp.push(newField);

    // Refresh the field list
    refreshFieldList();

    // Close the new field modal
    newFieldModal.modal("hide");

    // Reset new field form
    $("#new-field-label").val("");

    // Select the new field
    selectField(fieldsTemp.length - 1);
  });

  // Handle field selection
  $("#field-list").on("click", ".field-item", function () {
    const index = $(this).data("index");
    selectField(index);
  });

  // Handle field move up
  $("#field-list").on("click", ".move-field-up", function (e) {
    e.stopPropagation();
    const index = $(this).closest(".field-item").data("index");

    if (index > 0) {
      // Swap with previous field
      const temp = fieldsTemp[index];
      fieldsTemp[index] = fieldsTemp[index - 1];
      fieldsTemp[index - 1] = temp;

      // Refresh list and select the moved field
      refreshFieldList();
      selectField(index - 1);
    }
  });

  // Handle field move down
  $("#field-list").on("click", ".move-field-down", function (e) {
    e.stopPropagation();
    const index = $(this).closest(".field-item").data("index");

    if (index < fieldsTemp.length - 1) {
      // Swap with next field
      const temp = fieldsTemp[index];
      fieldsTemp[index] = fieldsTemp[index + 1];
      fieldsTemp[index + 1] = temp;

      // Refresh list and select the moved field
      refreshFieldList();
      selectField(index + 1);
    }
  });

  // Handle field delete
  $("#field-list").on("click", ".delete-field", function (e) {
    e.stopPropagation();
    const index = $(this).closest(".field-item").data("index");

    if (confirm("Bạn có chắc muốn xóa trường này?")) {
      // Remove field
      fieldsTemp.splice(index, 1);

      // Refresh list
      refreshFieldList();

      // Clear properties
      $("#field-properties-container").html(
        '<p class="text-center text-muted">Chọn một trường từ danh sách để chỉnh sửa</p>'
      );
      currentFieldIndex = null;
    }
  });

  // Handle save changes
  $("#save-fields-btn").on("click", function () {
    // Save to component data
    if (currentModalComponent) {
      currentModalComponent.data("fields", fieldsTemp);

      // Update the modal preview
      updateModalPreviewFields(currentModalComponent);

      // Close modal
      fieldEditorModal.modal("hide");
    }
  });
}

/**
 * Refresh the field list in the editor
 */
function refreshFieldList() {
  const fieldList = $("#field-list");
  fieldList.empty();

  fieldsTemp.forEach((field, index) => {
    const fieldTypeLabel = getFieldTypeLabel(field.type);
    const requiredBadge = field.required
      ? '<span class="badge badge-danger badge-pill ml-1">*</span>'
      : "";

    fieldList.append(`
      <li class="list-group-item field-item d-flex align-items-center justify-content-between" data-index="${index}">
        <div>
          <i class="${getFieldTypeIcon(field.type)} mr-2"></i>
          <span class="field-label">${field.label}</span>
          ${requiredBadge}
          <small class="text-muted d-block">${fieldTypeLabel}</small>
        </div>
        <div class="field-actions">
          <button type="button" class="btn btn-sm btn-light move-field-up" title="Di chuyển lên">
            <i class="fas fa-chevron-up"></i>
          </button>
          <button type="button" class="btn btn-sm btn-light move-field-down" title="Di chuyển xuống">
            <i class="fas fa-chevron-down"></i>
          </button>
          <button type="button" class="btn btn-sm btn-danger delete-field" title="Xóa trường">
            <i class="fas fa-trash"></i>
          </button>
        </div>
      </li>
    `);
  });
}

/**
 * Get an icon class for a field type
 */
function getFieldTypeIcon(fieldType) {
  switch (fieldType) {
    case "text-field":
      return "fas fa-keyboard";
    case "email-field":
      return "fas fa-at";
    case "date-field":
      return "far fa-calendar-alt";
    case "select":
      return "fas fa-caret-down";
    case "radio-group":
      return "far fa-dot-circle";
    case "checkbox-group":
      return "far fa-check-square";
    case "readonly-field":
      return "fas fa-lock";
    default:
      return "fas fa-keyboard";
  }
}

/**
 * Get a display label for a field type
 */
function getFieldTypeLabel(fieldType) {
  switch (fieldType) {
    case "text-field":
      return "Trường văn bản";
    case "email-field":
      return "Trường email";
    case "date-field":
      return "Trường ngày tháng";
    case "select":
      return "Dropdown lựa chọn";
    case "radio-group":
      return "Nhóm radio button";
    case "checkbox-group":
      return "Nhóm checkbox";
    case "readonly-field":
      return "Trường chỉ đọc";
    default:
      return "Trường không xác định";
  }
}

/**
 * Create a new field object based on the field type
 */
function createNewFieldObject(fieldType, fieldLabel) {
  // Generate a unique ID based on field type and timestamp
  const timestamp = new Date().getTime();
  let fieldId;

  switch (fieldType) {
    case "text-field":
      fieldId = `txt${capitalizeFirstLetter(fieldLabel.replace(/\s+/g, ""))}`;
      return {
        type: "text-field",
        label: fieldLabel,
        id: fieldId,
        required: true,
        placeholder: "",
        validation: {
          regex: "",
          message: "",
          function: `check${capitalizeFirstLetter(
            fieldLabel.replace(/\s+/g, "")
          )}`,
        },
      };

    case "email-field":
      return {
        type: "email-field",
        label: fieldLabel,
        id: `txtEmail_${timestamp}`,
        required: true,
        placeholder: "your.email@example.com",
        validation: {
          regex: "@.*\\.com$",
          message: "Email phải chứa @ và kết thúc với .com",
          function: "checkEmail",
        },
      };

    case "date-field":
      return {
        type: "date-field",
        label: fieldLabel,
        id: `txtDate_${timestamp}`,
        required: true,
        validation: {
          function: `check${capitalizeFirstLetter(
            fieldLabel.replace(/\s+/g, "")
          )}`,
        },
      };

    case "select":
      return {
        type: "select",
        label: fieldLabel,
        id: `sl${capitalizeFirstLetter(fieldLabel.replace(/\s+/g, ""))}`,
        required: true,
        options: [
          { value: "1", text: "Tùy chọn 1" },
          { value: "2", text: "Tùy chọn 2" },
          { value: "3", text: "Tùy chọn 3" },
        ],
      };

    case "radio-group":
      return {
        type: "radio-group",
        label: fieldLabel,
        name: `radio_${timestamp}`,
        required: true,
        options: [
          {
            id: `radio1_${timestamp}`,
            value: "Tùy chọn 1",
            text: "Tùy chọn 1",
            checked: true,
          },
          {
            id: `radio2_${timestamp}`,
            value: "Tùy chọn 2",
            text: "Tùy chọn 2",
          },
        ],
        validation: {
          function: `check${capitalizeFirstLetter(
            fieldLabel.replace(/\s+/g, "")
          )}`,
        },
      };

    case "checkbox-group":
      return {
        type: "checkbox-group",
        label: fieldLabel,
        id: `chk${capitalizeFirstLetter(fieldLabel.replace(/\s+/g, ""))}`,
        required: true,
        options: [
          { id: `chk1_${timestamp}`, value: "Tùy chọn 1", text: "Tùy chọn 1" },
          { id: `chk2_${timestamp}`, value: "Tùy chọn 2", text: "Tùy chọn 2" },
          { id: `chk3_${timestamp}`, value: "Tùy chọn 3", text: "Tùy chọn 3" },
        ],
        validation: {
          function: `check${capitalizeFirstLetter(
            fieldLabel.replace(/\s+/g, "")
          )}`,
        },
      };

    case "readonly-field":
      return {
        type: "readonly-field",
        label: fieldLabel,
        id: `txtReadonly_${timestamp}`,
        required: false,
        readonly: true,
      };

    default:
      // Default to text field if unknown type
      return {
        type: "text-field",
        label: fieldLabel,
        id: `txtField_${timestamp}`,
        required: true,
      };
  }
}

/**
 * Capitalize the first letter of a string
 */
function capitalizeFirstLetter(string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
}

/**
 * Select a field in the editor
 */
function selectField(index) {
  currentFieldIndex = index;

  // Highlight the selected field
  $(".field-item").removeClass("active");
  $(`.field-item[data-index="${index}"]`).addClass("active");

  // Show field properties based on field type
  const field = fieldsTemp[index];

  if (field) {
    let propertiesHtml = `
      <form id="field-properties-form">
        <div class="form-group">
          <label for="field-label">Nhãn trường:</label>
          <input type="text" class="form-control" id="field-label" value="${
            field.label
          }">
        </div>
        
        <div class="form-group">
          <label for="field-id">ID trường:</label>
          <input type="text" class="form-control" id="field-id" value="${
            field.id
          }">
          <small class="form-text text-muted">ID dùng để truy cập trường trong JavaScript</small>
        </div>
        
        <div class="form-check mb-3">
          <input type="checkbox" class="form-check-input" id="field-required" ${
            field.required ? "checked" : ""
          }>
          <label class="form-check-label" for="field-required">Bắt buộc nhập</label>
        </div>
    `;

    // Additional properties based on field type
    switch (field.type) {
      case "text-field":
      case "email-field":
        propertiesHtml += `
          <div class="form-group">
            <label for="field-placeholder">Văn bản gợi ý:</label>
            <input type="text" class="form-control" id="field-placeholder" value="${
              field.placeholder || ""
            }">
          </div>
          
          <hr>
          <h6>Kiểm tra hợp lệ (Validation)</h6>
          
          <div class="form-group">
            <label for="field-regex">Biểu thức chính quy (Regex):</label>
            <input type="text" class="form-control" id="field-regex" value="${
              field.validation?.regex || ""
            }">
            <small class="form-text text-muted">Để trống nếu không cần kiểm tra bằng regex</small>
          </div>
          
          <div class="form-group">
            <label for="field-error-message">Thông báo lỗi:</label>
            <input type="text" class="form-control" id="field-error-message" value="${
              field.validation?.message || ""
            }">
          </div>
          
          <div class="form-group">
            <label for="field-validation-function">Tên hàm kiểm tra:</label>
            <input type="text" class="form-control" id="field-validation-function" value="${
              field.validation?.function || ""
            }">
          </div>
        `;
        break;

      case "date-field":
        propertiesHtml += `
          <hr>
          <h6>Kiểm tra hợp lệ (Validation)</h6>
          
          <div class="form-group">
            <label for="field-validation-function">Tên hàm kiểm tra:</label>
            <input type="text" class="form-control" id="field-validation-function" value="${
              field.validation?.function || ""
            }">
          </div>
          
          <div class="form-check mb-3">
            <input type="checkbox" class="form-check-input" id="field-past-only" checked>
            <label class="form-check-label" for="field-past-only">Chỉ cho phép chọn ngày trong quá khứ</label>
          </div>
        `;
        break;

      case "select":
        propertiesHtml += `
          <hr>
          <h6>Tùy chọn</h6>
          <div id="select-options">
        `;

        // Add options
        field.options.forEach((option, optIndex) => {
          propertiesHtml += `
            <div class="form-row mb-2 option-row">
              <div class="col-5">
                <input type="text" class="form-control form-control-sm option-value" value="${option.value}" placeholder="Giá trị">
              </div>
              <div class="col-5">
                <input type="text" class="form-control form-control-sm option-text" value="${option.text}" placeholder="Văn bản">
              </div>
              <div class="col-2">
                <button type="button" class="btn btn-sm btn-danger remove-option">
                  <i class="fas fa-trash"></i>
                </button>
              </div>
            </div>
          `;
        });

        propertiesHtml += `
          </div>
          <button type="button" class="btn btn-sm btn-primary mt-2" id="add-select-option">
            <i class="fas fa-plus"></i> Thêm tùy chọn
          </button>
        `;
        break;

      case "radio-group":
        propertiesHtml += `
          <div class="form-group">
            <label for="field-name">Name attribute:</label>
            <input type="text" class="form-control" id="field-name" value="${field.name}">
            <small class="form-text text-muted">Thuộc tính name để nhóm các radio buttons</small>
          </div>
          
          <hr>
          <h6>Tùy chọn</h6>
          <div id="radio-options">
        `;

        // Add options
        field.options.forEach((option, optIndex) => {
          propertiesHtml += `
            <div class="form-row mb-2 option-row">
              <div class="col-5">
                <input type="text" class="form-control form-control-sm option-value" value="${
                  option.value
                }" placeholder="Giá trị">
              </div>
              <div class="col-4">
                <input type="text" class="form-control form-control-sm option-text" value="${
                  option.text
                }" placeholder="Văn bản">
              </div>
              <div class="col-2">
                <div class="form-check">
                  <input type="radio" class="form-check-input option-checked" ${
                    option.checked ? "checked" : ""
                  } name="radio-default">
                  <label class="form-check-label">Mặc định</label>
                </div>
              </div>
              <div class="col-1">
                <button type="button" class="btn btn-sm btn-danger remove-option">
                  <i class="fas fa-trash"></i>
                </button>
              </div>
            </div>
          `;
        });

        propertiesHtml += `
          </div>
          <button type="button" class="btn btn-sm btn-primary mt-2" id="add-radio-option">
            <i class="fas fa-plus"></i> Thêm tùy chọn
          </button>
          
          <hr>
          <h6>Kiểm tra hợp lệ (Validation)</h6>
          <div class="form-group">
            <label for="field-validation-function">Tên hàm kiểm tra:</label>
            <input type="text" class="form-control" id="field-validation-function" value="${
              field.validation?.function || ""
            }">
          </div>
        `;
        break;

      case "checkbox-group":
        propertiesHtml += `
          <hr>
          <h6>Tùy chọn</h6>
          <div id="checkbox-options">
        `;

        // Add options
        field.options.forEach((option, optIndex) => {
          propertiesHtml += `
            <div class="form-row mb-2 option-row">
              <div class="col-5">
                <input type="text" class="form-control form-control-sm option-value" value="${option.value}" placeholder="Giá trị">
              </div>
              <div class="col-5">
                <input type="text" class="form-control form-control-sm option-text" value="${option.text}" placeholder="Văn bản">
              </div>
              <div class="col-2">
                <button type="button" class="btn btn-sm btn-danger remove-option">
                  <i class="fas fa-trash"></i>
                </button>
              </div>
            </div>
          `;
        });

        propertiesHtml += `
          </div>
          <button type="button" class="btn btn-sm btn-primary mt-2" id="add-checkbox-option">
            <i class="fas fa-plus"></i> Thêm tùy chọn
          </button>
          
          <hr>
          <h6>Kiểm tra hợp lệ (Validation)</h6>
          <div class="form-group">
            <label for="field-validation-function">Tên hàm kiểm tra:</label>
            <input type="text" class="form-control" id="field-validation-function" value="${
              field.validation?.function || ""
            }">
          </div>
          
          <div class="form-check mb-3">
            <input type="checkbox" class="form-check-input" id="field-min-required" checked>
            <label class="form-check-label" for="field-min-required">Yêu cầu chọn ít nhất 1 mục</label>
          </div>
        `;
        break;

      case "readonly-field":
        propertiesHtml += `
          <div class="form-check mb-3">
            <input type="checkbox" class="form-check-input" id="field-readonly" ${
              field.readonly ? "checked" : ""
            }>
            <label class="form-check-label" for="field-readonly">Chỉ đọc (không thể chỉnh sửa)</label>
          </div>
        `;
        break;
    }

    // Close the form tag
    propertiesHtml += `
      </form>
      <button type="button" class="btn btn-primary mt-3" id="apply-field-properties">Áp dụng thay đổi</button>
    `;

    // Set the HTML and initialize event handlers
    $("#field-properties-container").html(propertiesHtml);
    initFieldPropertiesHandlers(field);
  }
}

/**
 * Initialize event handlers for field properties
 */
function initFieldPropertiesHandlers(field) {
  // Apply button click handler
  $("#apply-field-properties").on("click", function () {
    updateFieldFromForm(field);
  });

  // Add option buttons for select, radio, checkbox
  $("#add-select-option").on("click", function () {
    const optionsContainer = $("#select-options");
    optionsContainer.append(`
      <div class="form-row mb-2 option-row">
        <div class="col-5">
          <input type="text" class="form-control form-control-sm option-value" value="" placeholder="Giá trị">
        </div>
        <div class="col-5">
          <input type="text" class="form-control form-control-sm option-text" value="" placeholder="Văn bản">
        </div>
        <div class="col-2">
          <button type="button" class="btn btn-sm btn-danger remove-option">
            <i class="fas fa-trash"></i>
          </button>
        </div>
      </div>
    `);
  });

  $("#add-radio-option").on("click", function () {
    const optionsContainer = $("#radio-options");
    optionsContainer.append(`
      <div class="form-row mb-2 option-row">
        <div class="col-5">
          <input type="text" class="form-control form-control-sm option-value" value="" placeholder="Giá trị">
        </div>
        <div class="col-4">
          <input type="text" class="form-control form-control-sm option-text" value="" placeholder="Văn bản">
        </div>
        <div class="col-2">
          <div class="form-check">
            <input type="radio" class="form-check-input option-checked" name="radio-default">
            <label class="form-check-label">Mặc định</label>
          </div>
        </div>
        <div class="col-1">
          <button type="button" class="btn btn-sm btn-danger remove-option">
            <i class="fas fa-trash"></i>
          </button>
        </div>
      </div>
    `);
  });

  $("#add-checkbox-option").on("click", function () {
    const optionsContainer = $("#checkbox-options");
    optionsContainer.append(`
      <div class="form-row mb-2 option-row">
        <div class="col-5">
          <input type="text" class="form-control form-control-sm option-value" value="" placeholder="Giá trị">
        </div>
        <div class="col-5">
          <input type="text" class="form-control form-control-sm option-text" value="" placeholder="Văn bản">
        </div>
        <div class="col-2">
          <button type="button" class="btn btn-sm btn-danger remove-option">
            <i class="fas fa-trash"></i>
          </button>
        </div>
      </div>
    `);
  });

  // Remove option button
  $(document).on("click", ".remove-option", function () {
    $(this).closest(".option-row").remove();
  });
}

/**
 * Update field data from the properties form
 */
function updateFieldFromForm(field) {
  if (!field || currentFieldIndex === null) return;

  // Common properties
  field.label = $("#field-label").val();
  field.id = $("#field-id").val();
  field.required = $("#field-required").is(":checked");

  // Type specific properties
  switch (field.type) {
    case "text-field":
    case "email-field":
      field.placeholder = $("#field-placeholder").val();

      // Validation properties
      if (!field.validation) field.validation = {};
      field.validation.regex = $("#field-regex").val();
      field.validation.message = $("#field-error-message").val();
      field.validation.function = $("#field-validation-function").val();
      break;

    case "date-field":
      // Validation
      if (!field.validation) field.validation = {};
      field.validation.function = $("#field-validation-function").val();
      break;

    case "select":
      // Options
      field.options = [];
      $("#select-options .option-row").each(function () {
        const value = $(this).find(".option-value").val();
        const text = $(this).find(".option-text").val();

        if (value && text) {
          field.options.push({
            value: value,
            text: text,
          });
        }
      });
      break;

    case "radio-group":
      field.name = $("#field-name").val();

      // Options
      field.options = [];
      $("#radio-options .option-row").each(function () {
        const value = $(this).find(".option-value").val();
        const text = $(this).find(".option-text").val();
        const checked = $(this).find(".option-checked").is(":checked");
        const id = `radio_${new Date().getTime()}_${field.options.length}`;

        if (value && text) {
          field.options.push({
            id: id,
            value: value,
            text: text,
            checked: checked,
          });
        }
      });

      // Validation
      if (!field.validation) field.validation = {};
      field.validation.function = $("#field-validation-function").val();
      break;

    case "checkbox-group":
      // Options
      field.options = [];
      $("#checkbox-options .option-row").each(function () {
        const value = $(this).find(".option-value").val();
        const text = $(this).find(".option-text").val();
        const id = `chk_${new Date().getTime()}_${field.options.length}`;

        if (value && text) {
          field.options.push({
            id: id,
            value: value,
            text: text,
          });
        }
      });

      // Validation
      if (!field.validation) field.validation = {};
      field.validation.function = $("#field-validation-function").val();
      break;

    case "readonly-field":
      field.readonly = $("#field-readonly").is(":checked");
      break;
  }

  // Update the temp array
  fieldsTemp[currentFieldIndex] = field;

  // Refresh the field list
  refreshFieldList();

  // Highlight the current field
  $(`.field-item[data-index="${currentFieldIndex}"]`).addClass("active");

  // Show success message
  alert("Đã áp dụng thay đổi cho trường!");
}
