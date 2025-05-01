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

  // Initialize when DOM is fully loaded
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
