/**
 * Modal Form Editor for GFree English Course Web Builder
 * Provides a dedicated interface for editing form fields in the Modal component
 * with enhanced validation capabilities
 */

const ModalFormEditor = (function () {
  // State management
  const state = {
    modalComponent: null,
    currentField: null,
    isEditing: false,
    editorVisible: false,
    validationPresets: {
      name: {
        regex: "^[A-Z][a-z]*(\\s+[A-Z][a-z]*)+$",
        message: "Mỗi từ phải bắt đầu bằng chữ hoa và phần còn lại viết thường",
      },
      phone: {
        regex: "^(09|03|08)\\d{8}$",
        message: "Số điện thoại phải có 10 số và bắt đầu với 09, 03 hoặc 08",
      },
      email: {
        regex: "@.*\\.com$",
        message: "Email phải chứa @ và kết thúc với .com",
      },
      numbers: {
        regex: "^\\d+$",
        message: "Vui lòng chỉ nhập số",
      },
    },
  };

  /**
   * Initialize the editor
   */
  function init() {
    // Create editor UI if not already present
    if (!document.getElementById("modal-form-editor")) {
      createEditorUI();
    }

    // Setup event listeners for component selection
    document.addEventListener("componentSelected", handleComponentSelected);

    console.log("Modal Form Editor initialized");
  }

  /**
   * Create the editor UI
   */
  function createEditorUI() {
    const editorContainer = document.createElement("div");
    editorContainer.id = "modal-form-editor";
    editorContainer.className = "modal fade";
    editorContainer.setAttribute("tabindex", "-1");

    editorContainer.innerHTML = `
            <div class="modal-dialog modal-lg">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">Form Field Editor</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="row">
                            <!-- Left side: Fields list -->
                            <div class="col-md-4 border-end">
                                <div class="d-flex justify-content-between align-items-center mb-2">
                                    <h6 class="mb-0">Form Fields</h6>
                                    <button id="add-field-btn" class="btn btn-sm btn-primary">
                                        <i class="bi bi-plus-circle"></i> Add
                                    </button>
                                </div>
                                <div id="form-fields-list" class="list-group">
                                    <!-- Fields will be listed here -->
                                </div>
                            </div>
                            
                            <!-- Right side: Field editor -->
                            <div class="col-md-8">
                                <div id="field-editor-container">
                                    <!-- Field editor will be rendered here -->
                                    <div class="text-center text-muted py-5" id="no-field-selected">
                                        <i class="bi bi-arrow-left-circle fs-2"></i>
                                        <p>Select a field to edit or add a new one</p>
                                    </div>
                                    
                                    <div id="field-editor-form" style="display: none;">
                                        <!-- Tabs for different field properties -->
                                        <ul class="nav nav-tabs" id="field-editor-tabs" role="tablist">
                                            <li class="nav-item" role="presentation">
                                                <button class="nav-link active" id="basic-tab" data-bs-toggle="tab" data-bs-target="#basic-pane" 
                                                    type="button" role="tab" aria-controls="basic-pane" aria-selected="true">Basic</button>
                                            </li>
                                            <li class="nav-item" role="presentation">
                                                <button class="nav-link" id="validation-tab" data-bs-toggle="tab" data-bs-target="#validation-pane" 
                                                    type="button" role="tab" aria-controls="validation-pane" aria-selected="false">Validation</button>
                                            </li>
                                            <li class="nav-item" id="options-tab-item" style="display: none;">
                                                <button class="nav-link" id="options-tab" data-bs-toggle="tab" data-bs-target="#options-pane" 
                                                    type="button" role="tab" aria-controls="options-pane" aria-selected="false">Options</button>
                                            </li>
                                        </ul>
                                        
                                        <div class="tab-content p-3 border border-top-0 rounded-bottom" id="field-editor-tab-content">
                                            <!-- Basic tab content -->
                                            <div class="tab-pane fade show active" id="basic-pane" role="tabpanel" aria-labelledby="basic-tab">
                                                <!-- Basic field properties -->
                                            </div>
                                            
                                            <!-- Validation tab content -->
                                            <div class="tab-pane fade" id="validation-pane" role="tabpanel" aria-labelledby="validation-tab">
                                                <!-- Validation properties -->
                                            </div>
                                            
                                            <!-- Options tab content (for select, checkbox, radio) -->
                                            <div class="tab-pane fade" id="options-pane" role="tabpanel" aria-labelledby="options-tab">
                                                <!-- Options for select, checkbox, radio -->
                                            </div>
                                        </div>
                                        
                                        <!-- Preview area -->
                                        <div class="mt-3">
                                            <h6 class="border-bottom pb-2 mb-2 d-flex justify-content-between">
                                                <span>Field Preview</span>
                                                <button id="toggle-preview-btn" class="btn btn-sm btn-outline-secondary">
                                                    <i class="bi bi-eye"></i> Show
                                                </button>
                                            </h6>
                                            <div id="field-preview" class="border p-3 rounded" style="display: none;">
                                                <!-- Field preview will be shown here -->
                                            </div>
                                        </div>
                                        
                                        <!-- Action buttons -->
                                        <div class="d-flex justify-content-end mt-3">
                                            <button type="button" id="save-field-btn" class="btn btn-primary">Save Field</button>
                                            <button type="button" id="cancel-edit-btn" class="btn btn-outline-secondary ms-2">Cancel</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;

    document.body.appendChild(editorContainer);
    setupEditorEventListeners();
  }

  /**
   * Setup event listeners for the editor UI
   */
  function setupEditorEventListeners() {
    const editor = document.getElementById("modal-form-editor");

    // Add field button
    editor
      .querySelector("#add-field-btn")
      .addEventListener("click", function () {
        createNewField();
      });

    // Toggle preview button
    editor
      .querySelector("#toggle-preview-btn")
      .addEventListener("click", function () {
        const previewArea = document.getElementById("field-preview");
        const isVisible = previewArea.style.display !== "none";

        previewArea.style.display = isVisible ? "none" : "block";
        this.innerHTML = isVisible
          ? '<i class="bi bi-eye"></i> Show'
          : '<i class="bi bi-eye-slash"></i> Hide';

        if (!isVisible) {
          updateFieldPreview();
        }
      });

    // Save field button
    editor
      .querySelector("#save-field-btn")
      .addEventListener("click", saveField);

    // Cancel button
    editor
      .querySelector("#cancel-edit-btn")
      .addEventListener("click", cancelEditing);
  }

  /**
   * Handle component selection events
   */
  function handleComponentSelected(e) {
    const componentId = e.detail.componentId;
    if (!componentId) {
      return;
    }

    const component = window.pageModelManager.getComponentById(componentId);
    if (component && component.type === "modal") {
      state.modalComponent = component;

      // Add "Edit Form Fields" button to properties panel
      addFormFieldsEditorButton();
    } else {
      state.modalComponent = null;
    }
  }

  /**
   * Add a button to the properties panel to open the form fields editor
   */
  function addFormFieldsEditorButton() {
    // Check if the specific properties container exists
    const specificPropsContainer = document.getElementById(
      "specific-props-container"
    );
    if (!specificPropsContainer) return;

    // Remove any existing button to avoid duplicates
    const existingBtn = document.getElementById("edit-form-fields-btn");
    if (existingBtn) existingBtn.remove();

    // Create the button
    const buttonContainer = document.createElement("div");
    buttonContainer.className = "mb-3 mt-3";
    buttonContainer.innerHTML = `
            <button id="edit-form-fields-btn" class="btn btn-primary w-100">
                <i class="bi bi-list-check me-1"></i> Edit Form Fields
            </button>
        `;

    // Add to the container
    specificPropsContainer.appendChild(buttonContainer);

    // Add click event
    document
      .getElementById("edit-form-fields-btn")
      .addEventListener("click", openFormEditor);
  }

  /**
   * Open the form fields editor modal
   */
  function openFormEditor() {
    if (!state.modalComponent) return;

    // Populate the fields list
    renderFieldsList();

    // Show the editor modal
    const editorModal = document.getElementById("modal-form-editor");
    const bsModal = new bootstrap.Modal(editorModal);
    bsModal.show();

    state.editorVisible = true;
  }

  /**
   * Render the list of form fields
   */
  function renderFieldsList() {
    const fieldsListContainer = document.getElementById("form-fields-list");
    if (!fieldsListContainer || !state.modalComponent) return;

    // Clear the container
    fieldsListContainer.innerHTML = "";

    // Get the form fields
    const formFields = state.modalComponent.formFields || [];

    if (formFields.length === 0) {
      fieldsListContainer.innerHTML = `
                <div class="text-center text-muted p-3">
                    <p>No fields added yet</p>
                    <p>Click 'Add' to create your first field</p>
                </div>
            `;
      return;
    }

    // Create a list item for each field
    formFields.forEach((field) => {
      const fieldItem = document.createElement("div");
      fieldItem.className =
        "list-group-item list-group-item-action d-flex justify-content-between align-items-center";
      fieldItem.dataset.fieldId = field.id;

      // Field info
      const fieldInfo = document.createElement("div");
      fieldInfo.innerHTML = `
                <strong>${field.label || "Unnamed Field"}</strong>
                <br>
                <small class="text-muted">${field.type || "text"} ${
        field.id ? "- #" + field.id : ""
      }</small>
            `;

      // Field actions
      const fieldActions = document.createElement("div");
      fieldActions.innerHTML = `
                <button class="btn btn-sm btn-outline-primary me-1 edit-field-btn" data-field-id="${field.id}">
                    <i class="bi bi-pencil"></i>
                </button>
                <button class="btn btn-sm btn-outline-danger delete-field-btn" data-field-id="${field.id}">
                    <i class="bi bi-trash"></i>
                </button>
            `;

      fieldItem.appendChild(fieldInfo);
      fieldItem.appendChild(fieldActions);
      fieldsListContainer.appendChild(fieldItem);

      // Add click event to the item
      fieldItem.addEventListener("click", function (e) {
        // Only handle clicks on the item itself, not on the buttons
        if (!e.target.closest("button")) {
          editField(field.id);
        }
      });
    });

    // Add event listeners for edit and delete buttons
    fieldsListContainer.querySelectorAll(".edit-field-btn").forEach((btn) => {
      btn.addEventListener("click", function () {
        editField(this.dataset.fieldId);
      });
    });

    fieldsListContainer.querySelectorAll(".delete-field-btn").forEach((btn) => {
      btn.addEventListener("click", function () {
        deleteField(this.dataset.fieldId);
      });
    });
  }

  /**
   * Create a new field
   */
  function createNewField() {
    // Create a default field object
    state.currentField = {
      id: generateFieldId(),
      type: "text",
      label: "New Field",
      placeholder: "",
      required: false,
      validation: {
        enabled: false,
        regex: "",
        errorMessage: "Please enter a valid value",
        minLength: "",
        maxLength: "",
      },
    };

    state.isEditing = false;
    showFieldEditor();
    renderBasicTab();
    renderValidationTab();
  }

  /**
   * Edit an existing field
   */
  function editField(fieldId) {
    if (!state.modalComponent || !fieldId) return;

    // Find the field in the component
    const field = (state.modalComponent.formFields || []).find(
      (f) => f.id === fieldId
    );
    if (!field) {
      console.error("Field not found:", fieldId);
      return;
    }

    // Clone the field to avoid modifying the original directly
    state.currentField = JSON.parse(JSON.stringify(field));
    state.isEditing = true;

    // Make sure validation object exists
    if (!state.currentField.validation) {
      state.currentField.validation = {
        enabled: false,
        regex: "",
        errorMessage: "Please enter a valid value",
      };
    }

    showFieldEditor();
    renderBasicTab();
    renderValidationTab();

    // Show options tab for select, radio, checkbox
    if (["select", "radio", "checkbox"].includes(state.currentField.type)) {
      document.getElementById("options-tab-item").style.display = "";
      renderOptionsTab();
    } else {
      document.getElementById("options-tab-item").style.display = "none";
    }
  }

  /**
   * Delete a field
   */
  function deleteField(fieldId) {
    if (!state.modalComponent || !fieldId) return;

    if (!confirm("Are you sure you want to delete this field?")) {
      return;
    }

    // Remove the field from the component
    if (!state.modalComponent.formFields) {
      state.modalComponent.formFields = [];
    }

    state.modalComponent.formFields = state.modalComponent.formFields.filter(
      (f) => f.id !== fieldId
    );

    // Update the UI
    renderFieldsList();

    // Hide the editor if the current field was deleted
    if (state.currentField && state.currentField.id === fieldId) {
      hideFieldEditor();
    }

    // Notify model updated
    notifyModelUpdated();
  }

  /**
   * Show the field editor
   */
  function showFieldEditor() {
    document.getElementById("no-field-selected").style.display = "none";
    document.getElementById("field-editor-form").style.display = "block";
  }

  /**
   * Hide the field editor
   */
  function hideFieldEditor() {
    document.getElementById("no-field-selected").style.display = "block";
    document.getElementById("field-editor-form").style.display = "none";
    state.currentField = null;
  }

  /**
   * Render the basic tab content
   */
  function renderBasicTab() {
    const field = state.currentField;
    if (!field) return;

    const basicPane = document.getElementById("basic-pane");

    basicPane.innerHTML = `
            <div class="mb-3">
                <label for="field-type" class="form-label">Field Type</label>
                <select class="form-select" id="field-type">
                    <option value="text" ${
                      field.type === "text" ? "selected" : ""
                    }>Text</option>
                    <option value="email" ${
                      field.type === "email" ? "selected" : ""
                    }>Email</option>
                    <option value="number" ${
                      field.type === "number" ? "selected" : ""
                    }>Number</option>
                    <option value="password" ${
                      field.type === "password" ? "selected" : ""
                    }>Password</option>
                    <option value="date" ${
                      field.type === "date" ? "selected" : ""
                    }>Date</option>
                    <option value="textarea" ${
                      field.type === "textarea" ? "selected" : ""
                    }>Text Area</option>
                    <option value="select" ${
                      field.type === "select" ? "selected" : ""
                    }>Select Dropdown</option>
                    <option value="radio" ${
                      field.type === "radio" ? "selected" : ""
                    }>Radio Group</option>
                    <option value="checkbox" ${
                      field.type === "checkbox" ? "selected" : ""
                    }>Checkbox Group</option>
                </select>
            </div>
            
            <div class="mb-3">
                <label for="field-label" class="form-label">Label</label>
                <input type="text" class="form-control" id="field-label" value="${
                  field.label || ""
                }">
            </div>
            
            <div class="mb-3">
                <label for="field-id" class="form-label">Field ID</label>
                <input type="text" class="form-control" id="field-id" value="${
                  field.id || ""
                }"
                    ${state.isEditing ? "readonly" : ""}>
                <div class="form-text">Use descriptive IDs like "txtFullName" or "slGender"</div>
            </div>
            
            <div class="mb-3" id="placeholder-container" ${
              ["select", "radio", "checkbox"].includes(field.type)
                ? 'style="display:none"'
                : ""
            }>
                <label for="field-placeholder" class="form-label">Placeholder</label>
                <input type="text" class="form-control" id="field-placeholder" value="${
                  field.placeholder || ""
                }">
            </div>
            
            <div class="mb-3">
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" id="field-required" ${
                      field.required ? "checked" : ""
                    }>
                    <label class="form-check-label" for="field-required">Required Field</label>
                </div>
            </div>
            
            <div class="mb-3">
                <label for="field-label-position" class="form-label">Label Position</label>
                <select class="form-select" id="field-label-position">
                    <option value="left" ${
                      field.labelPosition === "left" || !field.labelPosition
                        ? "selected"
                        : ""
                    }>Left of field</option>
                    <option value="above" ${
                      field.labelPosition === "above" ? "selected" : ""
                    }>Above field</option>
                </select>
            </div>
        `;

    // Add event listener for field type change
    document
      .getElementById("field-type")
      .addEventListener("change", function () {
        const newType = this.value;

        // Show/hide placeholder based on field type
        document.getElementById("placeholder-container").style.display = [
          "select",
          "radio",
          "checkbox",
        ].includes(newType)
          ? "none"
          : "block";

        // Show/hide options tab based on field type
        document.getElementById("options-tab-item").style.display = [
          "select",
          "radio",
          "checkbox",
        ].includes(newType)
          ? ""
          : "none";

        // Update the current field
        state.currentField.type = newType;

        // Initialize options array if needed
        if (
          ["select", "radio", "checkbox"].includes(newType) &&
          !state.currentField.options
        ) {
          state.currentField.options = [
            { value: "option1", text: "Option 1" },
            { value: "option2", text: "Option 2" },
          ];
          renderOptionsTab();
        }

        // Update validation tab UI elements
        updateValidationUI(newType);
      });
  }

  /**
   * Render the validation tab content
   */
  function renderValidationTab() {
    const field = state.currentField;
    if (!field) return;

    // Ensure validation object exists
    if (!field.validation) {
      field.validation = {
        enabled: false,
        regex: "",
        errorMessage: "Please enter a valid value",
      };
    }

    const validationPane = document.getElementById("validation-pane");

    validationPane.innerHTML = `
            <div class="mb-3">
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" id="validation-enabled" ${
                      field.validation.enabled ? "checked" : ""
                    }>
                    <label class="form-check-label" for="validation-enabled">Enable Validation</label>
                </div>
            </div>
            
            <div id="validation-options" ${
              !field.validation.enabled ? 'style="display:none"' : ""
            }>
                <div class="mb-3">
                    <label for="validation-regex" class="form-label">Validation Pattern (Regex)</label>
                    <div class="input-group">
                        <input type="text" class="form-control" id="validation-regex" value="${
                          field.validation.regex || ""
                        }">
                        <button class="btn btn-outline-secondary" type="button" id="test-regex-btn">Test</button>
                    </div>
                    <div class="form-text">Example: ^[A-Z][a-z]* for capitalized words</div>
                </div>
                
                <div class="mb-3">
                    <label for="validation-error" class="form-label">Error Message</label>
                    <input type="text" class="form-control" id="validation-error" value="${
                      field.validation.errorMessage ||
                      "Please enter a valid value"
                    }">
                </div>
                
                <div class="mb-3">
                    <label class="form-label">Validation Presets</label>
                    <div class="d-flex flex-wrap gap-1">
                        <button class="btn btn-sm btn-outline-secondary validation-preset" 
                            data-regex="${state.validationPresets.name.regex}" 
                            data-message="${
                              state.validationPresets.name.message
                            }">
                            Name Format
                        </button>
                        <button class="btn btn-sm btn-outline-secondary validation-preset" 
                            data-regex="${state.validationPresets.phone.regex}" 
                            data-message="${
                              state.validationPresets.phone.message
                            }">
                            VN Phone
                        </button>
                        <button class="btn btn-sm btn-outline-secondary validation-preset" 
                            data-regex="${state.validationPresets.email.regex}" 
                            data-message="${
                              state.validationPresets.email.message
                            }">
                            Email
                        </button>
                        <button class="btn btn-sm btn-outline-secondary validation-preset" 
                            data-regex="${
                              state.validationPresets.numbers.regex
                            }" 
                            data-message="${
                              state.validationPresets.numbers.message
                            }">
                            Numbers Only
                        </button>
                    </div>
                </div>
                
                <!-- Type-specific validation options -->
                <div id="type-specific-validation">
                    <!-- This will be populated based on field type -->
                </div>
            </div>
        `;

    // Add event listeners for validation controls
    document
      .getElementById("validation-enabled")
      .addEventListener("change", function () {
        document.getElementById("validation-options").style.display = this
          .checked
          ? "block"
          : "none";
        state.currentField.validation.enabled = this.checked;
      });

    // Add event listeners for validation presets
    document.querySelectorAll(".validation-preset").forEach((btn) => {
      btn.addEventListener("click", function () {
        document.getElementById("validation-regex").value = this.dataset.regex;
        document.getElementById("validation-error").value =
          this.dataset.message;

        // Update the field
        state.currentField.validation.regex = this.dataset.regex;
        state.currentField.validation.errorMessage = this.dataset.message;
      });
    });

    // Test regex button
    document
      .getElementById("test-regex-btn")
      .addEventListener("click", function () {
        testRegexValidation();
      });

    // Populate type-specific validation options based on field type
    updateValidationUI(field.type);
  }

  /**
   * Update validation UI elements based on field type
   */
  function updateValidationUI(fieldType) {
    const typeSpecificContainer = document.getElementById(
      "type-specific-validation"
    );
    if (!typeSpecificContainer) return;

    const field = state.currentField;
    if (!field || !field.validation) return;

    let html = "";

    // Add min/max value for number fields
    if (fieldType === "number") {
      html += `
                <div class="row g-2 mb-3">
                    <div class="col-6">
                        <label for="validation-min-value" class="form-label">Min Value</label>
                        <input type="number" class="form-control" id="validation-min-value" 
                            value="${field.validation.minValue || ""}">
                    </div>
                    <div class="col-6">
                        <label for="validation-max-value" class="form-label">Max Value</label>
                        <input type="number" class="form-control" id="validation-max-value" 
                            value="${field.validation.maxValue || ""}">
                    </div>
                </div>
            `;
    }

    // Add min/max length for text fields
    if (["text", "email", "password", "textarea"].includes(fieldType)) {
      html += `
                <div class="row g-2 mb-3">
                    <div class="col-6">
                        <label for="validation-min-length" class="form-label">Min Length</label>
                        <input type="number" class="form-control" id="validation-min-length" 
                            value="${field.validation.minLength || ""}">
                    </div>
                    <div class="col-6">
                        <label for="validation-max-length" class="form-label">Max Length</label>
                        <input type="number" class="form-control" id="validation-max-length" 
                            value="${field.validation.maxLength || ""}">
                    </div>
                </div>
            `;
    }

    // Add date validation for date fields
    if (fieldType === "date") {
      html += `
                <div class="row g-2 mb-3">
                    <div class="col-6">
                        <label for="validation-min-date" class="form-label">Min Date</label>
                        <input type="date" class="form-control" id="validation-min-date" 
                            value="${field.validation.minDate || ""}">
                    </div>
                    <div class="col-6">
                        <label for="validation-max-date" class="form-label">Max Date</label>
                        <input type="date" class="form-control" id="validation-max-date" 
                            value="${field.validation.maxDate || ""}">
                    </div>
                </div>
            `;
    }

    typeSpecificContainer.innerHTML = html;
  }

  /**
   * Render the options tab content for select, radio, checkbox
   */
  function renderOptionsTab() {
    const field = state.currentField;
    if (!field) return;

    // Initialize options if needed
    if (!field.options) {
      field.options = [
        { value: "option1", text: "Option 1" },
        { value: "option2", text: "Option 2" },
      ];
    }

    const optionsPane = document.getElementById("options-pane");

    optionsPane.innerHTML = `
            <div class="mb-3">
                <label class="form-label d-flex justify-content-between align-items-center">
                    Options List
                    <button class="btn btn-sm btn-primary add-option-btn">
                        <i class="bi bi-plus-circle"></i> Add Option
                    </button>
                </label>
                
                <div id="options-container" class="border p-2 rounded">
                    <!-- Options will be listed here -->
                </div>
            </div>
            
            ${
              field.type === "radio" || field.type === "checkbox"
                ? `
                <div class="mb-3">
                    <label for="options-layout" class="form-label">Options Layout</label>
                    <select class="form-control" id="options-layout">
                        <option value="vertical" ${
                          field.optionsLayout === "vertical" ||
                          !field.optionsLayout
                            ? "selected"
                            : ""
                        }>Vertical (Stacked)</option>
                        <option value="horizontal" ${
                          field.optionsLayout === "horizontal" ? "selected" : ""
                        }>Horizontal (Inline)</option>
                    </select>
                </div>
            `
                : ""
            }
        `;

    // Render options list
    renderOptionsList();

    // Add event listeners
    optionsPane
      .querySelector(".add-option-btn")
      .addEventListener("click", function () {
        addOption();
      });

    if (field.type === "radio" || field.type === "checkbox") {
      document
        .getElementById("options-layout")
        .addEventListener("change", function () {
          field.optionsLayout = this.value;
        });
    }
  }

  /**
   * Render the options list
   */
  function renderOptionsList() {
    const field = state.currentField;
    if (!field || !field.options) return;

    const optionsContainer = document.getElementById("options-container");
    if (!optionsContainer) return;

    optionsContainer.innerHTML = "";

    // Create an item for each option
    field.options.forEach((option, index) => {
      const optionItem = document.createElement("div");
      optionItem.className = "option-item mb-2";
      optionItem.dataset.index = index;

      optionItem.innerHTML = `
                <div class="input-group input-group-sm">
                    <span class="input-group-text">${index + 1}</span>
                    <input type="text" class="form-control option-text" placeholder="Display Text" value="${
                      option.text || ""
                    }"
                        aria-label="Option text">
                    <input type="text" class="form-control option-value" placeholder="Value" value="${
                      option.value || ""
                    }"
                        aria-label="Option value">
                    <button class="btn btn-outline-danger delete-option-btn" type="button" title="Delete this option">
                        <i class="bi bi-trash"></i>
                    </button>
                </div>
            `;

      optionsContainer.appendChild(optionItem);

      // Add event listeners
      const textInput = optionItem.querySelector(".option-text");
      textInput.addEventListener("input", function () {
        field.options[index].text = this.value;
      });

      const valueInput = optionItem.querySelector(".option-value");
      valueInput.addEventListener("input", function () {
        field.options[index].value = this.value;
      });

      const deleteBtn = optionItem.querySelector(".delete-option-btn");
      deleteBtn.addEventListener("click", function () {
        deleteOption(index);
      });
    });
  }

  /**
   * Add a new option to the options list
   */
  function addOption() {
    const field = state.currentField;
    if (!field) return;

    if (!field.options) {
      field.options = [];
    }

    field.options.push({
      text: `Option ${field.options.length + 1}`,
      value: `option${field.options.length + 1}`,
    });

    renderOptionsList();
  }

  /**
   * Delete an option from the options list
   */
  function deleteOption(index) {
    const field = state.currentField;
    if (!field || !field.options) return;

    if (field.options.length <= 1) {
      alert("You need at least one option.");
      return;
    }

    field.options.splice(index, 1);
    renderOptionsList();
  }

  /**
   * Test the regex validation against a sample input
   */
  function testRegexValidation() {
    const regex = document.getElementById("validation-regex").value;
    if (!regex) {
      alert("Please enter a regex pattern to test.");
      return;
    }

    // Create a test input modal
    let testModal = document.getElementById("regex-test-modal");
    if (!testModal) {
      testModal = document.createElement("div");
      testModal.id = "regex-test-modal";
      testModal.className = "modal fade";
      testModal.innerHTML = `
                <div class="modal-dialog modal-dialog-centered">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">Test Validation Pattern</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <div class="mb-3">
                                <label for="regex-test-input" class="form-label">Enter test value:</label>
                                <input type="text" class="form-control" id="regex-test-input" 
                                    placeholder="Type to test against pattern...">
                                <div class="form-text">Pattern: <code id="regex-pattern"></code></div>
                                <div id="regex-result" class="mt-2"></div>
                            </div>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        </div>
                    </div>
                </div>
            `;
      document.body.appendChild(testModal);
    }

    // Show the pattern being tested
    testModal.querySelector("#regex-pattern").textContent = regex;

    // Clear any previous results
    testModal.querySelector("#regex-result").innerHTML = "";
    testModal.querySelector("#regex-test-input").value = "";

    // Add input event listener
    testModal
      .querySelector("#regex-test-input")
      .addEventListener("input", function () {
        const input = this.value;
        const regexPattern = new RegExp(regex);
        const isValid = regexPattern.test(input);

        const resultDiv = testModal.querySelector("#regex-result");
        resultDiv.innerHTML = isValid
          ? '<div class="alert alert-success mb-0">Pattern matched! ✓</div>'
          : '<div class="alert alert-danger mb-0">Pattern not matched! ✗</div>';
      });

    // Show the modal
    const bsModal = new bootstrap.Modal(testModal);
    bsModal.show();
  }

  /**
   * Update field preview
   */
  function updateFieldPreview() {
    const field = state.currentField;
    if (!field) return;

    const previewContainer = document.getElementById("field-preview");
    if (!previewContainer) return;

    let previewHtml = "";
    const isLeftLabel = field.labelPosition !== "above";
    const isValid = true; // Assume valid by default
    const errorMessage =
      field.validation && field.validation.errorMessage
        ? field.validation.errorMessage
        : "Invalid input";

    // Create different layouts based on labelPosition
    if (isLeftLabel) {
      previewHtml += '<div class="row mb-3">';
      previewHtml += `<label for="preview-field" class="col-md-3 col-form-label">${field.label}</label>`;
      previewHtml += '<div class="col-md-9">';
    } else {
      previewHtml += '<div class="mb-3">';
      previewHtml += `<label for="preview-field" class="form-label">${field.label}</label>`;
    }

    // Create input based on type
    switch (field.type) {
      case "text":
      case "email":
      case "password":
      case "number":
      case "date":
        previewHtml += `<input type="${field.type}" class="form-control ${
          !isValid ? "is-invalid" : ""
        }" 
                                id="preview-field" placeholder="${
                                  field.placeholder || ""
                                }" 
                                ${field.required ? "required" : ""}>`;
        break;

      case "textarea":
        previewHtml += `<textarea class="form-control ${
          !isValid ? "is-invalid" : ""
        }" 
                               id="preview-field" placeholder="${
                                 field.placeholder || ""
                               }" 
                               ${field.required ? "required" : ""}></textarea>`;
        break;

      case "select":
        previewHtml += `<select class="form-select ${
          !isValid ? "is-invalid" : ""
        }" 
                               id="preview-field" ${
                                 field.required ? "required" : ""
                               }>`;

        // Add options
        if (field.options && field.options.length > 0) {
          field.options.forEach((option) => {
            previewHtml += `<option value="${option.value}">${option.text}</option>`;
          });
        } else {
          previewHtml += '<option value="">No options</option>';
        }

        previewHtml += "</select>";
        break;

      case "radio":
        // Add radio options
        if (field.options && field.options.length > 0) {
          const optionsLayout =
            field.optionsLayout === "horizontal"
              ? "d-inline-block me-3"
              : "d-block";

          field.options.forEach((option, i) => {
            previewHtml += `<div class="form-check ${optionsLayout}">
                            <input class="form-check-input" type="radio" name="preview-radio" 
                                id="preview-radio-${i}" value="${
              option.value
            }" ${i === 0 ? "checked" : ""}>
                            <label class="form-check-label" for="preview-radio-${i}">${
              option.text
            }</label>
                        </div>`;
          });
        } else {
          previewHtml += '<div class="form-text">No options defined</div>';
        }
        break;

      case "checkbox":
        // Add checkbox options
        if (field.options && field.options.length > 0) {
          const optionsLayout =
            field.optionsLayout === "horizontal"
              ? "d-inline-block me-3"
              : "d-block";

          field.options.forEach((option, i) => {
            previewHtml += `<div class="form-check ${optionsLayout}">
                            <input class="form-check-input" type="checkbox" 
                                id="preview-check-${i}" value="${option.value}">
                            <label class="form-check-label" for="preview-check-${i}">${option.text}</label>
                        </div>`;
          });
        } else {
          previewHtml += '<div class="form-text">No options defined</div>';
        }
        break;
    }

    // Add error message if invalid
    if (!isValid) {
      previewHtml += `<div class="invalid-feedback">${errorMessage}</div>`;
    }

    // Close the containing divs
    if (isLeftLabel) {
      previewHtml += "</div></div>";
    } else {
      previewHtml += "</div>";
    }

    previewContainer.innerHTML = previewHtml;
  }

  /**
   * Save the current field
   */
  function saveField() {
    const field = state.currentField;
    if (!field) return;

    // Get values from the UI
    field.label = document.getElementById("field-label").value;
    field.id = document.getElementById("field-id").value;
    field.required = document.getElementById("field-required").checked;
    field.labelPosition = document.getElementById("field-label-position").value;

    // Get placeholder if applicable
    if (!["select", "radio", "checkbox"].includes(field.type)) {
      field.placeholder = document.getElementById("field-placeholder").value;
    }

    // Get validation settings
    field.validation.enabled =
      document.getElementById("validation-enabled").checked;
    if (field.validation.enabled) {
      field.validation.regex =
        document.getElementById("validation-regex").value;
      field.validation.errorMessage =
        document.getElementById("validation-error").value;

      // Get type-specific validation
      if (field.type === "number") {
        field.validation.minValue = document.getElementById(
          "validation-min-value"
        ).value;
        field.validation.maxValue = document.getElementById(
          "validation-max-value"
        ).value;
      }

      if (["text", "email", "password", "textarea"].includes(field.type)) {
        field.validation.minLength = document.getElementById(
          "validation-min-length"
        ).value;
        field.validation.maxLength = document.getElementById(
          "validation-max-length"
        ).value;
      }

      if (field.type === "date") {
        field.validation.minDate = document.getElementById(
          "validation-min-date"
        ).value;
        field.validation.maxDate = document.getElementById(
          "validation-max-date"
        ).value;
      }
    }

    // Validate the field
    const validationResult = validateFieldProperties(field);
    if (!validationResult.isValid) {
      alert(validationResult.message);
      return;
    }

    // Add or update the field in the component
    if (!state.modalComponent.formFields) {
      state.modalComponent.formFields = [];
    }

    if (state.isEditing) {
      // Update existing field
      const index = state.modalComponent.formFields.findIndex(
        (f) => f.id === field.id
      );
      if (index !== -1) {
        state.modalComponent.formFields[index] = field;
      }
    } else {
      // Add new field
      state.modalComponent.formFields.push(field);
    }

    // Update the fields list
    renderFieldsList();

    // Hide the editor
    hideFieldEditor();

    // Notify model updated
    notifyModelUpdated();
  }

  /**
   * Validate field properties before saving
   */
  function validateFieldProperties(field) {
    if (!field.label) {
      return { isValid: false, message: "Field label is required" };
    }

    if (!field.id) {
      return { isValid: false, message: "Field ID is required" };
    }

    // Check for duplicate IDs (only for new fields)
    if (!state.isEditing) {
      const existingField = state.modalComponent.formFields?.find(
        (f) => f.id === field.id
      );
      if (existingField) {
        return {
          isValid: false,
          message: "Field ID already exists. Please use a unique ID.",
        };
      }
    }

    // For select, radio, checkbox, check that options exist
    if (["select", "radio", "checkbox"].includes(field.type)) {
      if (!field.options || field.options.length === 0) {
        return {
          isValid: false,
          message: "At least one option is required for this field type",
        };
      }
    }

    // If validation is enabled, check for regex if it's specified
    if (
      field.validation &&
      field.validation.enabled &&
      field.validation.regex
    ) {
      try {
        // Test if the regex is valid
        new RegExp(field.validation.regex);
      } catch (e) {
        return {
          isValid: false,
          message: "Invalid regular expression: " + e.message,
        };
      }
    }

    return { isValid: true };
  }

  /**
   * Cancel editing and return to the fields list
   */
  function cancelEditing() {
    hideFieldEditor();
  }

  /**
   * Generate a unique field ID
   */
  function generateFieldId() {
    const prefix = "txt";
    return prefix + Date.now();
  }

  /**
   * Notify that the model has been updated
   */
  function notifyModelUpdated() {
    document.dispatchEvent(new CustomEvent("modelUpdated"));
  }

  // Return public API
  return {
    init,
    openFormEditor,
    createNewField,
    editField,
    deleteField,
  };
})();

// Initialize when DOM is ready
document.addEventListener("DOMContentLoaded", ModalFormEditor.init);
