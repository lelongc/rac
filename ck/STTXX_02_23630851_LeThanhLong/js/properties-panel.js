/**
 * Properties Panel Module for GFree English Course Web Builder
 * Manages the display and editing of component properties
 */

(function () {
  // Current state of the properties panel
  const state = {
    selectedComponent: null,
    currentEditingField: null, // For modal form field editing
    isFieldEditorOpen: false,
  };

  // Cache DOM elements
  const elements = {};

  /**
   * Initialize the properties panel
   */
  function init() {
    // Cache DOM elements
    elements.panel = document.getElementById("properties-panel");
    elements.noSelectionMsg = elements.panel.querySelector(
      ".no-selection-message"
    );
    elements.propertiesContainer = elements.panel.querySelector(
      ".component-properties"
    );
    elements.specificPropsContainer = document.getElementById(
      "specific-props-container"
    );

    // General property inputs
    elements.idInput = document.getElementById("prop-id");
    elements.classInput = document.getElementById("prop-class");
    elements.colorInput = document.getElementById("prop-color");
    elements.bgColorInput = document.getElementById("prop-bg-color");

    // Set up event listeners
    setupEventListeners();

    // Listen for component selection events from renderer
    document.addEventListener("componentSelected", handleComponentSelected);
  }

  /**
   * Set up event listeners for the properties panel
   */
  function setupEventListeners() {
    // Listen for changes to general properties
    elements.idInput.addEventListener("change", handlePropertyChange);
    elements.classInput.addEventListener("change", handlePropertyChange);
    elements.colorInput.addEventListener("change", handlePropertyChange);
    elements.bgColorInput.addEventListener("change", handlePropertyChange);

    // Listen for changes in the specific properties container using event delegation
    elements.specificPropsContainer.addEventListener(
      "change",
      handleSpecificPropertyChange
    );

    // Listen for clicks in the specific properties container (for buttons)
    elements.specificPropsContainer.addEventListener(
      "click",
      handleSpecificPropertyClick
    );
  }

  /**
   * Handle component selection
   * @param {CustomEvent} e - The componentSelected event
   */
  function handleComponentSelected(e) {
    const componentId = e.detail.componentId;

    if (!componentId) {
      hidePropertyPanel();
      state.selectedComponent = null;
      return;
    }

    // Get component from model
    const component = window.pageModelManager.getComponentById(componentId);
    if (!component) {
      hidePropertyPanel();
      state.selectedComponent = null;
      return;
    }

    // Update state
    state.selectedComponent = component;

    // Show properties for this component
    showComponentProperties(component);
  }

  /**
   * Show properties for a component
   * @param {Object} component - The component to show properties for
   */
  function showComponentProperties(component) {
    // Hide "no selection" message and show properties form
    elements.noSelectionMsg.style.display = "none";
    elements.propertiesContainer.style.display = "block";

    // Set general properties
    elements.idInput.value = component.id;
    elements.classInput.value = component.classes
      ? component.classes.join(" ")
      : "";
    elements.colorInput.value = component.styles.color || "#000000";
    elements.bgColorInput.value = component.styles.backgroundColor || "#ffffff";

    // Set component-specific properties
    renderSpecificProperties(component);
  }

  /**
   * Hide the property panel
   */
  function hidePropertyPanel() {
    elements.noSelectionMsg.style.display = "block";
    elements.propertiesContainer.style.display = "none";
    elements.specificPropsContainer.innerHTML = "";
  }

  /**
   * Render specific properties for a component
   * @param {Object} component - The component to render properties for
   */
  function renderSpecificProperties(component) {
    // Get the HTML for component-specific properties
    const specificPropsHtml = component.getPropertyControls();

    // Set the HTML content
    elements.specificPropsContainer.innerHTML = specificPropsHtml;

    // For modal component, we need to add additional functionality
    if (component.type === "modal") {
      setupModalFieldEditor(component);
    }
    // For navigation component, add links management
    else if (component.type === "nav") {
      setupNavigationLinksEditor(component);
    }
    // For table component, add columns management
    else if (component.type === "table") {
      setupTableColumnsEditor(component);
    }
  }

  /**
   * Handle changes to general properties
   */
  function handlePropertyChange(e) {
    if (!state.selectedComponent) return;

    const input = e.target;
    let property, value;

    // Determine property and value based on input
    switch (input.id) {
      case "prop-id":
        property = "id";
        value = input.value;
        break;

      case "prop-class":
        property = "classes";
        value = input.value.split(" ").filter((c) => c.trim() !== "");
        break;

      case "prop-color":
        property = "styles.color";
        value = input.value;
        break;

      case "prop-bg-color":
        property = "styles.backgroundColor";
        value = input.value;
        break;
    }

    if (property) {
      updateComponentProperty(property, value);
    }
  }

  /**
   * Handle changes to component-specific properties
   */
  function handleSpecificPropertyChange(e) {
    if (!state.selectedComponent) return;

    const input = e.target;
    const property = input.getAttribute("data-property");

    if (!property) return;

    let value;
    if (input.type === "checkbox") {
      value = input.checked;
    } else {
      value = input.value;
    }

    updateComponentProperty(property, value);
  }

  /**
   * Handle clicks in the specific properties container (for buttons)
   */
  function handleSpecificPropertyClick(e) {
    if (!state.selectedComponent) return;

    // Check for special buttons
    if (e.target.closest("#add-form-field-btn")) {
      openFieldEditor();
    } else if (e.target.closest("#save-form-field-btn")) {
      saveCurrentField();
    } else if (e.target.closest("#cancel-field-editor-btn")) {
      closeFieldEditor();
    } else if (e.target.closest(".edit-form-field-btn")) {
      const fieldId = e.target
        .closest(".edit-form-field-btn")
        .getAttribute("data-field-id");
      editField(fieldId);
    } else if (e.target.closest(".delete-form-field-btn")) {
      const fieldId = e.target
        .closest(".delete-form-field-btn")
        .getAttribute("data-field-id");
      deleteField(fieldId);
    }
    // Navigation link management
    else if (e.target.closest("#add-nav-link-btn")) {
      addNavigationLink(state.selectedComponent);
    } else if (e.target.closest(".edit-nav-link-btn")) {
      const index = parseInt(
        e.target.closest(".edit-nav-link-btn").getAttribute("data-index"),
        10
      );
      editNavigationLink(state.selectedComponent, index);
    } else if (e.target.closest(".delete-nav-link-btn")) {
      const index = parseInt(
        e.target.closest(".delete-nav-link-btn").getAttribute("data-index"),
        10
      );
      deleteNavigationLink(state.selectedComponent, index);
    }
    // Table column management
    else if (e.target.closest("#add-table-column-btn")) {
      addTableColumn(state.selectedComponent);
    } else if (e.target.closest(".edit-column-btn")) {
      const index = parseInt(
        e.target.closest(".edit-column-btn").getAttribute("data-index"),
        10
      );
      editTableColumn(state.selectedComponent, index);
    } else if (e.target.closest(".delete-column-btn")) {
      const index = parseInt(
        e.target.closest(".delete-column-btn").getAttribute("data-index"),
        10
      );
      deleteTableColumn(state.selectedComponent, index);
    }
    // Handle other buttons for different component types as needed
  }

  /**
   * Update a component property and notify
   * @param {string} property - The property path (can be nested, e.g., 'styles.color')
   * @param {any} value - The new value
   */
  function updateComponentProperty(property, value) {
    if (!state.selectedComponent) return;

    const componentId = state.selectedComponent.id;

    // For nested properties like 'styles.color'
    if (property.includes(".")) {
      const [parent, child] = property.split(".");

      // Create a copy of the parent object
      const parentObj = { ...state.selectedComponent[parent] };
      parentObj[child] = value;

      // Update with the new parent object
      window.pageModelManager.updateComponent(componentId, {
        [parent]: parentObj,
      });
    } else {
      // For direct properties
      window.pageModelManager.updateComponent(componentId, {
        [property]: value,
      });
    }

    // Notify that the model has been updated
    notifyModelUpdated();
  }

  // === Modal Form Field Editing ===

  /**
   * Set up the modal field editor interface
   */
  function setupModalFieldEditor(component) {
    if (!component || component.type !== "modal") return;

    // Add the "Manage Form Fields" section to the specific properties
    const fieldListContainer = document.createElement("div");
    fieldListContainer.className = "mt-3";
    fieldListContainer.innerHTML = `
            <h6 class="border-bottom pb-2">Form Fields</h6>
            
            <div id="form-fields-list" class="mb-2">
                ${renderFormFieldsList(component)}
            </div>
            
            <button id="add-form-field-btn" class="btn btn-sm btn-primary w-100">
                <i class="bi bi-plus-circle me-1"></i> Add New Field
            </button>
            
            <div id="field-editor" class="mt-3 border rounded p-2" style="display: none;">
                <!-- Field editor will be rendered here -->
            </div>
        `;

    elements.specificPropsContainer.appendChild(fieldListContainer);
  }

  /**
   * Render the list of form fields for the modal component
   */
  function renderFormFieldsList(component) {
    if (!component.formFields || component.formFields.length === 0) {
      return '<p class="text-muted small">No form fields defined</p>';
    }

    return `
            <div class="list-group">
                ${component.formFields
                  .map(
                    (field) => `
                    <div class="list-group-item list-group-item-action d-flex justify-content-between align-items-center py-2">
                        <div>
                            <span class="fw-bold">${
                              field.label || "Untitled"
                            }</span>
                            <br>
                            <small class="text-muted">${field.type || "text"} ${
                      field.id ? " - #" + field.id : ""
                    }</small>
                        </div>
                        <div>
                            <button class="btn btn-sm btn-outline-primary edit-form-field-btn" data-field-id="${
                              field.id
                            }">
                                <i class="bi bi-pencil"></i>
                            </button>
                            <button class="btn btn-sm btn-outline-danger delete-form-field-btn" data-field-id="${
                              field.id
                            }">
                                <i class="bi bi-trash"></i>
                            </button>
                        </div>
                    </div>
                `
                  )
                  .join("")}
            </div>
        `;
  }

  /**
   * Open the field editor to add a new form field
   */
  function openFieldEditor() {
    if (!state.selectedComponent || state.selectedComponent.type !== "modal")
      return;

    // Create a new field template
    state.currentEditingField = {
      id: "field_" + Date.now(),
      type: "text",
      label: "New Field",
      placeholder: "",
      validation: false,
      required: false,
    };

    // Show the field editor
    renderFieldEditor();
    state.isFieldEditorOpen = true;
  }

  /**
   * Edit an existing form field
   */
  function editField(fieldId) {
    if (!state.selectedComponent || state.selectedComponent.type !== "modal")
      return;

    // Find the field in the component's formFields
    const field = state.selectedComponent.formFields.find(
      (f) => f.id === fieldId
    );

    if (!field) {
      console.error(`Field with id ${fieldId} not found`);
      return;
    }

    // Set the current editing field
    state.currentEditingField = { ...field }; // Clone to avoid direct modification

    // Show the field editor
    renderFieldEditor();
    state.isFieldEditorOpen = true;
  }

  /**
   * Render the field editor interface
   */
  function renderFieldEditor() {
    const field = state.currentEditingField;
    if (!field) return;

    const fieldEditor = document.getElementById("field-editor");
    if (!fieldEditor) return;

    // Initialize default values if missing
    field.labelPosition = field.labelPosition || "left";
    field.required = field.required !== undefined ? field.required : false;
    field.placeholder = field.placeholder || "";
    field.validation = field.validation || {};
    field.options = field.options || [];
    field.optionsLayout = field.optionsLayout || "vertical";

    fieldEditor.style.display = "block";
    fieldEditor.innerHTML = `
      <div class="border-bottom pb-2 mb-3 d-flex justify-content-between align-items-center">
        <h6 class="mb-0">${field.id ? "Edit Field" : "Add New Field"}</h6>
        <div>
          <button id="field-help-btn" class="btn btn-sm btn-outline-secondary me-2" title="Help">
            <i class="bi bi-question-circle"></i>
          </button>
          <button id="field-preview-btn" class="btn btn-sm btn-outline-primary" title="Preview">
            <i class="bi bi-eye"></i> Preview
          </button>
        </div>
      </div>
      
      <ul class="nav nav-tabs mb-3" id="fieldEditorTabs" role="tablist">
        <li class="nav-item" role="presentation">
          <button class="nav-link active" id="basic-tab" data-bs-toggle="tab" data-bs-target="#basic-pane" 
            type="button" role="tab" aria-controls="basic-pane" aria-selected="true">Basic</button>
        </li>
        <li class="nav-item" role="presentation">
          <button class="nav-link" id="validation-tab" data-bs-toggle="tab" data-bs-target="#validation-pane" 
            type="button" role="tab" aria-controls="validation-pane" aria-selected="false">Validation</button>
        </li>
        <li class="nav-item" id="options-tab-item" style="${
          ["select", "radio", "checkbox"].includes(field.type)
            ? ""
            : "display: none;"
        }">
          <button class="nav-link" id="options-tab" data-bs-toggle="tab" data-bs-target="#options-pane" 
            type="button" role="tab" aria-controls="options-pane" aria-selected="false">Options</button>
        </li>
      </ul>
      
      <div class="tab-content" id="fieldEditorTabContent">
        <!-- Basic Properties Tab -->
        <div class="tab-pane fade show active" id="basic-pane" role="tabpanel" aria-labelledby="basic-tab">
          <div class="mb-2">
            <label for="field-label" class="form-label small">Label Text</label>
            <input type="text" class="form-control form-control-sm" id="field-label" 
                value="${field.label || ""}" data-field-prop="label">
          </div>
          
          <div class="mb-2">
            <label for="field-id" class="form-label small">Field ID</label>
            <input type="text" class="form-control form-control-sm" id="field-id" 
                value="${field.id || ""}" data-field-prop="id">
            <div class="form-text small">Use descriptive IDs like "txtFullName" or "slGender"</div>
          </div>
          
          <div class="mb-2">
            <label for="field-type" class="form-label small">Field Type</label>
            <select class="form-select form-select-sm" id="field-type" data-field-prop="type">
              <option value="text" ${
                field.type === "text" ? "selected" : ""
              }>Text</option>
              <option value="email" ${
                field.type === "email" ? "selected" : ""
              }>Email</option>
              <option value="number" ${
                field.type === "number" ? "selected" : ""
              }>Number</option>
              <option value="date" ${
                field.type === "date" ? "selected" : ""
              }>Date</option>
              <option value="password" ${
                field.type === "password" ? "selected" : ""
              }>Password</option>
              <option value="textarea" ${
                field.type === "textarea" ? "selected" : ""
              }>Text Area</option>
              <option value="select" ${
                field.type === "select" ? "selected" : ""
              }>Select Dropdown</option>
              <option value="checkbox" ${
                field.type === "checkbox" ? "selected" : ""
              }>Checkbox Group</option>
              <option value="radio" ${
                field.type === "radio" ? "selected" : ""
              }>Radio Group</option>
            </select>
          </div>
          
          <div class="mb-2" id="placeholder-container" ${
            ["select", "checkbox", "radio"].includes(field.type)
              ? 'style="display:none;"'
              : ""
          }>
            <label for="field-placeholder" class="form-label small">Placeholder</label>
            <input type="text" class="form-control form-control-sm" id="field-placeholder" 
                value="${
                  field.placeholder || ""
                }" data-field-prop="placeholder">
          </div>
          
          <div class="mb-2">
            <label for="field-label-position" class="form-label small">Label Position</label>
            <select class="form-select form-select-sm" id="field-label-position" data-field-prop="labelPosition">
              <option value="left" ${
                field.labelPosition === "left" ? "selected" : ""
              }>Left of field</option>
              <option value="above" ${
                field.labelPosition === "above" ? "selected" : ""
              }>Above field</option>
            </select>
          </div>
          
          <div class="mb-2 form-check">
            <input type="checkbox" class="form-check-input" id="field-required" 
                ${field.required ? "checked" : ""} data-field-prop="required">
            <label class="form-check-label small" for="field-required">Required Field</label>
          </div>
        </div>
        
        <!-- Validation Tab -->
        <div class="tab-pane fade" id="validation-pane" role="tabpanel" aria-labelledby="validation-tab">
          <div class="mb-2 form-check">
            <input type="checkbox" class="form-check-input" id="field-enable-validation" 
                ${
                  field.validation.enabled ? "checked" : ""
                } data-validation-prop="enabled">
            <label class="form-check-label small" for="field-enable-validation">Enable Validation</label>
          </div>
          
          <div id="validation-options" ${
            !field.validation.enabled ? 'style="display:none;"' : ""
          }>
            <div class="mb-2">
              <label for="validation-regex" class="form-label small">Validation Pattern (Regex)</label>
              <input type="text" class="form-control form-control-sm" id="validation-regex" 
                  value="${
                    field.validation.regex || ""
                  }" data-validation-prop="regex">
              <div class="form-text small">Example: ^[A-Z][a-z]* for capitalized words</div>
            </div>
            
            <div class="mb-2">
              <label for="validation-error-message" class="form-label small">Error Message</label>
              <input type="text" class="form-control form-control-sm" id="validation-error-message" 
                  value="${
                    field.validation.errorMessage || ""
                  }" data-validation-prop="errorMessage">
            </div>
            
            <div class="mb-2">
              <label class="form-label small mb-2">Validation Presets</label>
              <div class="d-flex flex-wrap gap-1">
                <button class="btn btn-sm btn-outline-secondary validation-preset" 
                  data-regex="^[A-Z][a-z]*(\s+[A-Z][a-z]*)+$" 
                  data-message="Each word must start with uppercase letter">
                  Name Format
                </button>
                <button class="btn btn-sm btn-outline-secondary validation-preset" 
                  data-regex="^(09|03|08)\d{8}$" 
                  data-message="Phone must have 10 digits and start with 09, 03 or 08">
                  VN Phone
                </button>
                <button class="btn btn-sm btn-outline-secondary validation-preset" 
                  data-regex="^\S+@\S+\.\S{2,}$" 
                  data-message="Please enter a valid email address">
                  Email
                </button>
                <button class="btn btn-sm btn-outline-secondary validation-preset" 
                  data-regex="^\d+$" 
                  data-message="Please enter only numbers">
                  Numbers Only
                </button>
              </div>
            </div>
            
            <div class="row g-2 mb-2" id="number-range-container" style="${
              field.type === "number" ? "" : "display:none;"
            }">
              <div class="col-6">
                <label for="validation-min-value" class="form-label small">Min Value</label>
                <input type="number" class="form-control form-control-sm" id="validation-min-value" 
                    value="${
                      field.validation.minValue || ""
                    }" data-validation-prop="minValue">
              </div>
              <div class="col-6">
                <label for="validation-max-value" class="form-label small">Max Value</label>
                <input type="number" class="form-control form-control-sm" id="validation-max-value" 
                    value="${
                      field.validation.maxValue || ""
                    }" data-validation-prop="maxValue">
              </div>
            </div>
            
            <div class="row g-2 mb-2" id="text-length-container" style="${
              ["text", "email", "password", "textarea"].includes(field.type)
                ? ""
                : "display:none;"
            }">
              <div class="col-6">
                <label for="validation-min-length" class="form-label small">Min Length</label>
                <input type="number" class="form-control form-control-sm" id="validation-min-length" 
                    value="${
                      field.validation.minLength || ""
                    }" data-validation-prop="minLength">
              </div>
              <div class="col-6">
                <label for="validation-max-length" class="form-label small">Max Length</label>
                <input type="number" class="form-control form-control-sm" id="validation-max-length" 
                    value="${
                      field.validation.maxLength || ""
                    }" data-validation-prop="maxLength">
              </div>
            </div>
          </div>
        </div>
        
        <!-- Options Tab (for select, radio, checkbox) -->
        <div class="tab-pane fade" id="options-pane" role="tabpanel" aria-labelledby="options-tab">
          <div class="mb-2">
            <label class="form-label small d-flex justify-content-between align-items-center">
              Options List
              <button id="add-option-btn" class="btn btn-sm btn-primary">
                <i class="bi bi-plus-circle"></i> Add Option
              </button>
            </label>
            
            <div id="options-container" class="border rounded p-2 mb-2">
              ${renderFieldOptions(field)}
            </div>
          </div>
          
          <div class="mb-2" id="options-layout-container" style="${
            ["radio", "checkbox"].includes(field.type) ? "" : "display:none;"
          }">
            <label for="options-layout" class="form-label small">Options Layout</label>
            <select class="form-select form-select-sm" id="options-layout" data-field-prop="optionsLayout">
              <option value="vertical" ${
                field.optionsLayout === "vertical" ? "selected" : ""
              }>Vertical (Stacked)</option>
              <option value="horizontal" ${
                field.optionsLayout === "horizontal" ? "selected" : ""
              }>Horizontal (Inline)</option>
            </select>
          </div>
        </div>
      </div>
      
      <!-- Preview Area -->
      <div id="field-preview-area" class="mt-3 p-2 border rounded" style="display:none;">
        <h6 class="border-bottom pb-2 mb-2">Field Preview</h6>
        <div id="field-preview-content"></div>
      </div>
      
      <div class="d-flex justify-content-end mt-3">
        <button id="cancel-field-editor-btn" class="btn btn-sm btn-outline-secondary me-2">Cancel</button>
        <button id="save-form-field-btn" class="btn btn-sm btn-primary">Save Field</button>
      </div>
    `;

    // Add event listeners for the field editor inputs
    setupFieldEditorEventListeners(fieldEditor, field);
  }

  /**
   * Render the options list for select, radio, checkbox fields
   */
  function renderFieldOptions(field) {
    if (
      !field.options ||
      !Array.isArray(field.options) ||
      field.options.length === 0
    ) {
      return `<p class="text-muted mb-0 small">No options defined. Click "Add Option" to add some.</p>`;
    }

    return `
      <div class="options-list">
        ${field.options
          .map(
            (option, index) => `
          <div class="option-item d-flex align-items-center mb-1" data-index="${index}">
            <div class="flex-grow-1 me-1">
              <div class="input-group input-group-sm">
                <input type="text" class="form-control option-text" placeholder="Display Text" 
                  value="${option.text || ""}" aria-label="Option text">
                <input type="text" class="form-control option-value" placeholder="Value" 
                  value="${option.value || ""}" aria-label="Option value">
                <button class="btn btn-outline-danger delete-option-btn" type="button">
                  <i class="bi bi-trash"></i>
                </button>
              </div>
            </div>
          </div>
        `
          )
          .join("")}
      </div>
    `;
  }

  /**
   * Setup event listeners for the field editor
   */
  function setupFieldEditorEventListeners(fieldEditor, field) {
    // Basic input change listeners
    const basicInputs = fieldEditor.querySelectorAll("[data-field-prop]");
    basicInputs.forEach((input) => {
      input.addEventListener("change", function () {
        const prop = this.getAttribute("data-field-prop");
        let value;

        if (this.type === "checkbox") {
          value = this.checked;
        } else {
          value = this.value;
        }

        if (field) {
          field[prop] = value;

          // Special handling for type changes
          if (prop === "type") {
            // Show/hide placeholder field based on type
            const placeholderContainer = document.getElementById(
              "placeholder-container"
            );
            placeholderContainer.style.display = [
              "select",
              "checkbox",
              "radio",
            ].includes(value)
              ? "none"
              : "";

            // Show/hide options tab based on type
            const optionsTabItem = document.getElementById("options-tab-item");
            optionsTabItem.style.display = [
              "select",
              "radio",
              "checkbox",
            ].includes(value)
              ? ""
              : "none";

            // Show/hide validation fields based on type
            updateValidationFieldsVisibility(value);

            // Show/hide options layout based on type
            const optionsLayoutContainer = document.getElementById(
              "options-layout-container"
            );
            if (optionsLayoutContainer) {
              optionsLayoutContainer.style.display = [
                "radio",
                "checkbox",
              ].includes(value)
                ? ""
                : "none";
            }

            // Initialize options array if switching to a type that needs options
            if (
              ["select", "radio", "checkbox"].includes(value) &&
              (!field.options || !Array.isArray(field.options))
            ) {
              field.options = [];
            }
          }

          // Update preview if shown
          const previewArea = document.getElementById("field-preview-area");
          if (previewArea && previewArea.style.display !== "none") {
            updateFieldPreview(field);
          }
        }
      });
    });

    // Validation inputs
    const validationInputs = fieldEditor.querySelectorAll(
      "[data-validation-prop]"
    );
    validationInputs.forEach((input) => {
      input.addEventListener("change", function () {
        const prop = this.getAttribute("data-validation-prop");
        let value;

        if (this.type === "checkbox") {
          value = this.checked;
        } else {
          value = this.value;
        }

        if (field) {
          // Initialize validation object if it doesn't exist
          if (!field.validation) {
            field.validation = {};
          }

          field.validation[prop] = value;

          // Special handling for 'enabled' property
          if (prop === "enabled") {
            const validationOptions =
              document.getElementById("validation-options");
            validationOptions.style.display = value ? "" : "none";
          }

          // Update preview if shown
          const previewArea = document.getElementById("field-preview-area");
          if (previewArea && previewArea.style.display !== "none") {
            updateFieldPreview(field);
          }
        }
      });
    });

    // Validation preset buttons
    const presetButtons = fieldEditor.querySelectorAll(".validation-preset");
    presetButtons.forEach((button) => {
      button.addEventListener("click", function () {
        const regex = this.getAttribute("data-regex");
        const message = this.getAttribute("data-message");

        if (field && field.validation) {
          document.getElementById("validation-regex").value = regex;
          document.getElementById("validation-error-message").value = message;

          field.validation.regex = regex;
          field.validation.errorMessage = message;
        }
      });
    });

    // Toggle validation options visibility
    const enableValidationCheckbox = document.getElementById(
      "field-enable-validation"
    );
    enableValidationCheckbox.addEventListener("change", function () {
      const validationOptions = document.getElementById("validation-options");
      validationOptions.style.display = this.checked ? "" : "none";
    });

    // Field type specific visibility updates
    updateValidationFieldsVisibility(field.type);

    // Toggle field preview
    const previewButton = document.getElementById("field-preview-btn");
    previewButton.addEventListener("click", function () {
      const previewArea = document.getElementById("field-preview-area");
      const isVisible = previewArea.style.display !== "none";

      previewArea.style.display = isVisible ? "none" : "";
      this.innerHTML = isVisible
        ? '<i class="bi bi-eye"></i> Preview'
        : '<i class="bi bi-eye-slash"></i> Hide Preview';

      if (!isVisible) {
        updateFieldPreview(field);
      }
    });

    // Add new option button
    const addOptionBtn = document.getElementById("add-option-btn");
    if (addOptionBtn) {
      addOptionBtn.addEventListener("click", function () {
        if (!field.options) {
          field.options = [];
        }

        field.options.push({
          text: "New Option",
          value: `option${field.options.length + 1}`,
        });

        // Redraw options list
        document.getElementById("options-container").innerHTML =
          renderFieldOptions(field);

        // Setup option item event listeners again
        setupOptionsEventListeners(field);
      });
    }

    // Setup option item event listeners
    setupOptionsEventListeners(field);

    // Help button
    const helpBtn = document.getElementById("field-help-btn");
    helpBtn.addEventListener("click", function () {
      showFieldEditorHelp();
    });
  }

  /**
   * Setup event listeners for option items
   */
  function setupOptionsEventListeners(field) {
    // Get all delete option buttons
    const deleteOptionBtns = document.querySelectorAll(".delete-option-btn");
    deleteOptionBtns.forEach((button) => {
      button.addEventListener("click", function () {
        const optionItem = this.closest(".option-item");
        const index = parseInt(optionItem.getAttribute("data-index"), 10);

        if (field.options && index >= 0 && index < field.options.length) {
          field.options.splice(index, 1);

          // Redraw options list
          document.getElementById("options-container").innerHTML =
            renderFieldOptions(field);

          // Setup option item event listeners again
          setupOptionsEventListeners(field);
        }
      });
    });

    // Get all option text and value inputs
    const optionInputs = document.querySelectorAll(
      ".option-text, .option-value"
    );
    optionInputs.forEach((input) => {
      input.addEventListener("change", function () {
        const optionItem = this.closest(".option-item");
        const index = parseInt(optionItem.getAttribute("data-index"), 10);
        const isText = this.classList.contains("option-text");

        if (field.options && index >= 0 && index < field.options.length) {
          const prop = isText ? "text" : "value";
          field.options[index][prop] = this.value;
        }
      });
    });
  }

  /**
   * Update validation fields visibility based on field type
   */
  function updateValidationFieldsVisibility(fieldType) {
    const numberRangeContainer = document.getElementById(
      "number-range-container"
    );
    const textLengthContainer = document.getElementById(
      "text-length-container"
    );

    if (numberRangeContainer) {
      numberRangeContainer.style.display = fieldType === "number" ? "" : "none";
    }

    if (textLengthContainer) {
      textLengthContainer.style.display = [
        "text",
        "email",
        "password",
        "textarea",
      ].includes(fieldType)
        ? ""
        : "none";
    }
  }

  /**
   * Update the field preview area with current field settings
   */
  function updateFieldPreview(field) {
    const previewContent = document.getElementById("field-preview-content");
    if (!previewContent || !field) return;

    let html = "";
    const labelHtml = `<label for="preview-${field.id}" class="form-label">${
      field.label || "Field Label"
    }</label>`;

    // Create different layouts based on labelPosition
    const isLeftLabel = field.labelPosition === "left";

    if (isLeftLabel) {
      html += '<div class="row mb-2">';
      html += '<div class="col-4 text-end">' + labelHtml + "</div>";
      html += '<div class="col-8">';
    } else {
      html += '<div class="mb-2">';
      html += labelHtml;
    }

    // Create input based on type
    switch (field.type) {
      case "text":
      case "email":
      case "number":
      case "date":
      case "password":
        html += `<input type="${field.type}" class="form-control" id="preview-${
          field.id
        }" 
                 placeholder="${field.placeholder || ""}" ${
          field.required ? "required" : ""
        }>`;
        break;

      case "textarea":
        html += `<textarea class="form-control" id="preview-${field.id}" 
                 placeholder="${field.placeholder || ""}" ${
          field.required ? "required" : ""
        }></textarea>`;
        break;

      case "select":
        html += `<select class="form-select" id="preview-${field.id}" ${
          field.required ? "required" : ""
        }>`;
        if (field.options && field.options.length) {
          field.options.forEach((option) => {
            html += `<option value="${option.value || ""}">${
              option.text || ""
            }</option>`;
          });
        } else {
          html += "<option>No options defined</option>";
        }
        html += "</select>";
        break;

      case "radio":
        if (field.options && field.options.length) {
          const isInline = field.optionsLayout === "horizontal";

          field.options.forEach((option, index) => {
            html += `<div class="form-check ${
              isInline ? "form-check-inline" : ""
            }">
                      <input class="form-check-input" type="radio" name="preview-${
                        field.id
                      }" 
                       id="preview-${field.id}-${index}" value="${
              option.value || ""
            }" ${index === 0 ? "checked" : ""}>
                      <label class="form-check-label" for="preview-${
                        field.id
                      }-${index}">${option.text || ""}</label>
                     </div>`;
          });
        } else {
          html += '<p class="text-muted">No radio options defined</p>';
        }
        break;

      case "checkbox":
        if (field.options && field.options.length) {
          const isInline = field.optionsLayout === "horizontal";

          field.options.forEach((option, index) => {
            html += `<div class="form-check ${
              isInline ? "form-check-inline" : ""
            }">
                      <input class="form-check-input" type="checkbox" 
                       id="preview-${field.id}-${index}" value="${
              option.value || ""
            }">
                      <label class="form-check-label" for="preview-${
                        field.id
                      }-${index}">${option.text || ""}</label>
                     </div>`;
          });
        } else {
          html += '<p class="text-muted">No checkbox options defined</p>';
        }
        break;
    }

    // Add error message element if validation is enabled
    if (field.validation && field.validation.enabled) {
      html += `<div class="invalid-feedback" id="preview-error-${field.id}">
                ${field.validation.errorMessage || "Please enter a valid value"}
              </div>`;
    }

    // Close column divs
    if (isLeftLabel) {
      html += "</div></div>";
    } else {
      html += "</div>";
    }

    previewContent.innerHTML = html;
  }

  /**
   * Show help information for the field editor
   */
  function showFieldEditorHelp() {
    // Create a modal if it doesn't exist
    const modalId = "field-editor-help-modal";
    let modal = document.getElementById(modalId);

    if (!modal) {
      modal = document.createElement("div");
      modal.id = modalId;
      modal.className = "modal fade";
      modal.setAttribute("tabindex", "-1");
      modal.innerHTML = `
        <div class="modal-dialog modal-lg">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Form Field Editor Help</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <h6>Basic Properties</h6>
              <ul>
                <li><strong>Label Text:</strong> The text shown next to the field</li>
                <li><strong>Field ID:</strong> Unique identifier for the field (used in HTML and JavaScript)</li>
                <li><strong>Field Type:</strong> The type of input element</li>
                <li><strong>Placeholder:</strong> Text shown inside the field when empty</li>
                <li><strong>Label Position:</strong> Where the label appears relative to the field</li>
                <li><strong>Required:</strong> Whether the field must be filled out</li>
              </ul>
              
              <h6>Validation</h6>
              <ul>
                <li><strong>Regex Pattern:</strong> A regular expression pattern to validate the input</li>
                <li><strong>Error Message:</strong> Text shown when validation fails</li>
                <li><strong>Min/Max Value:</strong> For number fields, the allowed range</li>
                <li><strong>Min/Max Length:</strong> For text fields, the allowed length range</li>
              </ul>
              
              <h6>Options (for Select, Radio, Checkbox)</h6>
              <ul>
                <li><strong>Text:</strong> The display text shown to the user</li>
                <li><strong>Value:</strong> The actual value stored when submitted</li>
                <li><strong>Options Layout:</strong> For radio/checkbox, vertical (stacked) or horizontal (inline)</li>
              </ul>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-primary" data-bs-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      `;
      document.body.appendChild(modal);

      // Initialize Bootstrap modal
      modal = new bootstrap.Modal(modal);
    }

    // Show the modal
    modal.show();
  }

  /**
   * Save the current field being edited
   */
  function saveCurrentField() {
    if (!state.selectedComponent || !state.currentEditingField) return;

    const component = state.selectedComponent;
    const field = state.currentEditingField;

    // Initialize formFields array if it doesn't exist
    if (!component.formFields) {
      component.formFields = [];
    }

    // Check if this is an edit of an existing field
    const existingFieldIndex = component.formFields.findIndex(
      (f) => f.id === field.id
    );

    if (existingFieldIndex >= 0) {
      // Update existing field
      component.formFields[existingFieldIndex] = { ...field };
    } else {
      // Add new field
      component.formFields.push({ ...field });
    }

    // Update the component in the model
    window.pageModelManager.updateComponent(component.id, {
      formFields: component.formFields,
    });

    // Close the field editor
    closeFieldEditor();

    // Update the fields list
    document.getElementById("form-fields-list").innerHTML =
      renderFormFieldsList(component);

    // Notify model updated
    notifyModelUpdated();
  }

  /**
   * Delete a form field
   */
  function deleteField(fieldId) {
    if (!state.selectedComponent || !fieldId) return;

    const component = state.selectedComponent;

    if (!component.formFields) return;

    // Filter out the field to delete
    component.formFields = component.formFields.filter((f) => f.id !== fieldId);

    // Update the component in the model
    window.pageModelManager.updateComponent(component.id, {
      formFields: component.formFields,
    });

    // Update the fields list
    document.getElementById("form-fields-list").innerHTML =
      renderFormFieldsList(component);

    // Notify model updated
    notifyModelUpdated();
  }

  /**
   * Close the field editor
   */
  function closeFieldEditor() {
    state.isFieldEditorOpen = false;
    state.currentEditingField = null;

    const fieldEditor = document.getElementById("field-editor");
    if (fieldEditor) {
      fieldEditor.style.display = "none";
    }
  }

  /**
   * Notify that the model has been updated
   */
  function notifyModelUpdated() {
    document.dispatchEvent(new CustomEvent("modelUpdated"));
  }

  // === Navigation Links Management ===

  /**
   * Set up the navigation links editor interface
   */
  function setupNavigationLinksEditor(component) {
    if (!component || component.type !== "nav") return;

    // Add the "Manage Navigation Links" section to the specific properties
    const navLinksContainer = document.createElement("div");
    navLinksContainer.className = "mt-3";
    navLinksContainer.innerHTML = `
      <h6 class="border-bottom pb-2">Navigation Links</h6>
      
      <div id="nav-links-list" class="mb-2">
        ${renderNavigationLinksList(component)}
      </div>
      
      <!-- New link form -->
      <div class="card mb-2">
        <div class="card-header py-1 px-2 bg-light">
          <h6 class="mb-0 small">Add New Link</h6>
        </div>
        <div class="card-body p-2">
          <div class="mb-2">
            <label for="new-link-text" class="form-label small">Link Text</label>
            <input type="text" class="form-control form-control-sm" id="new-link-text">
          </div>
          <div class="mb-2">
            <label for="new-link-url" class="form-label small">URL</label>
            <input type="text" class="form-control form-control-sm" id="new-link-url" placeholder="e.g., #, ../html/index.html">
          </div>
          <button id="add-nav-link-btn" class="btn btn-sm btn-primary">
            <i class="bi bi-plus-circle me-1"></i> Add Link
          </button>
        </div>
      </div>
      
      <!-- Register button customization -->
      <div class="card mb-2">
        <div class="card-header py-1 px-2 bg-light">
          <h6 class="mb-0 small">Register Button</h6>
        </div>
        <div class="card-body p-2">
          <div class="mb-2 form-check">
            <input class="form-check-input" type="checkbox" id="include-register-btn" 
              ${
                component.includeRegisterButton ? "checked" : ""
              } data-property="includeRegisterButton">
            <label class="form-check-label small" for="include-register-btn">Include "Register" Button</label>
          </div>
          
          <div id="register-button-options" ${
            !component.includeRegisterButton ? 'style="display:none;"' : ""
          }>
            <div class="mb-2">
              <label for="register-btn-text" class="form-label small">Button Text</label>
              <input type="text" class="form-control form-control-sm" id="register-btn-text"
                     value="${
                       component.registerButtonText || "Đăng ký"
                     }" data-property="registerButtonText">
            </div>
            
            <div class="mb-2">
              <label for="register-btn-class" class="form-label small">Button Color</label>
              <select class="form-select form-select-sm" id="register-btn-class" data-property="registerButtonClass">
                <option value="btn-primary" ${
                  component.registerButtonClass === "btn-primary"
                    ? "selected"
                    : ""
                }>Primary (Blue)</option>
                <option value="btn-secondary" ${
                  component.registerButtonClass === "btn-secondary"
                    ? "selected"
                    : ""
                }>Secondary (Gray)</option>
                <option value="btn-success" ${
                  component.registerButtonClass === "btn-success"
                    ? "selected"
                    : ""
                }>Success (Green)</option>
                <option value="btn-danger" ${
                  component.registerButtonClass === "btn-danger"
                    ? "selected"
                    : ""
                }>Danger (Red)</option>
                <option value="btn-warning" ${
                  component.registerButtonClass === "btn-warning"
                    ? "selected"
                    : ""
                }>Warning (Yellow)</option>
                <option value="btn-info" ${
                  component.registerButtonClass === "btn-info" ? "selected" : ""
                }>Info (Cyan)</option>
              </select>
            </div>
            
            <div class="mb-2">
              <label for="register-btn-size" class="form-label small">Button Size</label>
              <select class="form-select form-select-sm" id="register-btn-size" data-property="registerButtonSize">
                <option value="" ${
                  component.registerButtonSize === "" ? "selected" : ""
                }>Default</option>
                <option value="btn-sm" ${
                  component.registerButtonSize === "btn-sm" ? "selected" : ""
                }>Small</option>
                <option value="btn-lg" ${
                  component.registerButtonSize === "btn-lg" ? "selected" : ""
                }>Large</option>
              </select>
            </div>
            
            <div class="mt-2">
              <span class="small">Preview:</span>
              <div class="border rounded p-2 mt-1 text-center">
                <button class="btn ${component.registerButtonClass} ${
      component.registerButtonSize
    } preview-register-btn">
                  ${component.registerButtonText || "Đăng ký"}
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    `;

    elements.specificPropsContainer.appendChild(navLinksContainer);

    // Add event listener for Add Link button
    const addLinkBtn = navLinksContainer.querySelector("#add-nav-link-btn");
    addLinkBtn.addEventListener("click", function () {
      addNavigationLink(component);
    });

    // Toggle register button options based on checkbox
    const includeRegisterBtn = navLinksContainer.querySelector(
      "#include-register-btn"
    );
    const registerButtonOptions = navLinksContainer.querySelector(
      "#register-button-options"
    );

    includeRegisterBtn.addEventListener("change", function () {
      registerButtonOptions.style.display = this.checked ? "block" : "none";
    });

    // Update preview when button properties change
    const registerBtnText =
      navLinksContainer.querySelector("#register-btn-text");
    const registerBtnClass = navLinksContainer.querySelector(
      "#register-btn-class"
    );
    const registerBtnSize =
      navLinksContainer.querySelector("#register-btn-size");
    const previewButton = navLinksContainer.querySelector(
      ".preview-register-btn"
    );

    const updateButtonPreview = () => {
      previewButton.textContent = registerBtnText.value;

      // Reset classes and add the new ones
      previewButton.className = `btn ${registerBtnClass.value} ${registerBtnSize.value}`;
    };

    registerBtnText.addEventListener("input", updateButtonPreview);
    registerBtnClass.addEventListener("change", updateButtonPreview);
    registerBtnSize.addEventListener("change", updateButtonPreview);
  }

  /**
   * Render the list of navigation links
   */
  function renderNavigationLinksList(component) {
    if (!component.items || component.items.length === 0) {
      return '<p class="text-muted small">No navigation links defined</p>';
    }

    return `
      <div class="list-group">
        ${component.items
          .map(
            (link, index) => `
          <div class="list-group-item p-2">
            <div class="d-flex justify-content-between align-items-center mb-1">
              <span class="fw-bold small">${link.text || "Untitled"}</span>
              <div>
                <button class="btn btn-sm btn-outline-primary edit-nav-link-btn" 
                  data-index="${index}" title="Edit">
                  <i class="bi bi-pencil"></i>
                </button>
                <button class="btn btn-sm btn-outline-danger delete-nav-link-btn" 
                  data-index="${index}" title="Delete">
                  <i class="bi bi-trash"></i>
                </button>
              </div>
            </div>
            <div class="small text-muted">${link.url || "#"}</div>
            ${
              index === 0
                ? `<div class="small mt-1 bg-light p-1 rounded">
                <i class="bi bi-info-circle"></i> First item is usually your brand/site name
               </div>`
                : ""
            }
          </div>
        `
          )
          .join("")}
      </div>
    `;
  }

  /**
   * Add a new navigation link to the component
   */
  function addNavigationLink(component) {
    // Get values from the form inputs
    const textInput = document.getElementById("new-link-text");
    const urlInput = document.getElementById("new-link-url");

    const text = textInput.value.trim();
    const url = urlInput.value.trim();

    // Basic validation
    if (!text) {
      alert("Please enter link text");
      textInput.focus();
      return;
    }

    // Make a copy of current items and add the new link
    const items = [...(component.items || [])];
    items.push({ text, url: url || "#" });

    // Update the component in the model
    window.pageModelManager.updateComponent(component.id, { items });

    // Clear the form
    textInput.value = "";
    urlInput.value = "";

    // Update the links list
    document.getElementById("nav-links-list").innerHTML =
      renderNavigationLinksList(component);

    // Notify model updated
    notifyModelUpdated();
  }

  /**
   * Edit a navigation link
   */
  function editNavigationLink(component, index) {
    if (!component || !component.items || index >= component.items.length)
      return;

    const link = component.items[index];

    // Create a simple modal dialog for editing
    const modalId = "edit-link-modal";
    let modal = document.getElementById(modalId);

    // Create modal if it doesn't exist
    if (!modal) {
      modal = document.createElement("div");
      modal.id = modalId;
      modal.className = "modal fade";
      modal.setAttribute("tabindex", "-1");
      modal.innerHTML = `
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Edit Navigation Link</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <div class="mb-3">
                <label for="edit-link-text" class="form-label">Link Text</label>
                <input type="text" class="form-control" id="edit-link-text">
              </div>
              <div class="mb-3">
                <label for="edit-link-url" class="form-label">URL</label>
                <input type="text" class="form-control" id="edit-link-url">
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
              <button type="button" class="btn btn-primary" id="save-link-changes-btn">Save Changes</button>
            </div>
          </div>
        </div>
      `;
      document.body.appendChild(modal);

      // Use Bootstrap's Modal API
      modal = new bootstrap.Modal(modal);
    }

    // Set current values
    document.getElementById("edit-link-text").value = link.text || "";
    document.getElementById("edit-link-url").value = link.url || "#";

    // Show the modal
    modal.show();

    // Handle save button click
    const saveBtn = document.getElementById("save-link-changes-btn");

    // Remove previous event listener if exists
    const newSaveBtn = saveBtn.cloneNode(true);
    saveBtn.parentNode.replaceChild(newSaveBtn, saveBtn);

    // Add new event listener
    newSaveBtn.addEventListener("click", function () {
      const text = document.getElementById("edit-link-text").value.trim();
      const url = document.getElementById("edit-link-url").value.trim();

      if (!text) {
        alert("Link text cannot be empty");
        return;
      }

      // Update the link
      const items = [...component.items];
      items[index] = { text, url: url || "#" };

      // Update the component in the model
      window.pageModelManager.updateComponent(component.id, { items });

      // Update the links list
      document.getElementById("nav-links-list").innerHTML =
        renderNavigationLinksList(component);

      // Notify model updated
      notifyModelUpdated();

      // Hide the modal
      modal.hide();
    });
  }

  /**
   * Delete a navigation link
   */
  function deleteNavigationLink(component, index) {
    if (!component || !component.items || index >= component.items.length)
      return;

    // Confirmation
    if (
      !confirm(
        `Are you sure you want to delete the link "${component.items[index].text}"?`
      )
    ) {
      return;
    }

    // Make a copy of items and remove the link
    const items = [...component.items];
    items.splice(index, 1);

    // Update the component in the model
    window.pageModelManager.updateComponent(component.id, { items });

    // Update the links list
    document.getElementById("nav-links-list").innerHTML =
      renderNavigationLinksList(component);

    // Notify model updated
    notifyModelUpdated();
  }

  // === Table Columns Management ===

  /**
   * Set up the table columns editor interface
   */
  function setupTableColumnsEditor(component) {
    if (!component || component.type !== "table") return;

    // Add the "Manage Table Columns" section to the specific properties
    const tableColumnsContainer = document.createElement("div");
    tableColumnsContainer.className = "mt-3";
    tableColumnsContainer.innerHTML = `
      <h6 class="border-bottom pb-2">Table Columns</h6>
      
      <div id="table-columns-list" class="mb-2">
        ${renderTableColumnsList(component)}
      </div>
      
      <!-- New column form -->
      <div class="card mb-2">
        <div class="card-header py-1 px-2 bg-light">
          <h6 class="mb-0 small">Add New Column</h6>
        </div>
        <div class="card-body p-2">
          <div class="mb-2">
            <label for="new-column-text" class="form-label small">Column Header</label>
            <input type="text" class="form-control form-control-sm" id="new-column-text" placeholder="e.g., Name, Email, Date">
          </div>
          <button id="add-table-column-btn" class="btn btn-sm btn-primary">
            <i class="bi bi-plus-circle me-1"></i> Add Column
          </button>
        </div>
      </div>
      
      <div class="mb-2">
        <div class="form-check">
          <input class="form-check-input" type="checkbox" id="show-table-border" 
              ${
                component.showBorder ? "checked" : ""
              } data-property="showBorder">
          <label class="form-check-label small" for="show-table-border">Show Table Border</label>
        </div>
      </div>
    `;

    elements.specificPropsContainer.appendChild(tableColumnsContainer);

    // Add event listener for Add Column button
    const addColumnBtn = tableColumnsContainer.querySelector(
      "#add-table-column-btn"
    );
    addColumnBtn.addEventListener("click", function () {
      addTableColumn(component);
    });
  }

  /**
   * Render the list of table columns
   */
  function renderTableColumnsList(component) {
    if (!component.columns || component.columns.length === 0) {
      return '<p class="text-muted small">No table columns defined</p>';
    }

    return `
      <div class="list-group">
        ${component.columns
          .map((column, index) => {
            // Handle both string columns and object columns
            const headerText =
              typeof column === "string"
                ? column
                : column.headerText || "Untitled";

            return `
            <div class="list-group-item p-2">
              <div class="d-flex justify-content-between align-items-center">
                <span class="fw-bold small">${headerText}</span>
                <div>
                  <button class="btn btn-sm btn-outline-primary edit-column-btn" 
                    data-index="${index}" title="Edit">
                    <i class="bi bi-pencil"></i>
                  </button>
                  <button class="btn btn-sm btn-outline-danger delete-column-btn" 
                    data-index="${index}" title="Delete">
                    <i class="bi bi-trash"></i>
                  </button>
                </div>
              </div>
            </div>
          `;
          })
          .join("")}
      </div>
    `;
  }

  /**
   * Add a new table column to the component
   */
  function addTableColumn(component) {
    // Get value from the form input
    const textInput = document.getElementById("new-column-text");
    const headerText = textInput.value.trim();

    // Basic validation
    if (!headerText) {
      alert("Please enter column header text");
      textInput.focus();
      return;
    }

    // Convert existing columns to objects if they're strings
    let columns = [...(component.columns || [])].map((col) =>
      typeof col === "string" ? { headerText: col } : col
    );

    // Add the new column
    columns.push({ headerText });

    // Update the component in the model
    window.pageModelManager.updateComponent(component.id, { columns });

    // Clear the form
    textInput.value = "";

    // Update the columns list
    document.getElementById("table-columns-list").innerHTML =
      renderTableColumnsList(component);

    // Notify model updated
    notifyModelUpdated();
  }

  /**
   * Edit a table column
   */
  function editTableColumn(component, index) {
    if (!component || !component.columns || index >= component.columns.length)
      return;

    // Get the column (handle both string and object formats)
    const column = component.columns[index];
    const currentHeaderText =
      typeof column === "string" ? column : column.headerText || "";

    // Create a simple modal dialog for editing
    const modalId = "edit-column-modal";
    let modal = document.getElementById(modalId);

    // Create modal if it doesn't exist
    if (!modal) {
      modal = document.createElement("div");
      modal.id = modalId;
      modal.className = "modal fade";
      modal.setAttribute("tabindex", "-1");
      modal.innerHTML = `
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Edit Table Column</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <div class="mb-3">
                <label for="edit-column-text" class="form-label">Column Header</label>
                <input type="text" class="form-control" id="edit-column-text">
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
              <button type="button" class="btn btn-primary" id="save-column-changes-btn">Save Changes</button>
            </div>
          </div>
        </div>
      `;
      document.body.appendChild(modal);

      // Use Bootstrap's Modal API
      modal = new bootstrap.Modal(modal);
    }

    // Set current value
    document.getElementById("edit-column-text").value = currentHeaderText;

    // Show the modal
    modal.show();

    // Handle save button click
    const saveBtn = document.getElementById("save-column-changes-btn");

    // Remove previous event listener if exists
    const newSaveBtn = saveBtn.cloneNode(true);
    saveBtn.parentNode.replaceChild(newSaveBtn, saveBtn);

    // Add new event listener
    newSaveBtn.addEventListener("click", function () {
      const headerText = document
        .getElementById("edit-column-text")
        .value.trim();

      if (!headerText) {
        alert("Column header cannot be empty");
        return;
      }

      // Convert columns to objects if needed and update the column
      let columns = [...component.columns].map((col, i) => {
        if (i === index) {
          return { headerText };
        } else {
          return typeof col === "string" ? { headerText: col } : col;
        }
      });

      // Update the component in the model
      window.pageModelManager.updateComponent(component.id, { columns });

      // Update the columns list
      document.getElementById("table-columns-list").innerHTML =
        renderTableColumnsList(component);

      // Notify model updated
      notifyModelUpdated();

      // Hide the modal
      modal.hide();
    });
  }

  /**
   * Delete a table column
   */
  function deleteTableColumn(component, index) {
    if (!component || !component.columns || index >= component.columns.length)
      return;

    const column = component.columns[index];
    const headerText = typeof column === "string" ? column : column.headerText;

    // Confirmation
    if (
      !confirm(`Are you sure you want to delete the column "${headerText}"?`)
    ) {
      return;
    }

    // Remove the column
    const columns = [...component.columns];
    columns.splice(index, 1);

    // Update the component in the model
    window.pageModelManager.updateComponent(component.id, { columns });

    // Update the columns list
    document.getElementById("table-columns-list").innerHTML =
      renderTableColumnsList(component);

    // Notify model updated
    notifyModelUpdated();
  }

  // Initialize when DOM is fully loaded
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
