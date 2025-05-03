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
    // For image-table layout, add columns management for table part
    else if (component.type === "image-table-layout") {
      setupImageTableLayoutEditor(component);
    }
    // For nav-table layout, add columns management for table part and links for nav
    else if (component.type === "nav-table-layout") {
      setupNavTableLayoutEditor(component);
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
      const fieldType =
        e.target
          .closest(".edit-form-field-btn")
          .getAttribute("data-field-type") || "regular";
      editField(fieldId, fieldType);
    } else if (e.target.closest(".delete-form-field-btn")) {
      const fieldId = e.target
        .closest(".delete-form-field-btn")
        .getAttribute("data-field-id");
      const fieldType =
        e.target
          .closest(".delete-form-field-btn")
          .getAttribute("data-field-type") || "regular";
      deleteField(fieldId, fieldType);
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
    // Image+Table column management
    else if (
      e.target.closest("#add-table-column-btn") &&
      state.selectedComponent.type === "image-table-layout"
    ) {
      addColumnToImageTable(state.selectedComponent);
    } else if (
      e.target.closest(".edit-column-btn") &&
      state.selectedComponent.type === "image-table-layout"
    ) {
      const index = parseInt(
        e.target.closest(".edit-column-btn").getAttribute("data-index"),
        10
      );
      editColumnInImageTable(state.selectedComponent, index);
    } else if (
      e.target.closest(".delete-column-btn") &&
      state.selectedComponent.type === "image-table-layout"
    ) {
      const index = parseInt(
        e.target.closest(".delete-column-btn").getAttribute("data-index"),
        10
      );
      deleteColumnFromImageTable(state.selectedComponent, index);
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
    let fieldsHtml = "";

    // Regular form fields
    if (component.formFields && component.formFields.length > 0) {
      fieldsHtml += component.formFields
        .map(
          (field) => `
        <div class="list-group-item list-group-item-action d-flex justify-content-between align-items-center py-2">
            <div>
                <span class="fw-bold">${field.label || "Untitled"}</span>
                <br>
                <small class="text-muted">${field.type || "text"} ${
            field.id ? " - #" + field.id : ""
          }</small>
            </div>
            <div>
                <button class="btn btn-sm btn-outline-primary edit-form-field-btn" data-field-id="${
                  field.id
                }" data-field-type="regular">
                    <i class="bi bi-pencil"></i>
                </button>
                <button class="btn btn-sm btn-outline-danger delete-form-field-btn" data-field-id="${
                  field.id
                }" data-field-type="regular">
                    <i class="bi bi-trash"></i>
                </button>
            </div>
        </div>
      `
        )
        .join("");
    }

    // Radio groups
    if (component.radioGroups && component.radioGroups.length > 0) {
      fieldsHtml += component.radioGroups
        .map(
          (group) => `
        <div class="list-group-item list-group-item-action d-flex justify-content-between align-items-center py-2">
            <div>
                <span class="fw-bold">${group.label || "Untitled"}</span>
                <br>
                <small class="text-muted">Radio Group - ${
                  group.options.length
                } options - #${group.id}</small>
            </div>
            <div>
                <button class="btn btn-sm btn-outline-primary edit-form-field-btn" data-field-id="${
                  group.id
                }" data-field-type="radio">
                    <i class="bi bi-pencil"></i>
                </button>
                <button class="btn btn-sm btn-outline-danger delete-form-field-btn" data-field-id="${
                  group.id
                }" data-field-type="radio">
                    <i class="bi bi-trash"></i>
                </button>
            </div>
        </div>
      `
        )
        .join("");
    }

    // Checkbox groups
    if (component.checkboxGroups && component.checkboxGroups.length > 0) {
      fieldsHtml += component.checkboxGroups
        .map(
          (group) => `
        <div class="list-group-item list-group-item-action d-flex justify-content-between align-items-center py-2">
            <div>
                <span class="fw-bold">${group.label || "Untitled"}</span>
                <br>
                <small class="text-muted">Checkbox Group - ${
                  group.options.length
                } options - #${group.id}</small>
            </div>
            <div>
                <button class="btn btn-sm btn-outline-primary edit-form-field-btn" data-field-id="${
                  group.id
                }" data-field-type="checkbox">
                    <i class="bi bi-pencil"></i>
                </button>
                <button class="btn btn-sm btn-outline-danger delete-form-field-btn" data-field-id="${
                  group.id
                }" data-field-type="checkbox">
                    <i class="bi bi-trash"></i>
                </button>
            </div>
        </div>
      `
        )
        .join("");
    }

    return (
      fieldsHtml ||
      '<div class="text-muted p-3 small">No form fields added yet. Click the "Add New Field" button below to add fields.</div>'
    );
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
  function editField(fieldId, fieldType = "regular") {
    if (!state.selectedComponent || state.selectedComponent.type !== "modal")
      return;

    const component = state.selectedComponent;
    let field;

    // Find the field or group based on its type
    switch (fieldType) {
      case "radio":
        field = component.radioGroups?.find((g) => g.id === fieldId);
        if (field) {
          // Create a field object compatible with our editor
          state.currentEditingField = {
            ...field,
            isGroup: true,
            groupType: "radio",
          };
        }
        break;

      case "checkbox":
        field = component.checkboxGroups?.find((g) => g.id === fieldId);
        if (field) {
          // Create a field object compatible with our editor
          state.currentEditingField = {
            ...field,
            isGroup: true,
            groupType: "checkbox",
          };
        }
        break;

      default: // regular form field
        field = component.formFields?.find((f) => f.id === fieldId);
        if (field) {
          // Regular fields don't need special handling
          state.currentEditingField = { ...field };
        }
        break;
    }

    if (!state.currentEditingField) return;

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
    field.isGroup = field.isGroup || false;
    field.groupType = field.groupType || "";

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
      
      <div class="mb-2">
        <label for="field-type-container" class="form-label">Field Type</label>
        <div class="d-flex" id="field-type-container">
          <div class="form-check me-3">
            <input class="form-check-input" type="radio" name="fieldTypeGroup" id="regular-field" 
              ${!field.isGroup ? "checked" : ""} value="regular">
            <label class="form-check-label" for="regular-field">Regular Field</label>
          </div>
          <div class="form-check me-3">
            <input class="form-check-input" type="radio" name="fieldTypeGroup" id="radio-group" 
              ${
                field.isGroup && field.groupType === "radio" ? "checked" : ""
              } value="radio">
            <label class="form-check-label" for="radio-group">Radio Group</label>
          </div>
          <div class="form-check">
            <input class="form-check-input" type="radio" name="fieldTypeGroup" id="checkbox-group" 
              ${
                field.isGroup && field.groupType === "checkbox" ? "checked" : ""
              } value="checkbox">
            <label class="form-check-label" for="checkbox-group">Checkbox Group</label>
          </div>
        </div>
      </div>
      
      <!-- Regular field controls -->
      <div id="regular-field-controls" style="${
        field.isGroup ? "display:none;" : ""
      }">
        <div class="mb-2">
          <label for="field-type" class="form-label">Input Type</label>
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
          </select>
        </div>
        
        <div class="mb-2">
          <label for="field-label" class="form-label">Label Text</label>
          <input type="text" class="form-control form-control-sm" id="field-label" 
              value="${field.label || ""}" data-field-prop="label">
        </div>
        
        <div class="mb-2">
          <label for="field-id" class="form-label">Field ID</label>
          <input type="text" class="form-control form-control-sm" id="field-id" 
              value="${field.id || ""}" data-field-prop="id">
          <div class="form-text small">Use descriptive IDs like "txtFullName" or "slGender"</div>
        </div>
        
        <div class="mb-2" id="placeholder-container" ${
          ["select"].includes(field.type) ? 'style="display:none;"' : ""
        }>
          <label for="field-placeholder" class="form-label">Placeholder</label>
          <input type="text" class="form-control form-control-sm" id="field-placeholder" 
              value="${field.placeholder || ""}" data-field-prop="placeholder">
        </div>
        
        <div class="mb-2">
          <label for="field-label-position" class="form-label">Label Position</label>
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
          <label class="form-check-label" for="field-required">Required Field</label>
        </div>

        <!-- Options section for select dropdown -->
        <div id="select-options-container" style="${
          field.type === "select" ? "" : "display:none;"
        }">
          <hr>
          <h6>Dropdown Options</h6>
          <div id="options-list">
            ${renderFieldOptions(field)}
          </div>
          <button class="btn btn-sm btn-outline-primary w-100 mt-2" id="add-option-btn">
            <i class="bi bi-plus-circle"></i> Add Option
          </button>
        </div>
      </div>
      
      <!-- Group fields controls (radio/checkbox) -->
      <div id="group-field-controls" style="${
        !field.isGroup ? "display:none;" : ""
      }">
        <div class="mb-2">
          <label for="group-label" class="form-label">Group Label</label>
          <input type="text" class="form-control form-control-sm" id="group-label" 
              value="${field.label || ""}" data-field-prop="label">
        </div>
        
        <div class="mb-2">
          <label for="group-id" class="form-label">Group ID</label>
          <input type="text" class="form-control form-control-sm" id="group-id" 
              value="${field.id || ""}" data-field-prop="id">
          <div class="form-text small">Use descriptive IDs like "radioHinhthuc" or "chkSkills"</div>
        </div>
        
        <div id="group-name-container" style="${
          field.groupType === "radio" ? "" : "display:none;"
        }">
          <div class="mb-2">
            <label for="group-name" class="form-label">Radio Group Name</label>
            <input type="text" class="form-control form-control-sm" id="group-name" 
                value="${field.name || "radioGroup"}" data-field-prop="name">
            <div class="form-text small">Common name for all radio buttons in this group</div>
          </div>
        </div>
        
        <div class="mb-2 form-check">
          <input type="checkbox" class="form-check-input" id="group-required" 
              ${field.required ? "checked" : ""} data-field-prop="required">
          <label class="form-check-label" for="group-required">Required Group</label>
        </div>
        
        <div class="mb-2">
          <label for="options-layout" class="form-label">Options Layout</label>
          <select class="form-select form-select-sm" id="options-layout" data-field-prop="optionsLayout">
            <option value="vertical" ${
              field.optionsLayout === "vertical" ? "selected" : ""
            }>Vertical (Stacked)</option>
            <option value="horizontal" ${
              field.optionsLayout === "horizontal" ? "selected" : ""
            }>Horizontal (Inline)</option>
          </select>
        </div>
        
        <hr>
        <h6>Group Options</h6>
        
        <div id="group-options-list">
          ${renderGroupOptions(field)}
        </div>
        
        <button class="btn btn-sm btn-outline-primary w-100 mt-2" id="add-group-option-btn">
          <i class="bi bi-plus-circle"></i> Add Option
        </button>
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
   * Render options for radio/checkbox groups
   */
  function renderGroupOptions(field) {
    if (!field.options || !field.options.length) {
      return `<div class="text-muted small">No options added yet. Add some options below.</div>`;
    }

    return `
      <div class="options-list">
        ${field.options
          .map(
            (option, index) => `
          <div class="option-item d-flex align-items-center mb-1" data-index="${index}">
            <div class="flex-grow-1 me-1">
              <div class="input-group input-group-sm mb-1">
                <span class="input-group-text">ID</span>
                <input type="text" class="form-control option-id" placeholder="ID" 
                  value="${option.id || ""}" aria-label="Option ID">
              </div>
              <div class="input-group input-group-sm">
                <span class="input-group-text">Label</span>
                <input type="text" class="form-control option-label" placeholder="Label" 
                  value="${option.label || ""}" aria-label="Option label">
                <span class="input-group-text">Value</span>
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
    // Radio buttons for field type group
    const fieldTypeRadios = fieldEditor.querySelectorAll(
      'input[name="fieldTypeGroup"]'
    );
    fieldTypeRadios.forEach((radio) => {
      radio.addEventListener("change", function () {
        const regularControls = document.getElementById(
          "regular-field-controls"
        );
        const groupControls = document.getElementById("group-field-controls");
        const groupNameContainer = document.getElementById(
          "group-name-container"
        );

        field.isGroup = this.value === "radio" || this.value === "checkbox";
        field.groupType = this.value === "regular" ? "" : this.value;

        // Show/hide appropriate controls
        if (field.isGroup) {
          regularControls.style.display = "none";
          groupControls.style.display = "block";

          // Show group name field only for radio buttons
          if (groupNameContainer) {
            groupNameContainer.style.display =
              this.value === "radio" ? "block" : "none";
          }

          // Initialize default values for the group
          if (this.value === "radio" && !field.name) {
            field.name = "radioGroup";
          }

          if (!field.options || !field.options.length) {
            field.options = [
              {
                id: `${this.value}Option1`,
                label: "Option 1",
                value: "option1",
              },
            ];

            // Update the options UI
            const groupOptionsList =
              document.getElementById("group-options-list");
            if (groupOptionsList) {
              groupOptionsList.innerHTML = renderGroupOptions(field);
              setupOptionsEventListeners(field);
            }
          }
        } else {
          regularControls.style.display = "block";
          groupControls.style.display = "none";
        }
      });
    });

    // Add button for group options
    const addGroupOptionBtn = fieldEditor.querySelector(
      "#add-group-option-btn"
    );
    if (addGroupOptionBtn) {
      addGroupOptionBtn.addEventListener("click", function () {
        if (!field.options) field.options = [];

        const newOptionId =
          field.groupType === "radio"
            ? `radio${field.options.length + 1}`
            : `chk${field.options.length + 1}`;

        field.options.push({
          id: newOptionId,
          label: `Option ${field.options.length + 1}`,
          value: `option${field.options.length + 1}`,
        });

        // Update UI
        const groupOptionsList = document.getElementById("group-options-list");
        groupOptionsList.innerHTML = renderGroupOptions(field);

        // Setup listeners for the new option
        setupOptionsEventListeners(field);
      });
    }

    // Basic input change listeners
    const basicInputs = fieldEditor.querySelectorAll("[data-field-prop]");
    basicInputs.forEach((input) => {
      input.addEventListener("change", function () {
        const property = this.getAttribute("data-field-prop");
        let value;

        if (this.type === "checkbox") {
          value = this.checked;
        } else {
          value = this.value;
        }

        field[property] = value;
      });
    });

    // Field type change listener (for regular fields)
    const fieldTypeSelect = fieldEditor.querySelector("#field-type");
    if (fieldTypeSelect) {
      fieldTypeSelect.addEventListener("change", function () {
        const placeholderContainer = document.getElementById(
          "placeholder-container"
        );
        const selectOptionsContainer = document.getElementById(
          "select-options-container"
        );

        field.type = this.value;

        // Toggle placeholder visibility
        if (placeholderContainer) {
          placeholderContainer.style.display =
            this.value === "select" ? "none" : "block";
        }

        // Toggle options list visibility for select fields
        if (selectOptionsContainer) {
          selectOptionsContainer.style.display =
            this.value === "select" ? "block" : "none";

          // Initialize options for select if needed
          if (
            this.value === "select" &&
            (!field.options || !field.options.length)
          ) {
            field.options = [{ text: "Option 1", value: "option1" }];
            const optionsList = document.getElementById("options-list");
            if (optionsList) {
              optionsList.innerHTML = renderFieldOptions(field);
              setupOptionsEventListeners(field);
            }
          }
        }
      });
    }

    // Add option button (for select fields)
    const addOptionBtn = fieldEditor.querySelector("#add-option-btn");
    if (addOptionBtn) {
      addOptionBtn.addEventListener("click", function () {
        if (!field.options) field.options = [];
        field.options.push({
          text: `Option ${field.options.length + 1}`,
          value: `option${field.options.length + 1}`,
        });

        // Update UI
        const optionsList = document.getElementById("options-list");
        optionsList.innerHTML = renderFieldOptions(field);
        setupOptionsEventListeners(field);
      });
    }

    // Cancel button
    const cancelBtn = fieldEditor.querySelector("#cancel-field-editor-btn");
    if (cancelBtn) {
      cancelBtn.addEventListener("click", function () {
        closeFieldEditor();
      });
    }

    // Save button
    const saveBtn = fieldEditor.querySelector("#save-form-field-btn");
    if (saveBtn) {
      saveBtn.addEventListener("click", function () {
        saveCurrentField();
      });
    }

    // Setup initial option listeners
    setupOptionsEventListeners(field);
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
   * Save the current field being edited
   */
  function saveCurrentField() {
    if (!state.selectedComponent || !state.currentEditingField) return;

    const component = state.selectedComponent;
    const field = state.currentEditingField;

    // Handle different field types (regular field vs. radio group vs. checkbox group)
    if (field.isGroup) {
      // For group fields (radio/checkbox)
      if (field.groupType === "radio") {
        // Check if we're editing an existing radio group
        const existingGroupIndex = component.radioGroups
          ? component.radioGroups.findIndex((group) => group.id === field.id)
          : -1;

        const radioGroup = {
          name: field.name || "hinhthuc",
          label: field.label || "Group Label",
          id: field.id,
          validation: true,
          optionsLayout: field.optionsLayout || "vertical",
          options: field.options.map((option) => ({
            id: option.id || `radio${Date.now()}`,
            value: option.value || "",
            label: option.label || option.value || "",
            checked: option.checked || false,
          })),
        };

        if (existingGroupIndex >= 0) {
          // Update existing group
          component.radioGroups[existingGroupIndex] = radioGroup;
        } else {
          // Add new radio group
          if (!component.radioGroups) component.radioGroups = [];
          component.radioGroups.push(radioGroup);
        }
      } else if (field.groupType === "checkbox") {
        // Check if we're editing an existing checkbox group
        const existingGroupIndex = component.checkboxGroups
          ? component.checkboxGroups.findIndex((group) => group.id === field.id)
          : -1;

        const checkboxGroup = {
          label: field.label || "Group Label",
          id: field.id,
          validation: true,
          optionsLayout: field.optionsLayout || "vertical",
          options: field.options.map((option) => ({
            id: option.id || `chk${Date.now()}`,
            value: option.value || "",
            label: option.label || option.value || "",
            checked: option.checked || false,
          })),
        };

        if (existingGroupIndex >= 0) {
          // Update existing group
          component.checkboxGroups[existingGroupIndex] = checkboxGroup;
        } else {
          // Add new checkbox group
          if (!component.checkboxGroups) component.checkboxGroups = [];
          component.checkboxGroups.push(checkboxGroup);
        }
      }
    } else {
      // For regular form fields (text, email, select, etc.)
      if (!component.formFields) component.formFields = [];

      // Check if this field exists
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
    }

    // Close the field editor
    closeFieldEditor();

    // Update the fields list
    const formFieldsList = document.getElementById("form-fields-list");
    if (formFieldsList) {
      formFieldsList.innerHTML = renderFormFieldsList(component);
    }

    // Notify that the model has been updated
    notifyModelUpdated();
  }

  /**
   * Delete a form field
   */
  function deleteField(fieldId, fieldType = "regular") {
    if (!state.selectedComponent) return;

    const component = state.selectedComponent;

    // Delete the field based on its type
    switch (fieldType) {
      case "radio":
        if (component.radioGroups) {
          component.radioGroups = component.radioGroups.filter(
            (g) => g.id !== fieldId
          );
        }
        break;

      case "checkbox":
        if (component.checkboxGroups) {
          component.checkboxGroups = component.checkboxGroups.filter(
            (g) => g.id !== fieldId
          );
        }
        break;

      default: // regular form field
        if (component.formFields) {
          component.formFields = component.formFields.filter(
            (f) => f.id !== fieldId
          );
        }
        break;
    }

    // Update the form fields list
    document.getElementById("form-fields-list").innerHTML =
      renderFormFieldsList(component);

    // Notify about model update
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
      
      <!-- Navigation orientation -->
      <div class="card mb-2">
        <div class="card-header py-1 px-2 bg-light">
          <h6 class="mb-0 small">Navigation Display</h6>
        </div>
        <div class="card-body p-2">
          <div class="mb-2">
            <label for="nav-orientation" class="form-label small">Orientation</label>
            <select class="form-select form-select-sm" id="nav-orientation" data-property="orientation">
              <option value="horizontal" ${
                component.orientation === "horizontal" || !component.orientation
                  ? "selected"
                  : ""
              }>Horizontal (Default)</option>
              <option value="vertical" ${
                component.orientation === "vertical" ? "selected" : ""
              }>Vertical (Sidebar)</option>
            </select>
            <div class="form-text small">Vertical mode works well next to table components.</div>
          </div>
          
          <!-- Preview of orientation -->
          <div class="mt-2 p-2 border rounded">
            ${
              component.orientation === "vertical"
                ? `<div class="d-flex align-items-center justify-content-center" style="height:110px">
                <div class="bg-light p-2 rounded" style="width:80px; text-align:center">
                  <div class="mb-1">Link 1</div>
                  <div class="mb-1">Link 2</div>
                  <div class="mb-1">Link 3</div>
                  <div class="mb-1 btn-sm btn-danger" style="font-size:10px">Button</div>
                </div>
                <div style="flex:1; height:100px; background:#eee; margin-left:10px; display:flex; align-items:center; justify-content:center">
                  Table/Content
                </div>
              </div>`
                : `<div class="d-flex flex-column">
                <div class="bg-light p-2 rounded d-flex align-items-center justify-content-center">
                  <span class="me-3">Link 1</span>
                  <span class="me-3">Link 2</span>
                  <span class="me-3">Link 3</span>
                  <span class="btn-sm btn-danger" style="font-size:10px">Button</span>
                </div>
                <div style="height:80px; background:#eee; margin-top:10px; display:flex; align-items:center; justify-content:center">
                  Table/Content
                </div>
              </div>`
            }
          </div>
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

    // Add live update for orientation preview
    const orientationSelect =
      navLinksContainer.querySelector("#nav-orientation");
    if (orientationSelect) {
      orientationSelect.addEventListener("change", function () {
        const previewContainer =
          this.closest(".card-body").querySelector(".border.rounded");
        if (previewContainer) {
          if (this.value === "vertical") {
            previewContainer.innerHTML = `
              <div class="d-flex align-items-center justify-content-center" style="height:110px">
                <div class="bg-light p-2 rounded" style="width:80px; text-align:center">
                  <div class="mb-1">Link 1</div>
                  <div class="mb-1">Link 2</div>
                  <div class="mb-1">Link 3</div>
                  <div class="mb-1 btn-sm btn-danger" style="font-size:10px">Button</div>
                </div>
                <div style="flex:1; height:100px; background:#eee; margin-left:10px; display:flex; align-items:center; justify-content:center">
                  Table/Content
                </div>
              </div>`;
          } else {
            previewContainer.innerHTML = `
              <div class="d-flex flex-column">
                <div class="bg-light p-2 rounded d-flex align-items-center justify-content-center">
                  <span class="me-3">Link 1</span>
                  <span class="me-3">Link 2</span>
                  <span class="me-3">Link 3</span>
                  <span class="btn-sm btn-danger" style="font-size:10px">Button</span>
                </div>
                <div style="height:80px; background:#eee; margin-top:10px; display:flex; align-items:center; justify-content:center">
                  Table/Content
                </div>
              </div>`;
          }
        }
      });
    }
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
    }

    // Set current values
    document.getElementById("edit-link-text").value = link.text || "";
    document.getElementById("edit-link-url").value = link.url || "#";

    // Handle save button click - fixed to work with persistent modals
    const saveBtn = document.getElementById("save-link-changes-btn");

    // Clean up previous event listeners to prevent duplicates
    if (saveBtn._clickHandler) {
      saveBtn.removeEventListener("click", saveBtn._clickHandler);
    }

    // Create a new handler function
    saveBtn._clickHandler = function () {
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
      bootstrap.Modal.getInstance(document.getElementById(modalId)).hide();
    };

    // Add the new event listener
    saveBtn.addEventListener("click", saveBtn._clickHandler);

    // Show the modal - make sure we use proper Bootstrap API
    const bsModal = new bootstrap.Modal(document.getElementById(modalId));
    bsModal.show();
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
    }

    // Set current value
    document.getElementById("edit-column-text").value = currentHeaderText;

    // Handle save button click - fixed to work with persistent modals
    const saveBtn = document.getElementById("save-column-changes-btn");

    // Clean up previous event listeners to prevent duplicates
    if (saveBtn._clickHandler) {
      saveBtn.removeEventListener("click", saveBtn._clickHandler);
    }

    // Create a new handler function
    saveBtn._clickHandler = function () {
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
      bootstrap.Modal.getInstance(document.getElementById(modalId)).hide();
    };

    // Add the new event listener
    saveBtn.addEventListener("click", saveBtn._clickHandler);

    // Show the modal - make sure we use proper Bootstrap API
    const bsModal = new bootstrap.Modal(document.getElementById(modalId));
    bsModal.show();
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

  /**
   * Set up the image table layout editor interface
   */
  function setupImageTableLayoutEditor(component) {
    if (!component || component.type !== "image-table-layout") return;

    // Add the "Manage Image and Table Columns" section to the specific properties
    const imageTableContainer = document.createElement("div");
    imageTableContainer.className = "mt-3";
    imageTableContainer.innerHTML = `
      <h6 class="border-bottom pb-2">Table Columns</h6>
      
      <div id="table-columns-list" class="mb-2">
        ${renderTableColumnsListForImageTable(component)}
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
      
      <!-- Layout preview -->
      <h6 class="border-bottom pb-2 mt-4">Layout Preview</h6>
      <div class="layout-preview p-2 border rounded mb-3">
        <div class="d-flex align-items-center ${
          component.image.position === "left" ? "" : "flex-row-reverse"
        }">
          <div class="${getImageColumnClass(
            component
          )} p-2 text-center bg-light">
            <div class="small">Image</div>
            <i class="bi bi-image fs-1"></i>
          </div>
          <div class="${getTableColumnClass(component)} p-2 ms-2 bg-light">
            <div class="small">Table</div>
            <i class="bi bi-table"></i>
            <div class="small mt-1">${component.table.title}</div>
          </div>
        </div>
      </div>
    `;

    elements.specificPropsContainer.appendChild(imageTableContainer);

    // Add event listener for Add Column button
    const addColumnBtn = imageTableContainer.querySelector(
      "#add-table-column-btn"
    );
    addColumnBtn.addEventListener("click", function () {
      addColumnToImageTable(component);
    });
  }

  // Helper function to get appropriate CSS class for image column width
  function getImageColumnClass(component) {
    switch (component.columnClasses.imageCol) {
      case "col-md-4":
        return "w-25";
      case "col-md-5":
        return "w-40";
      case "col-md-6":
        return "w-50";
      case "col-md-7":
        return "w-60";
      case "col-md-8":
        return "w-75";
      default:
        return "w-50";
    }
  }

  // Helper function to get appropriate CSS class for table column width
  function getTableColumnClass(component) {
    switch (component.columnClasses.tableCol) {
      case "col-md-4":
        return "w-25";
      case "col-md-5":
        return "w-40";
      case "col-md-6":
        return "w-50";
      case "col-md-7":
        return "w-60";
      case "col-md-8":
        return "w-75";
      default:
        return "w-50";
    }
  }

  /**
   * Set up the nav table layout editor interface
   */
  function setupNavTableLayoutEditor(component) {
    if (!component || component.type !== "nav-table-layout") return;

    // Add both navigation links and table columns sections
    const navTableContainer = document.createElement("div");
    navTableContainer.className = "mt-3";

    // Navigation Links Section
    navTableContainer.innerHTML = `
      <h6 class="border-bottom pb-2">Navigation Links</h6>
      
      <div id="nav-links-list" class="mb-2">
        ${renderNavigationLinksList(component, "navigation.items")}
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
      <div class="card mb-3">
        <div class="card-header py-1 px-2 bg-light">
          <h6 class="mb-0 small">Register Button</h6>
        </div>
        <div class="card-body p-2">
          <div class="mb-2 form-check">
            <input class="form-check-input" type="checkbox" id="include-register-btn" 
              ${
                component.navigation.includeRegisterButton ? "checked" : ""
              } data-property="navigation.includeRegisterButton">
            <label class="form-check-label small" for="include-register-btn">Include "Register" Button</label>
          </div>
          
          <div id="register-button-options" ${
            !component.navigation.includeRegisterButton
              ? 'style="display:none;"'
              : ""
          }>
            <div class="mb-2">
              <label for="register-btn-text" class="form-label small">Button Text</label>
              <input type="text" class="form-control form-control-sm" id="register-btn-text"
                     value="${
                       component.navigation.registerButtonText || "Đăng ký"
                     }" data-property="navigation.registerButtonText">
            </div>
            
            <div class="mb-2">
              <label for="register-btn-class" class="form-label small">Button Color</label>
              <select class="form-select form-select-sm" id="register-btn-class" data-property="navigation.registerButtonClass">
                <option value="btn-primary" ${
                  component.navigation.registerButtonClass === "btn-primary"
                    ? "selected"
                    : ""
                }>Primary (Blue)</option>
                <option value="btn-secondary" ${
                  component.navigation.registerButtonClass === "btn-secondary"
                    ? "selected"
                    : ""
                }>Secondary (Gray)</option>
                <option value="btn-success" ${
                  component.navigation.registerButtonClass === "btn-success"
                    ? "selected"
                    : ""
                }>Success (Green)</option>
                <option value="btn-danger" ${
                  component.navigation.registerButtonClass === "btn-danger"
                    ? "selected"
                    : ""
                }>Danger (Red)</option>
                <option value="btn-warning" ${
                  component.navigation.registerButtonClass === "btn-warning"
                    ? "selected"
                    : ""
                }>Warning (Yellow)</option>
                <option value="btn-info" ${
                  component.navigation.registerButtonClass === "btn-info"
                    ? "selected"
                    : ""
                }>Info (Cyan)</option>
              </select>
            </div>
            
            <div class="mb-2">
              <label for="register-btn-size" class="form-label small">Button Size</label>
              <select class="form-select form-select-sm" id="register-btn-size" data-property="navigation.registerButtonSize">
                <option value="" ${
                  component.navigation.registerButtonSize === ""
                    ? "selected"
                    : ""
                }>Default</option>
                <option value="btn-sm" ${
                  component.navigation.registerButtonSize === "btn-sm"
                    ? "selected"
                    : ""
                }>Small</option>
                <option value="btn-lg" ${
                  component.navigation.registerButtonSize === "btn-lg"
                    ? "selected"
                    : ""
                }>Large</option>
              </select>
            </div>
            
            <div class="mt-2">
              <span class="small">Preview:</span>
              <div class="border rounded p-2 mt-1 text-center">
                <button class="btn ${
                  component.navigation.registerButtonClass
                } ${
      component.navigation.registerButtonSize
    } preview-register-btn">
                  ${component.navigation.registerButtonText || "Đăng ký"}
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Table Columns Section -->
      <h6 class="border-bottom pb-2 mt-4">Table Columns</h6>
      
      <div id="table-columns-list" class="mb-2">
        ${renderTableColumnsListForLayout(component)}
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
      
      <!-- Layout preview -->
      <h6 class="border-bottom pb-2 mt-4">Layout Preview</h6>
      <div class="layout-preview p-2 border rounded mb-3">
        <div class="d-flex align-items-start ${
          component.navigation.position === "left" ? "" : "flex-row-reverse"
        }">
          <div class="${getNavColumnClass(component)} p-2 border-end bg-light">
            <div class="small mb-2">Navigation</div>
            <div class="small">${component.navigation.items
              .map((item) => item.text)
              .slice(0, 3)
              .join("<br>")}</div>
            <div class="small mt-2">...</div>
            ${
              component.navigation.includeRegisterButton
                ? `<button class="btn btn-sm ${component.navigation.registerButtonClass} mt-2" style="font-size:0.7rem;">
                 ${component.navigation.registerButtonText}
               </button>`
                : ""
            }
          </div>
          <div class="flex-grow-1 p-2 ms-2 bg-light">
            <div class="small mb-2">Table: ${component.table.title}</div>
            <div class="table-responsive">
              <table class="table table-sm ${
                component.table.showBorder ? "table-bordered" : ""
              }" style="font-size:0.7rem">
                <thead>
                  <tr>
                    ${component.table.columns
                      .slice(0, 3)
                      .map(
                        (col) =>
                          `<th>${
                            typeof col === "string" ? col : col.headerText
                          }</th>`
                      )
                      .join("")}
                    ${component.table.columns.length > 3 ? "<th>...</th>" : ""}
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    ${component.table.columns
                      .slice(0, 3)
                      .map(() => "<td>Data</td>")
                      .join("")}
                    ${component.table.columns.length > 3 ? "<td>...</td>" : ""}
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    `;

    elements.specificPropsContainer.appendChild(navTableContainer);

    // Add event listener for Add Link button
    const addLinkBtn = navTableContainer.querySelector("#add-nav-link-btn");
    addLinkBtn.addEventListener("click", function () {
      addNavigationLinkToLayout(component);
    });

    // Add event listener for Add Column button
    const addColumnBtn = navTableContainer.querySelector(
      "#add-table-column-btn"
    );
    addColumnBtn.addEventListener("click", function () {
      addColumnToLayout(component);
    });

    // Add event listener for register button checkbox
    const registerBtn = navTableContainer.querySelector(
      "#include-register-btn"
    );
    registerBtn.addEventListener("change", function () {
      const options = navTableContainer.querySelector(
        "#register-button-options"
      );
      if (options) {
        options.style.display = this.checked ? "" : "none";
      }
    });

    // Set up event listeners for existing action buttons
    setupNavTableLayoutEventListeners(navTableContainer, component);
  }

  // Helper function to get appropriate CSS class for nav column width
  function getNavColumnClass(component) {
    switch (component.columnClasses.navCol) {
      case "col-md-3":
        return "w-25";
      case "col-md-4":
        return "w-33";
      case "col-md-5":
        return "w-40";
      default:
        return "w-25";
    }
  }

  /**
   * Render the list of table columns for image-table layout
   */
  function renderTableColumnsListForImageTable(component) {
    if (!component.table.columns || component.table.columns.length === 0) {
      return '<p class="text-muted small">No table columns defined</p>';
    }

    return `
      <div class="list-group">
        ${component.table.columns
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
   * Add a new table column to the image-table component
   */
  function addColumnToImageTable(component) {
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
    let columns = [...component.table.columns].map((col) =>
      typeof col === "string" ? { headerText: col } : col
    );

    // Add the new column
    columns.push({ headerText });

    // Update the component in the model
    window.pageModelManager.updateComponent(component.id, {
      table: { ...component.table, columns },
    });

    // Clear the form
    textInput.value = "";

    // Update the columns list
    document.getElementById("table-columns-list").innerHTML =
      renderTableColumnsListForImageTable(component);

    // Notify model updated
    notifyModelUpdated();
  }

  /**
   * Edit a column in the image-table component
   */
  function editColumnInImageTable(component, index) {
    if (
      !component ||
      !component.table.columns ||
      index >= component.table.columns.length
    )
      return;

    // Get the column (handle both string and object formats)
    const column = component.table.columns[index];
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
    }

    // Set current value
    document.getElementById("edit-column-text").value = currentHeaderText;

    // Handle save button click - fixed to work with persistent modals
    const saveBtn = document.getElementById("save-column-changes-btn");

    // Clean up previous event listeners to prevent duplicates
    if (saveBtn._clickHandler) {
      saveBtn.removeEventListener("click", saveBtn._clickHandler);
    }

    // Create a new handler function
    saveBtn._clickHandler = function () {
      const headerText = document
        .getElementById("edit-column-text")
        .value.trim();

      if (!headerText) {
        alert("Column header cannot be empty");
        return;
      }

      // Convert columns to objects if needed and update the column
      let columns = [...component.table.columns].map((col, i) => {
        if (i === index) {
          return { headerText };
        } else {
          return typeof col === "string" ? { headerText: col } : col;
        }
      });

      // Update the component in the model
      window.pageModelManager.updateComponent(component.id, {
        table: { ...component.table, columns },
      });

      // Update the columns list
      document.getElementById("table-columns-list").innerHTML =
        renderTableColumnsListForImageTable(component);

      // Notify model updated
      notifyModelUpdated();

      // Hide the modal
      bootstrap.Modal.getInstance(document.getElementById(modalId)).hide();
    };

    // Add the new event listener
    saveBtn.addEventListener("click", saveBtn._clickHandler);

    // Show the modal - make sure we use proper Bootstrap API
    const bsModal = new bootstrap.Modal(document.getElementById(modalId));
    bsModal.show();
  }

  /**
   * Delete a column from the image-table component
   */
  function deleteColumnFromImageTable(component, index) {
    if (
      !component ||
      !component.table.columns ||
      index >= component.table.columns.length
    )
      return;

    const column = component.table.columns[index];
    const headerText = typeof column === "string" ? column : column.headerText;

    // Confirmation
    if (
      !confirm(`Are you sure you want to delete the column "${headerText}"?`)
    ) {
      return;
    }

    // Remove the column
    const columns = [...component.table.columns];
    columns.splice(index, 1);

    // Update the component in the model
    window.pageModelManager.updateComponent(component.id, {
      table: { ...component.table, columns },
    });

    // Update the columns list
    document.getElementById("table-columns-list").innerHTML =
      renderTableColumnsListForImageTable(component);

    // Notify model updated
    notifyModelUpdated();
  }

  /**
   * Set up the nav table layout editor interface
   */
  function setupNavTableLayoutEditor(component) {
    if (!component || component.type !== "nav-table-layout") return;

    // Add both navigation links and table columns sections
    const navTableContainer = document.createElement("div");
    navTableContainer.className = "mt-3";

    // Navigation Links Section
    navTableContainer.innerHTML = `
      <h6 class="border-bottom pb-2">Navigation Links</h6>
      
      <div id="nav-links-list" class="mb-2">
        ${renderNavigationLinksList(component, "navigation.items")}
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
      <div class="card mb-3">
        <div class="card-header py-1 px-2 bg-light">
          <h6 class="mb-0 small">Register Button</h6>
        </div>
        <div class="card-body p-2">
          <div class="mb-2 form-check">
            <input class="form-check-input" type="checkbox" id="include-register-btn" 
              ${
                component.navigation.includeRegisterButton ? "checked" : ""
              } data-property="navigation.includeRegisterButton">
            <label class="form-check-label small" for="include-register-btn">Include "Register" Button</label>
          </div>
          
          <div id="register-button-options" ${
            !component.navigation.includeRegisterButton
              ? 'style="display:none;"'
              : ""
          }>
            <div class="mb-2">
              <label for="register-btn-text" class="form-label small">Button Text</label>
              <input type="text" class="form-control form-control-sm" id="register-btn-text"
                     value="${
                       component.navigation.registerButtonText || "Đăng ký"
                     }" data-property="navigation.registerButtonText">
            </div>
            
            <div class="mb-2">
              <label for="register-btn-class" class="form-label small">Button Color</label>
              <select class="form-select form-select-sm" id="register-btn-class" data-property="navigation.registerButtonClass">
                <option value="btn-primary" ${
                  component.navigation.registerButtonClass === "btn-primary"
                    ? "selected"
                    : ""
                }>Primary (Blue)</option>
                <option value="btn-secondary" ${
                  component.navigation.registerButtonClass === "btn-secondary"
                    ? "selected"
                    : ""
                }>Secondary (Gray)</option>
                <option value="btn-success" ${
                  component.navigation.registerButtonClass === "btn-success"
                    ? "selected"
                    : ""
                }>Success (Green)</option>
                <option value="btn-danger" ${
                  component.navigation.registerButtonClass === "btn-danger"
                    ? "selected"
                    : ""
                }>Danger (Red)</option>
                <option value="btn-warning" ${
                  component.navigation.registerButtonClass === "btn-warning"
                    ? "selected"
                    : ""
                }>Warning (Yellow)</option>
                <option value="btn-info" ${
                  component.navigation.registerButtonClass === "btn-info"
                    ? "selected"
                    : ""
                }>Info (Cyan)</option>
              </select>
            </div>
            
            <div class="mb-2">
              <label for="register-btn-size" class="form-label small">Button Size</label>
              <select class="form-select form-select-sm" id="register-btn-size" data-property="navigation.registerButtonSize">
                <option value="" ${
                  component.navigation.registerButtonSize === ""
                    ? "selected"
                    : ""
                }>Default</option>
                <option value="btn-sm" ${
                  component.navigation.registerButtonSize === "btn-sm"
                    ? "selected"
                    : ""
                }>Small</option>
                <option value="btn-lg" ${
                  component.navigation.registerButtonSize === "btn-lg"
                    ? "selected"
                    : ""
                }>Large</option>
              </select>
            </div>
            
            <div class="mt-2">
              <span class="small">Preview:</span>
              <div class="border rounded p-2 mt-1 text-center">
                <button class="btn ${
                  component.navigation.registerButtonClass
                } ${
      component.navigation.registerButtonSize
    } preview-register-btn">
                  ${component.navigation.registerButtonText || "Đăng ký"}
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Table Columns Section -->
      <h6 class="border-bottom pb-2 mt-4">Table Columns</h6>
      
      <div id="table-columns-list" class="mb-2">
        ${renderTableColumnsListForLayout(component)}
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
      
      <!-- Layout preview -->
      <h6 class="border-bottom pb-2 mt-4">Layout Preview</h6>
      <div class="layout-preview p-2 border rounded mb-3">
        <div class="d-flex align-items-start ${
          component.navigation.position === "left" ? "" : "flex-row-reverse"
        }">
          <div class="${getNavColumnClass(component)} p-2 border-end bg-light">
            <div class="small mb-2">Navigation</div>
            <div class="small">${component.navigation.items
              .map((item) => item.text)
              .slice(0, 3)
              .join("<br>")}</div>
            <div class="small mt-2">...</div>
            ${
              component.navigation.includeRegisterButton
                ? `<button class="btn btn-sm ${component.navigation.registerButtonClass} mt-2" style="font-size:0.7rem;">
                 ${component.navigation.registerButtonText}
               </button>`
                : ""
            }
          </div>
          <div class="flex-grow-1 p-2 ms-2 bg-light">
            <div class="small mb-2">Table: ${component.table.title}</div>
            <div class="table-responsive">
              <table class="table table-sm ${
                component.table.showBorder ? "table-bordered" : ""
              }" style="font-size:0.7rem">
                <thead>
                  <tr>
                    ${component.table.columns
                      .slice(0, 3)
                      .map(
                        (col) =>
                          `<th>${
                            typeof col === "string" ? col : col.headerText
                          }</th>`
                      )
                      .join("")}
                    ${component.table.columns.length > 3 ? "<th>...</th>" : ""}
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    ${component.table.columns
                      .slice(0, 3)
                      .map(() => "<td>Data</td>")
                      .join("")}
                    ${component.table.columns.length > 3 ? "<td>...</td>" : ""}
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    `;

    elements.specificPropsContainer.appendChild(navTableContainer);

    // Add event listener for Add Link button
    const addLinkBtn = navTableContainer.querySelector("#add-nav-link-btn");
    addLinkBtn.addEventListener("click", function () {
      addNavigationLinkToLayout(component);
    });

    // Add event listener for Add Column button
    const addColumnBtn = navTableContainer.querySelector(
      "#add-table-column-btn"
    );
    addColumnBtn.addEventListener("click", function () {
      addColumnToLayout(component);
    });

    // Add event listener for register button checkbox
    const registerBtn = navTableContainer.querySelector(
      "#include-register-btn"
    );
    registerBtn.addEventListener("change", function () {
      const options = navTableContainer.querySelector(
        "#register-button-options"
      );
      if (options) {
        options.style.display = this.checked ? "" : "none";
      }
    });

    // Set up event listeners for existing action buttons
    setupNavTableLayoutEventListeners(navTableContainer, component);
  }

  // Helper function to get appropriate CSS class for nav column width
  function getNavColumnClass(component) {
    switch (component.columnClasses.navCol) {
      case "col-md-3":
        return "w-25";
      case "col-md-4":
        return "w-33";
      case "col-md-5":
        return "w-40";
      default:
        return "w-25";
    }
  }

  /**
   * Render the navigation links list for layout components
   */
  function renderNavigationLinksList(component, propertyPath = "items") {
    // Extract items from the property path
    const pathParts = propertyPath.split(".");
    let items;

    if (pathParts.length === 1) {
      items = component[pathParts[0]];
    } else if (pathParts.length === 2) {
      items = component[pathParts[0]][pathParts[1]];
    }

    if (!items || items.length === 0) {
      return '<p class="text-muted small">No navigation links defined</p>';
    }

    return `
      <div class="list-group">
        ${items
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
          </div>
        `
          )
          .join("")}
      </div>
    `;
  }

  /**
   * Render the table columns list for layout components
   */
  function renderTableColumnsListForLayout(component) {
    if (!component.table.columns || component.table.columns.length === 0) {
      return '<p class="text-muted small">No table columns defined</p>';
    }

    return `
      <div class="list-group">
        ${component.table.columns
          .map((column, index) => {
            const headerText =
              typeof column === "string"
                ? column
                : column.headerText || "Untitled";

            return `
            <div class="list-group-item p-2">
              <div class="d-flex justify-content-between align-items-center">
                <span class="fw-bold small">${headerText}</span>
                <div>
                  <button class="btn btn-sm btn-outline-primary edit-table-column-btn" 
                    data-index="${index}" title="Edit">
                    <i class="bi bi-pencil"></i>
                  </button>
                  <button class="btn btn-sm btn-outline-danger delete-table-column-btn" 
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
   * Add a navigation link to a layout component
   */
  function addNavigationLinkToLayout(component) {
    // Get values from the form inputs
    const textInput = document.getElementById("new-link-text");
    const urlInput = document.getElementById("new-link-url");

    const text = textInput.value.trim();
    const url = urlInput.value.trim() || "#";

    // Basic validation
    if (!text) {
      alert("Link text cannot be empty");
      return;
    }

    // Make a copy of current items and add the new link
    const items = [...(component.navigation.items || [])];
    items.push({ text, url });

    // Update the component in the model
    window.pageModelManager.updateComponent(component.id, {
      navigation: { ...component.navigation, items },
    });

    // Clear the form
    textInput.value = "";
    urlInput.value = "";

    // Update the links list
    document.getElementById("nav-links-list").innerHTML =
      renderNavigationLinksList(component, "navigation.items");

    // Notify model updated
    notifyModelUpdated();
  }

  /**
   * Edit a navigation link in a layout component
   */
  function editNavigationLinkInLayout(component, index) {
    if (
      !component ||
      !component.navigation.items ||
      index >= component.navigation.items.length
    )
      return;

    const link = component.navigation.items[index];

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
    }

    // Set current values
    document.getElementById("edit-link-text").value = link.text || "";
    document.getElementById("edit-link-url").value = link.url || "#";

    // Handle save button click - fixed to work with persistent modals
    const saveBtn = document.getElementById("save-link-changes-btn");

    // Clean up previous event listeners to prevent duplicates
    if (saveBtn._clickHandler) {
      saveBtn.removeEventListener("click", saveBtn._clickHandler);
    }

    // Create a new handler function
    saveBtn._clickHandler = function () {
      const text = document.getElementById("edit-link-text").value.trim();
      const url = document.getElementById("edit-link-url").value.trim() || "#";

      if (!text) {
        alert("Link text cannot be empty");
        return;
      }

      // Make a copy and update the link
      const items = [...component.navigation.items];
      items[index] = { text, url };

      // Update the component in the model
      window.pageModelManager.updateComponent(component.id, {
        navigation: { ...component.navigation, items },
      });

      // Update the links list
      document.getElementById("nav-links-list").innerHTML =
        renderNavigationLinksList(component, "navigation.items");

      // Notify model updated
      notifyModelUpdated();

      // Hide the modal
      const bsModal = bootstrap.Modal.getInstance(
        document.getElementById(modalId)
      );
      bsModal.hide();
    };

    // Add the new event listener
    saveBtn.addEventListener("click", saveBtn._clickHandler);

    // Show the modal
    const bsModal = new bootstrap.Modal(document.getElementById(modalId));
    bsModal.show();
  }

  /**
   * Delete a navigation link from a layout component
   */
  function deleteNavigationLinkFromLayout(component, index) {
    if (
      !component ||
      !component.navigation.items ||
      index >= component.navigation.items.length
    )
      return;

    // Confirmation
    if (
      !confirm(
        `Are you sure you want to delete the link "${component.navigation.items[index].text}"?`
      )
    ) {
      return;
    }

    // Make a copy of items and remove the link
    const items = [...component.navigation.items];
    items.splice(index, 1);

    // Update the component in the model
    window.pageModelManager.updateComponent(component.id, {
      navigation: { ...component.navigation, items },
    });

    // Update the links list
    document.getElementById("nav-links-list").innerHTML =
      renderNavigationLinksList(component, "navigation.items");

    // Notify model updated
    notifyModelUpdated();
  }

  /**
   * Add a table column to a layout component
   */
  function addColumnToLayout(component) {
    // Get value from the form input
    const textInput = document.getElementById("new-column-text");
    const headerText = textInput.value.trim();

    // Basic validation
    if (!headerText) {
      alert("Column header cannot be empty");
      textInput.focus();
      return;
    }

    // Convert existing columns to objects if they're strings
    let columns = [...(component.table.columns || [])].map((col) =>
      typeof col === "string" ? { headerText: col } : col
    );

    // Add the new column
    columns.push({ headerText });

    // Update the component in the model
    window.pageModelManager.updateComponent(component.id, {
      table: { ...component.table, columns },
    });

    // Clear the form
    textInput.value = "";

    // Update the columns list
    document.getElementById("table-columns-list").innerHTML =
      renderTableColumnsListForLayout(component);

    // Notify model updated
    notifyModelUpdated();
  }

  /**
   * Edit a table column in a layout component
   */
  function editColumnInLayout(component, index) {
    if (
      !component ||
      !component.table.columns ||
      index >= component.table.columns.length
    )
      return;

    // Get the column (handle both string and object formats)
    const column = component.table.columns[index];
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
    }

    // Set current value
    document.getElementById("edit-column-text").value = currentHeaderText;

    // Handle save button click
    const saveBtn = document.getElementById("save-column-changes-btn");

    // Clean up previous event listeners to prevent duplicates
    if (saveBtn._clickHandler) {
      saveBtn.removeEventListener("click", saveBtn._clickHandler);
    }

    // Create a new handler function
    saveBtn._clickHandler = function () {
      const headerText = document
        .getElementById("edit-column-text")
        .value.trim();

      if (!headerText) {
        alert("Column header cannot be empty");
        return;
      }

      // Convert columns to objects if needed and update the column
      let columns = [...component.table.columns].map((col, i) => {
        if (i === index) {
          return { headerText };
        } else {
          return typeof col === "string" ? { headerText: col } : col;
        }
      });

      // Update the component in the model
      window.pageModelManager.updateComponent(component.id, {
        table: { ...component.table, columns },
      });

      // Update the columns list
      document.getElementById("table-columns-list").innerHTML =
        renderTableColumnsListForLayout(component);

      // Notify model updated
      notifyModelUpdated();

      // Hide the modal
      bootstrap.Modal.getInstance(document.getElementById(modalId)).hide();
    };

    // Add the new event listener
    saveBtn.addEventListener("click", saveBtn._clickHandler);

    // Show the modal
    const bsModal = new bootstrap.Modal(document.getElementById(modalId));
    bsModal.show();
  }

  /**
   * Delete a table column from a layout component
   */
  function deleteColumnFromLayout(component, index) {
    if (
      !component ||
      !component.table.columns ||
      index >= component.table.columns.length
    )
      return;

    const column = component.table.columns[index];
    const headerText = typeof column === "string" ? column : column.headerText;

    // Confirmation
    if (
      !confirm(`Are you sure you want to delete the column "${headerText}"?`)
    ) {
      return;
    }

    // Remove the column
    const columns = [...component.table.columns];
    columns.splice(index, 1);

    // Update the component in the model
    window.pageModelManager.updateComponent(component.id, {
      table: { ...component.table, columns },
    });

    // Update the columns list
    document.getElementById("table-columns-list").innerHTML =
      renderTableColumnsListForLayout(component);

    // Notify model updated
    notifyModelUpdated();
  }

  /**
   * Set up event listeners for nav-table layout editor
   */
  function setupNavTableLayoutEventListeners(container, component) {
    // Edit link buttons
    const editLinkBtns = container.querySelectorAll(".edit-nav-link-btn");
    editLinkBtns.forEach((btn) => {
      btn.addEventListener("click", function () {
        const index = parseInt(this.getAttribute("data-index"));
        editNavigationLinkInLayout(component, index);
      });
    });

    // Delete link buttons
    const deleteLinkBtns = container.querySelectorAll(".delete-nav-link-btn");
    deleteLinkBtns.forEach((btn) => {
      btn.addEventListener("click", function () {
        const index = parseInt(this.getAttribute("data-index"));
        deleteNavigationLinkFromLayout(component, index);
      });
    });

    // Edit column buttons
    const editColumnBtns = container.querySelectorAll(".edit-table-column-btn");
    editColumnBtns.forEach((btn) => {
      btn.addEventListener("click", function () {
        const index = parseInt(this.getAttribute("data-index"));
        editColumnInLayout(component, index);
      });
    });

    // Delete column buttons
    const deleteColumnBtns = container.querySelectorAll(
      ".delete-table-column-btn"
    );
    deleteColumnBtns.forEach((btn) => {
      btn.addEventListener("click", function () {
        const index = parseInt(this.getAttribute("data-index"));
        deleteColumnFromLayout(component, index);
      });
    });
  }

  // Initialize when DOM is fully loaded
  if (document.readyState === "loading") {
    // Loading hasn't finished yet
    document.addEventListener("DOMContentLoaded", init);
  } else {
    // `DOMContentLoaded` has already fired
    init();
  }
})(); // End of the IIFE
