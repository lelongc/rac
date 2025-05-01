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

    fieldEditor.style.display = "block";
    fieldEditor.innerHTML = `
            <h6 class="mb-2">${field.id ? "Edit Field" : "Add New Field"}</h6>
            
            <div class="mb-2">
                <label for="field-label" class="form-label small">Label</label>
                <input type="text" class="form-control form-control-sm" id="field-label" 
                    value="${field.label || ""}" data-field-prop="label">
            </div>
            
            <div class="mb-2">
                <label for="field-id" class="form-label small">ID</label>
                <input type="text" class="form-control form-control-sm" id="field-id" 
                    value="${field.id || ""}" data-field-prop="id">
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
                    <option value="select" ${
                      field.type === "select" ? "selected" : ""
                    }>Select/Dropdown</option>
                    <option value="checkbox" ${
                      field.type === "checkbox" ? "selected" : ""
                    }>Checkbox</option>
                    <option value="radio" ${
                      field.type === "radio" ? "selected" : ""
                    }>Radio</option>
                </select>
            </div>
            
            <div class="mb-2">
                <label for="field-placeholder" class="form-label small">Placeholder</label>
                <input type="text" class="form-control form-control-sm" id="field-placeholder" 
                    value="${
                      field.placeholder || ""
                    }" data-field-prop="placeholder">
            </div>
            
            <div class="mb-2 form-check">
                <input type="checkbox" class="form-check-input" id="field-required" 
                    ${
                      field.required ? "checked" : ""
                    } data-field-prop="required">
                <label class="form-check-label small" for="field-required">Required Field</label>
            </div>
            
            <div class="mb-2 form-check">
                <input type="checkbox" class="form-check-input" id="field-validation" 
                    ${
                      field.validation ? "checked" : ""
                    } data-field-prop="validation">
                <label class="form-check-label small" for="field-validation">Enable Validation</label>
            </div>
            
            <div class="d-flex justify-content-end mt-3">
                <button id="cancel-field-editor-btn" class="btn btn-sm btn-outline-secondary me-2">Cancel</button>
                <button id="save-form-field-btn" class="btn btn-sm btn-primary">Save Field</button>
            </div>
        `;

    // Add event listeners for the field editor inputs
    const inputs = fieldEditor.querySelectorAll("[data-field-prop]");
    inputs.forEach((input) => {
      input.addEventListener("change", function () {
        const prop = this.getAttribute("data-field-prop");
        let value;

        if (this.type === "checkbox") {
          value = this.checked;
        } else {
          value = this.value;
        }

        if (state.currentEditingField) {
          state.currentEditingField[prop] = value;
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

  // Initialize when DOM is fully loaded
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
