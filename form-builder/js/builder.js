// Global variables
let formElements = [];
let selectedElement = null;
let nextElementId = 1;
let undoStack = [];
let templateLibrary = {};

// Element class definition
class FormElement {
  constructor(type) {
    this.id = `element_${nextElementId++}`;
    this.type = type;
    this.properties = this.getDefaultProperties(type);
  }

  getDefaultProperties(type) {
    const commonProps = {
      label: "Label",
      required: false,
      classes: "",
    };

    switch (type) {
      case "header":
        return {
          imageUrl: "../image/website.png",
          altText: "Header Banner",
          height: "200px",
        };
      case "navbar":
        return {
          brand: "Website Brand",
          items: [
            { text: "Home", url: "#", active: true },
            { text: "About", url: "#", active: false },
            { text: "Contact", url: "#", active: false },
          ],
          variant: "light",
        };
      case "text":
      case "email":
      case "number":
        return {
          ...commonProps,
          placeholder: "Enter value here",
          defaultValue: "",
          helperText: "",
        };
      case "date":
        return {
          ...commonProps,
          defaultValue: "",
          min: "",
          max: "",
        };
      case "select":
        return {
          ...commonProps,
          options: ["Option 1", "Option 2", "Option 3"],
          defaultValue: "",
        };
      case "radio":
        return {
          ...commonProps,
          options: ["Option 1", "Option 2"],
          inline: false,
          defaultValue: "",
        };
      case "checkbox":
        return {
          ...commonProps,
          options: ["Option 1", "Option 2", "Option 3"],
          inline: false,
        };
      case "button":
        return {
          text: "Submit",
          type: "primary",
          size: "md",
          onClick: 'alert("Button clicked!")',
        };
      case "table":
        return {
          headers: ["ID", "Name", "Email", "Action"],
          bordered: true,
          striped: false,
          hover: true,
        };
      case "footer":
        return {
          text: "© 2023 My Website. All rights reserved.",
          variant: "dark",
        };
      default:
        return commonProps;
    }
  }

  // Additional method to clone an element
  clone() {
    const newElement = new FormElement(this.type);
    newElement.properties = JSON.parse(JSON.stringify(this.properties));
    return newElement;
  }
}

// Save current state to undo stack
function saveToUndoStack() {
  // Deep clone the current elements
  undoStack.push(JSON.stringify(formElements));

  // Enable undo button if there are items in the stack
  const undoBtn = document.getElementById("undoBtn");
  if (undoBtn) {
    undoBtn.disabled = undoStack.length === 0;
  }
}

// Undo last action
function undoLastAction() {
  if (undoStack.length > 0) {
    const previousState = JSON.parse(undoStack.pop());
    formElements = previousState;

    // Re-render the canvas
    refreshCanvas();

    // Update undo button state
    const undoBtn = document.getElementById("undoBtn");
    if (undoBtn) {
      undoBtn.disabled = undoStack.length === 0;
    }
  }
}

// Refresh the entire canvas
function refreshCanvas() {
  const formCanvas = document.getElementById("formCanvas");
  formCanvas.innerHTML = "";

  // Re-render all elements
  formElements.forEach((element) => {
    renderElement(element);
  });

  // Clear selection
  selectedElement = null;
  document.getElementById("propertiesPanel").innerHTML =
    '<p class="text-muted text-center">Select a component to edit its properties</p>';
}

// Duplicate an element
function duplicateElement(elementId) {
  // Save current state for undo
  saveToUndoStack();

  const originalElement = formElements.find((el) => el.id === elementId);
  if (!originalElement) return;

  // Clone the element
  const newElement = originalElement.clone();
  formElements.push(newElement);

  // Render the new element
  renderElement(newElement);

  // Select the new element
  selectElement(newElement.id);
}

// Initialize drag and drop functionality
function initDragAndDrop() {
  const components = document.querySelectorAll(".component-item");
  const formCanvas = document.getElementById("formCanvas");

  components.forEach((component) => {
    component.addEventListener("dragstart", (e) => {
      e.dataTransfer.setData("text/plain", component.dataset.type);
    });
  });

  formCanvas.addEventListener("dragover", (e) => {
    e.preventDefault();
    formCanvas.classList.add("drag-over");
  });

  formCanvas.addEventListener("dragleave", () => {
    formCanvas.classList.remove("drag-over");
  });

  formCanvas.addEventListener("drop", (e) => {
    e.preventDefault();
    formCanvas.classList.remove("drag-over");
    const type = e.dataTransfer.getData("text/plain");
    addElementToCanvas(type);
  });
}

// Add element with specific position on canvas
function addElementToCanvas(type, position = null) {
  // Save current state for undo
  saveToUndoStack();

  const element = new FormElement(type);
  formElements.push(element);
  renderElement(element);
  selectElement(element.id);

  // If position is specified, scroll to that position
  if (position) {
    const canvas = document.getElementById("formCanvas");
    canvas.scrollTo({
      top: position.top,
      left: position.left,
      behavior: "smooth",
    });
  }

  return element;
}

// Render element on canvas
function renderElement(element) {
  const formCanvas = document.getElementById("formCanvas");
  const elementDiv = document.createElement("div");
  elementDiv.className = "canvas-element";
  elementDiv.id = element.id;
  elementDiv.dataset.type = element.type;
  elementDiv.innerHTML = generateElementHTML(element);

  // Add control buttons
  const actionsDiv = document.createElement("div");
  actionsDiv.className = "element-actions btn-group";
  actionsDiv.innerHTML = `
        <button class="btn btn-sm btn-outline-primary" onclick="moveElement('${element.id}', -1)">
            <i class="bi bi-arrow-up"></i>
        </button>
        <button class="btn btn-sm btn-outline-primary" onclick="moveElement('${element.id}', 1)">
            <i class="bi bi-arrow-down"></i>
        </button>
        <button class="btn btn-sm btn-outline-primary" title="Duplicate" onclick="duplicateElement('${element.id}')">
          <i class="bi bi-files"></i>
        </button>
        <button class="btn btn-sm btn-outline-danger" onclick="removeElement('${element.id}')">
            <i class="bi bi-trash"></i>
        </button>
    `;
  elementDiv.appendChild(actionsDiv);

  // Make it selectable
  elementDiv.addEventListener("click", (e) => {
    if (!e.target.closest(".element-actions")) {
      selectElement(element.id);
    }
  });

  formCanvas.appendChild(elementDiv);
}

// Generate HTML for element based on its type and properties
function generateElementHTML(element) {
  const props = element.properties;

  switch (element.type) {
    case "header":
      return `
                <div style="width: 100%; height: ${props.height}; overflow: hidden;">
                    <img src="${props.imageUrl}" alt="${props.altText}" style="width: 100%; height: 100%; object-fit: cover;">
                </div>
            `;

    case "navbar":
      return `
                <nav class="navbar navbar-expand-lg navbar-${
                  props.variant
                } bg-${props.variant}">
                    <div class="container-fluid">
                        <a class="navbar-brand" href="#">${props.brand}</a>
                        <button class="navbar-toggler" type="button">
                            <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse">
                            <ul class="navbar-nav me-auto">
                                ${props.items
                                  .map(
                                    (item) =>
                                      `<li class="nav-item">
                                        <a class="nav-link${
                                          item.active ? " active" : ""
                                        }" href="${item.url}">${item.text}</a>
                                    </li>`
                                  )
                                  .join("")}
                            </ul>
                        </div>
                    </div>
                </nav>
            `;

    case "text":
    case "email":
    case "number":
      return `
                <div class="mb-3 ${props.classes}">
                    <label class="form-label">${props.label}${
        props.required ? ' <span class="text-danger">*</span>' : ""
      }</label>
                    <input type="${
                      element.type
                    }" class="form-control" placeholder="${
        props.placeholder
      }" value="${props.defaultValue}" ${props.required ? "required" : ""}>
                    ${
                      props.helperText
                        ? `<div class="form-text">${props.helperText}</div>`
                        : ""
                    }
                </div>
            `;

    case "date":
      return `
                <div class="mb-3 ${props.classes}">
                    <label class="form-label">${props.label}${
        props.required ? ' <span class="text-danger">*</span>' : ""
      }</label>
                    <input type="date" class="form-control" value="${
                      props.defaultValue
                    }" ${props.min ? 'min="' + props.min + '"' : ""} ${
        props.max ? 'max="' + props.max + '"' : ""
      } ${props.required ? "required" : ""}>
                </div>
            `;

    case "select":
      return `
                <div class="mb-3 ${props.classes}">
                    <label class="form-label">${props.label}${
        props.required ? ' <span class="text-danger">*</span>' : ""
      }</label>
                    <select class="form-select" ${
                      props.required ? "required" : ""
                    }>
                        ${props.options
                          .map(
                            (opt) =>
                              `<option value="${opt}" ${
                                opt === props.defaultValue ? "selected" : ""
                              }>${opt}</option>`
                          )
                          .join("")}
                    </select>
                </div>
            `;

    case "radio":
      return `
                <div class="mb-3 ${props.classes}">
                    <label class="form-label">${props.label}${
        props.required ? ' <span class="text-danger">*</span>' : ""
      }</label>
                    <div>
                        ${props.options
                          .map(
                            (opt, i) => `
                            <div class="form-check ${
                              props.inline ? "form-check-inline" : ""
                            }">
                                <input class="form-check-input" type="radio" name="radio_${
                                  element.id
                                }" id="radio_${
                              element.id
                            }_${i}" value="${opt}" ${
                              opt === props.defaultValue ? "checked" : ""
                            }>
                                <label class="form-check-label" for="radio_${
                                  element.id
                                }_${i}">${opt}</label>
                            </div>
                        `
                          )
                          .join("")}
                    </div>
                </div>
            `;

    case "checkbox":
      return `
                <div class="mb-3 ${props.classes}">
                    <label class="form-label">${props.label}${
        props.required ? ' <span class="text-danger">*</span>' : ""
      }</label>
                    <div>
                        ${props.options
                          .map(
                            (opt, i) => `
                            <div class="form-check ${
                              props.inline ? "form-check-inline" : ""
                            }">
                                <input class="form-check-input" type="checkbox" id="checkbox_${
                                  element.id
                                }_${i}" value="${opt}">
                                <label class="form-check-label" for="checkbox_${
                                  element.id
                                }_${i}">${opt}</label>
                            </div>
                        `
                          )
                          .join("")}
                    </div>
                </div>
            `;

    case "button":
      return `
                <button type="button" class="btn btn-${props.type} btn-${props.size}">${props.text}</button>
            `;

    case "table":
      return `
                <div class="table-responsive">
                    <table class="table ${
                      props.bordered ? "table-bordered" : ""
                    } ${props.striped ? "table-striped" : ""} ${
        props.hover ? "table-hover" : ""
      }">
                        <thead>
                            <tr>
                                ${props.headers
                                  .map((header) => `<th>${header}</th>`)
                                  .join("")}
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                ${props.headers
                                  .map(() => `<td>Sample data</td>`)
                                  .join("")}
                            </tr>
                            <tr>
                                ${props.headers
                                  .map(() => `<td>Sample data</td>`)
                                  .join("")}
                            </tr>
                        </tbody>
                    </table>
                </div>
            `;

    case "footer":
      return `
                <footer class="text-center py-3 mt-4 bg-${props.variant} text-${
        props.variant === "dark" ? "light" : "dark"
      }">
                    ${props.text}
                </footer>
            `;

    default:
      return `<div>Unknown element type: ${element.type}</div>`;
  }
}

// Select an element and show its properties
function selectElement(elementId) {
  // Deselect previously selected element
  if (selectedElement) {
    document.getElementById(selectedElement).classList.remove("border-primary");
  }

  selectedElement = elementId;

  // Highlight the selected element
  const element = document.getElementById(elementId);
  element.classList.add("border-primary");

  // Show its properties
  const elementObj = formElements.find((el) => el.id === elementId);
  showPropertyEditor(elementObj);
}

// Show property editor for selected element
function showPropertyEditor(element) {
  const propertiesPanel = document.getElementById("propertiesPanel");
  propertiesPanel.innerHTML = "";

  if (!element) {
    propertiesPanel.innerHTML =
      '<p class="text-muted text-center">Select a component to edit its properties</p>';
    return;
  }

  const props = element.properties;
  const type = element.type;

  // Add element type header
  const typeHeader = document.createElement("h5");
  typeHeader.textContent = `${
    type.charAt(0).toUpperCase() + type.slice(1)
  } Properties`;
  propertiesPanel.appendChild(typeHeader);

  // Create form for properties based on element type
  const propertiesForm = document.createElement("form");

  switch (type) {
    case "header":
      propertiesForm.innerHTML = `
                <div class="mb-3">
                    <label class="form-label">Image URL</label>
                    <input type="text" class="form-control" id="prop_imageUrl" value="${props.imageUrl}">
                </div>
                <div class="mb-3">
                    <label class="form-label">Alt Text</label>
                    <input type="text" class="form-control" id="prop_altText" value="${props.altText}">
                </div>
                <div class="mb-3">
                    <label class="form-label">Height</label>
                    <input type="text" class="form-control" id="prop_height" value="${props.height}">
                </div>
            `;
      break;

    case "navbar":
      propertiesForm.innerHTML = `
                <div class="mb-3">
                    <label class="form-label">Brand Name</label>
                    <input type="text" class="form-control" id="prop_brand" value="${
                      props.brand
                    }">
                </div>
                <div class="mb-3">
                    <label class="form-label">Variant</label>
                    <select class="form-select" id="prop_variant">
                        <option value="light" ${
                          props.variant === "light" ? "selected" : ""
                        }>Light</option>
                        <option value="dark" ${
                          props.variant === "dark" ? "selected" : ""
                        }>Dark</option>
                    </select>
                </div>
                <div class="mb-3">
                    <label class="form-label">Menu Items (one per line, format: Text|URL|active)</label>
                    <textarea class="form-control" id="prop_items" rows="4">${props.items
                      .map((item) => `${item.text}|${item.url}|${item.active}`)
                      .join("\n")}</textarea>
                </div>
            `;
      break;

    case "text":
    case "email":
    case "number":
      propertiesForm.innerHTML = `
                <div class="mb-3">
                    <label class="form-label">Label</label>
                    <input type="text" class="form-control" id="prop_label" value="${
                      props.label
                    }">
                </div>
                <div class="mb-3">
                    <label class="form-label">Placeholder</label>
                    <input type="text" class="form-control" id="prop_placeholder" value="${
                      props.placeholder
                    }">
                </div>
                <div class="mb-3">
                    <label class="form-label">Default Value</label>
                    <input type="text" class="form-control" id="prop_defaultValue" value="${
                      props.defaultValue
                    }">
                </div>
                <div class="mb-3">
                    <label class="form-label">Helper Text</label>
                    <input type="text" class="form-control" id="prop_helperText" value="${
                      props.helperText
                    }">
                </div>
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="prop_required" ${
                      props.required ? "checked" : ""
                    }>
                    <label class="form-check-label" for="prop_required">Required</label>
                </div>
                <div class="mb-3">
                    <label class="form-label">CSS Classes</label>
                    <input type="text" class="form-control" id="prop_classes" value="${
                      props.classes
                    }">
                </div>
            `;
      break;

    case "date":
      propertiesForm.innerHTML = `
                <div class="mb-3">
                    <label class="form-label">Label</label>
                    <input type="text" class="form-control" id="prop_label" value="${
                      props.label
                    }">
                </div>
                <div class="mb-3">
                    <label class="form-label">Default Value</label>
                    <input type="date" class="form-control" id="prop_defaultValue" value="${
                      props.defaultValue
                    }">
                </div>
                <div class="mb-3">
                    <label class="form-label">Min Date</label>
                    <input type="date" class="form-control" id="prop_min" value="${
                      props.min
                    }">
                </div>
                <div class="mb-3">
                    <label class="form-label">Max Date</label>
                    <input type="date" class="form-control" id="prop_max" value="${
                      props.max
                    }">
                </div>
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="prop_required" ${
                      props.required ? "checked" : ""
                    }>
                    <label class="form-check-label" for="prop_required">Required</label>
                </div>
                <div class="mb-3">
                    <label class="form-label">CSS Classes</label>
                    <input type="text" class="form-control" id="prop_classes" value="${
                      props.classes
                    }">
                </div>
            `;
      break;

    case "select":
      propertiesForm.innerHTML = `
                <div class="mb-3">
                    <label class="form-label">Label</label>
                    <input type="text" class="form-control" id="prop_label" value="${
                      props.label
                    }">
                </div>
                <div class="mb-3">
                    <label class="form-label">Options (one per line)</label>
                    <textarea class="form-control" id="prop_options" rows="4">${props.options.join(
                      "\n"
                    )}</textarea>
                </div>
                <div class="mb-3">
                    <label class="form-label">Default Value</label>
                    <input type="text" class="form-control" id="prop_defaultValue" value="${
                      props.defaultValue
                    }">
                </div>
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="prop_required" ${
                      props.required ? "checked" : ""
                    }>
                    <label class="form-check-label" for="prop_required">Required</label>
                </div>
                <div class="mb-3">
                    <label class="form-label">CSS Classes</label>
                    <input type="text" class="form-control" id="prop_classes" value="${
                      props.classes
                    }">
                </div>
            `;
      break;

    case "radio":
      propertiesForm.innerHTML = `
                <div class="mb-3">
                    <label class="form-label">Label</label>
                    <input type="text" class="form-control" id="prop_label" value="${
                      props.label
                    }">
                </div>
                <div class="mb-3">
                    <label class="form-label">Options (one per line)</label>
                    <textarea class="form-control" id="prop_options" rows="4">${props.options.join(
                      "\n"
                    )}</textarea>
                </div>
                <div class="mb-3">
                    <label class="form-label">Default Value</label>
                    <input type="text" class="form-control" id="prop_defaultValue" value="${
                      props.defaultValue
                    }">
                </div>
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="prop_inline" ${
                      props.inline ? "checked" : ""
                    }>
                    <label class="form-check-label" for="prop_inline">Inline Display</label>
                </div>
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="prop_required" ${
                      props.required ? "checked" : ""
                    }>
                    <label class="form-check-label" for="prop_required">Required</label>
                </div>
                <div class="mb-3">
                    <label class="form-label">CSS Classes</label>
                    <input type="text" class="form-control" id="prop_classes" value="${
                      props.classes
                    }">
                </div>
            `;
      break;

    case "checkbox":
      propertiesForm.innerHTML = `
                <div class="mb-3">
                    <label class="form-label">Label</label>
                    <input type="text" class="form-control" id="prop_label" value="${
                      props.label
                    }">
                </div>
                <div class="mb-3">
                    <label class="form-label">Options (one per line)</label>
                    <textarea class="form-control" id="prop_options" rows="4">${props.options.join(
                      "\n"
                    )}</textarea>
                </div>
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="prop_inline" ${
                      props.inline ? "checked" : ""
                    }>
                    <label class="form-check-label" for="prop_inline">Inline Display</label>
                </div>
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="prop_required" ${
                      props.required ? "checked" : ""
                    }>
                    <label class="form-check-label" for="prop_required">Required</label>
                </div>
                <div class="mb-3">
                    <label class="form-label">CSS Classes</label>
                    <input type="text" class="form-control" id="prop_classes" value="${
                      props.classes
                    }">
                </div>
            `;
      break;

    case "button":
      propertiesForm.innerHTML = `
                <div class="mb-3">
                    <label class="form-label">Button Text</label>
                    <input type="text" class="form-control" id="prop_text" value="${
                      props.text
                    }">
                </div>
                <div class="mb-3">
                    <label class="form-label">Button Type</label>
                    <select class="form-select" id="prop_type">
                        <option value="primary" ${
                          props.type === "primary" ? "selected" : ""
                        }>Primary</option>
                        <option value="secondary" ${
                          props.type === "secondary" ? "selected" : ""
                        }>Secondary</option>
                        <option value="success" ${
                          props.type === "success" ? "selected" : ""
                        }>Success</option>
                        <option value="danger" ${
                          props.type === "danger" ? "selected" : ""
                        }>Danger</option>
                        <option value="warning" ${
                          props.type === "warning" ? "selected" : ""
                        }>Warning</option>
                        <option value="info" ${
                          props.type === "info" ? "selected" : ""
                        }>Info</option>
                    </select>
                </div>
                <div class="mb-3">
                    <label class="form-label">Size</label>
                    <select class="form-select" id="prop_size">
                        <option value="sm" ${
                          props.size === "sm" ? "selected" : ""
                        }>Small</option>
                        <option value="md" ${
                          props.size === "md" ? "selected" : ""
                        }>Medium</option>
                        <option value="lg" ${
                          props.size === "lg" ? "selected" : ""
                        }>Large</option>
                    </select>
                </div>
                <div class="mb-3">
                    <label class="form-label">onClick Event</label>
                    <textarea class="form-control" id="prop_onClick" rows="2">${
                      props.onClick
                    }</textarea>
                </div>
            `;
      break;

    case "table":
      propertiesForm.innerHTML = `
                <div class="mb-3">
                    <label class="form-label">Headers (comma separated)</label>
                    <input type="text" class="form-control" id="prop_headers" value="${props.headers.join(
                      ", "
                    )}">
                </div>
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="prop_bordered" ${
                      props.bordered ? "checked" : ""
                    }>
                    <label class="form-check-label" for="prop_bordered">Bordered</label>
                </div>
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="prop_striped" ${
                      props.striped ? "checked" : ""
                    }>
                    <label class="form-check-label" for="prop_striped">Striped</label>
                </div>
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="prop_hover" ${
                      props.hover ? "checked" : ""
                    }>
                    <label class="form-check-label" for="prop_hover">Hover Effect</label>
                </div>
            `;
      break;

    case "footer":
      propertiesForm.innerHTML = `
                <div class="mb-3">
                    <label class="form-label">Footer Text</label>
                    <textarea class="form-control" id="prop_text" rows="3">${
                      props.text
                    }</textarea>
                </div>
                <div class="mb-3">
                    <label class="form-label">Variant</label>
                    <select class="form-select" id="prop_variant">
                        <option value="light" ${
                          props.variant === "light" ? "selected" : ""
                        }>Light</option>
                        <option value="dark" ${
                          props.variant === "dark" ? "selected" : ""
                        }>Dark</option>
                    </select>
                </div>
            `;
      break;
  }

  // Add save button
  const saveButton = document.createElement("button");
  saveButton.type = "button";
  saveButton.className = "btn btn-primary mt-2";
  saveButton.textContent = "Apply Changes";
  saveButton.onclick = () => updateElementProperties(element.id);
  propertiesForm.appendChild(saveButton);

  propertiesPanel.appendChild(propertiesForm);
}

// Update element properties from editor with enhanced error checking
function updateElementProperties(elementId) {
  const element = formElements.find((el) => el.id === elementId);
  if (!element) return;

  // Save current state for undo
  saveToUndoStack();

  const type = element.type;
  const props = element.properties;

  try {
    // Get property values based on element type
    switch (type) {
      case "header":
        props.imageUrl = document.getElementById("prop_imageUrl").value;
        props.altText = document.getElementById("prop_altText").value;
        props.height = document.getElementById("prop_height").value;
        break;

      case "navbar":
        props.brand = document.getElementById("prop_brand").value;
        props.variant = document.getElementById("prop_variant").value;

        // Parse items from textarea
        const itemsText = document.getElementById("prop_items").value;
        props.items = itemsText.split("\n").map((line) => {
          const [text = "", url = "#", active = false] = line.split("|");
          return { text, url, active: active === "true" };
        });
        break;

      case "text":
      case "email":
      case "number":
        props.label = document.getElementById("prop_label").value;
        props.placeholder = document.getElementById("prop_placeholder").value;
        props.defaultValue = document.getElementById("prop_defaultValue").value;
        props.helperText = document.getElementById("prop_helperText").value;
        props.required = document.getElementById("prop_required").checked;
        props.classes = document.getElementById("prop_classes").value;
        break;

      case "date":
        props.label = document.getElementById("prop_label").value;
        props.defaultValue = document.getElementById("prop_defaultValue").value;
        props.min = document.getElementById("prop_min").value;
        props.max = document.getElementById("prop_max").value;
        props.required = document.getElementById("prop_required").checked;
        props.classes = document.getElementById("prop_classes").value;
        break;

      case "select":
        props.label = document.getElementById("prop_label").value;
        props.options = document
          .getElementById("prop_options")
          .value.split("\n")
          .filter((opt) => opt.trim());
        props.defaultValue = document.getElementById("prop_defaultValue").value;
        props.required = document.getElementById("prop_required").checked;
        props.classes = document.getElementById("prop_classes").value;
        break;

      case "radio":
        props.label = document.getElementById("prop_label").value;
        props.options = document
          .getElementById("prop_options")
          .value.split("\n")
          .filter((opt) => opt.trim());
        props.defaultValue = document.getElementById("prop_defaultValue").value;
        props.inline = document.getElementById("prop_inline").checked;
        props.required = document.getElementById("prop_required").checked;
        props.classes = document.getElementById("prop_classes").value;
        break;

      case "checkbox":
        props.label = document.getElementById("prop_label").value;
        props.options = document
          .getElementById("prop_options")
          .value.split("\n")
          .filter((opt) => opt.trim());
        props.inline = document.getElementById("prop_inline").checked;
        props.required = document.getElementById("prop_required").checked;
        props.classes = document.getElementById("prop_classes").value;
        break;

      case "button":
        props.text = document.getElementById("prop_text").value;
        props.type = document.getElementById("prop_type").value;
        props.size = document.getElementById("prop_size").value;
        props.onClick = document.getElementById("prop_onClick").value;
        break;

      case "table":
        props.headers = document
          .getElementById("prop_headers")
          .value.split(",")
          .map((h) => h.trim());
        props.bordered = document.getElementById("prop_bordered").checked;
        props.striped = document.getElementById("prop_striped").checked;
        props.hover = document.getElementById("prop_hover").checked;
        break;

      case "footer":
        props.text = document.getElementById("prop_text").value;
        props.variant = document.getElementById("prop_variant").value;
        break;
    }

    // Re-render the element with updated properties
    const elementDiv = document.getElementById(elementId);
    if (elementDiv) {
      elementDiv.innerHTML = generateElementHTML(element);

      // Re-add the control buttons
      const actionsDiv = document.createElement("div");
      actionsDiv.className = "element-actions btn-group";
      actionsDiv.innerHTML = `
        <button class="btn btn-sm btn-outline-primary" title="Move Up" onclick="moveElement('${elementId}', -1)">
          <i class="bi bi-arrow-up"></i>
        </button>
        <button class="btn btn-sm btn-outline-primary" title="Move Down" onclick="moveElement('${elementId}', 1)">
          <i class="bi bi-arrow-down"></i>
        </button>
        <button class="btn btn-sm btn-outline-primary" title="Duplicate" onclick="duplicateElement('${elementId}')">
          <i class="bi bi-files"></i>
        </button>
        <button class="btn btn-sm btn-outline-danger" title="Delete" onclick="removeElement('${elementId}')">
          <i class="bi bi-trash"></i>
        </button>
      `;
      elementDiv.appendChild(actionsDiv);
    }
  } catch (error) {
    console.error("Error updating properties:", error);
    alert("Failed to update properties. Please check your inputs.");
  }
}

// Remove element from canvas
function removeElement(elementId) {
  // Save current state for undo
  saveToUndoStack();

  document.getElementById(elementId).remove();
  formElements = formElements.filter((el) => el.id !== elementId);

  if (selectedElement === elementId) {
    selectedElement = null;
    document.getElementById("propertiesPanel").innerHTML =
      '<p class="text-muted text-center">Select a component to edit its properties</p>';
  }
}

// Move element up or down
function moveElement(elementId, direction) {
  const element = document.getElementById(elementId);
  const canvas = document.getElementById("formCanvas");

  if (direction < 0 && element.previousElementSibling) {
    canvas.insertBefore(element, element.previousElementSibling);
  } else if (direction > 0 && element.nextElementSibling) {
    canvas.insertBefore(element.nextElementSibling, element);
  }

  // Rearrange the elements array to match the DOM
  const newElements = [];
  document.querySelectorAll(".canvas-element").forEach((el) => {
    const elementId = el.id;
    const elementObj = formElements.find((e) => e.id === elementId);
    if (elementObj) {
      newElements.push(elementObj);
    }
  });
  formElements = newElements;
}

// Enhanced preview functionality with responsive toggle
function showPreview() {
  const previewModal = document.getElementById("previewModal");
  const previewIframe = document.getElementById("previewIframe");

  // Generate complete HTML for the preview
  const previewHTML = generatePreviewHTML();

  // Set the content in the iframe
  const iframeDoc =
    previewIframe.contentDocument || previewIframe.contentWindow.document;
  iframeDoc.open();
  iframeDoc.write(previewHTML);
  iframeDoc.close();

  // Show the modal
  new bootstrap.Modal(previewModal).show();
}

// Generate complete HTML for preview
function generatePreviewHTML() {
  const formCanvas = document.getElementById("formCanvas");

  // Clone canvas content without control buttons
  const clonedContent = formCanvas.cloneNode(true);

  // Remove control buttons and other builder-specific attributes
  clonedContent
    .querySelectorAll(".element-actions")
    .forEach((el) => el.remove());
  clonedContent.querySelectorAll(".canvas-element").forEach((el) => {
    el.classList.remove("canvas-element", "border-primary", "selected");
    el.removeAttribute("id");
  });

  // Generate HTML with all necessary components
  return `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Preview</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
      body {
        padding: 20px 0;
      }
    </style>
</head>
<body>
    <div class="container">
        ${clonedContent.innerHTML}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>`;
}

// Enhanced export code functionality with HTML, CSS, and JS tabs
function exportCode() {
  const exportModal = document.getElementById("exportModal");
  const htmlTab = document.getElementById("htmlCode");
  const cssTab = document.getElementById("cssCode");
  const jsTab = document.getElementById("jsCode");

  // Generate the HTML, CSS and JS code
  const { htmlCode, cssCode, jsCode } = generateExportCode();

  // Display code in respective tabs
  document.getElementById("exportHTML").textContent = htmlCode;
  document.getElementById("exportCSS").textContent = cssCode;
  document.getElementById("exportJS").textContent = jsCode;

  // Show the modal
  new bootstrap.Modal(exportModal).show();
}

// Generate code for export
function generateExportCode() {
  const formCanvas = document.getElementById("formCanvas");

  // Clone canvas content without control buttons
  const clonedContent = formCanvas.cloneNode(true);

  // Remove control buttons and other builder-specific attributes
  clonedContent
    .querySelectorAll(".element-actions")
    .forEach((el) => el.remove());
  clonedContent.querySelectorAll(".canvas-element").forEach((el) => {
    el.classList.remove("canvas-element", "border-primary", "selected");
    el.removeAttribute("id");
  });

  // Generate HTML code
  const htmlCode = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generated Form</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        ${clonedContent.innerHTML}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    <script src="script.js"></script>
</body>
</html>`;

  // Generate CSS code
  const cssCode = `
/* Custom styles for the generated form */
body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f8f9fa;
  padding: 20px 0;
}

.container {
  background-color: #fff;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
  padding: 20px;
}

/* Form element styles */
.form-label {
  font-weight: 500;
}

/* Table styles */
.table {
  margin-bottom: 2rem;
}

/* Footer styles */
footer {
  margin-top: 2rem;
}
`;

  // Generate JavaScript code
  const jsCode = `
// JavaScript for form validation and submission
document.addEventListener('DOMContentLoaded', function() {
  // Get form elements
  const forms = document.querySelectorAll('form');
  
  forms.forEach(form => {
    form.addEventListener('submit', function(event) {
      if (!form.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      } else {
        // Form is valid, you can add custom submission logic here
        alert('Form submitted successfully!');
      }
      
      form.classList.add('was-validated');
    });
  });
  
  // Initialize any components that need JavaScript
  const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
  const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
});
`;

  return { htmlCode, cssCode, jsCode };
}

// Copy code to clipboard
function copyCodeToClipboard() {
  // Determine which tab is active
  const activeTab = document
    .querySelector("#exportTabs .nav-link.active")
    .getAttribute("id");
  let codeElement;

  switch (activeTab) {
    case "html-tab":
      codeElement = document.getElementById("exportHTML");
      break;
    case "css-tab":
      codeElement = document.getElementById("exportCSS");
      break;
    case "js-tab":
      codeElement = document.getElementById("exportJS");
      break;
  }

  if (codeElement) {
    const code = codeElement.textContent;
    navigator.clipboard.writeText(code).then(() => {
      // Create a temporary element for the toast notification
      const toast = document.createElement("div");
      toast.className = "position-fixed bottom-0 end-0 p-3";
      toast.style.zIndex = "5";
      toast.innerHTML = `
        <div class="toast" role="alert" aria-live="assertive" aria-atomic="true">
          <div class="toast-header">
            <strong class="me-auto">Form Builder</strong>
            <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
          </div>
          <div class="toast-body">
            Code copied to clipboard!
          </div>
        </div>
      `;

      document.body.appendChild(toast);
      const toastEl = toast.querySelector(".toast");
      const bsToast = new bootstrap.Toast(toastEl);
      bsToast.show();

      // Remove the toast after it's hidden
      toastEl.addEventListener("hidden.bs.toast", () => {
        document.body.removeChild(toast);
      });
    });
  }
}

// Download the entire website as a ZIP file
function downloadZip() {
  if (typeof JSZip !== "undefined") {
    const zip = new JSZip();

    const { htmlCode, cssCode, jsCode } = generateExportCode();

    // Add files to the zip
    zip.file("index.html", htmlCode);
    zip.file("styles.css", cssCode);
    zip.file("script.js", jsCode);

    // Generate the zip file
    zip.generateAsync({ type: "blob" }).then(function (content) {
      // Create a download link
      const link = document.createElement("a");
      link.href = URL.createObjectURL(content);
      link.download = "form-builder-export.zip";
      link.click();
      URL.revokeObjectURL(link.href);
    });
  } else {
    alert("JSZip library is not loaded. Please include it in your project.");
  }
}

// Clear canvas
function clearCanvas() {
  if (
    confirm(
      "Are you sure you want to clear the canvas? All content will be lost."
    )
  ) {
    document.getElementById("formCanvas").innerHTML = "";
    formElements = [];
    selectedElement = null;
    document.getElementById("propertiesPanel").innerHTML =
      '<p class="text-muted text-center">Select a component to edit its properties</p>';
  }
}

// Save current form as template
function saveAsTemplate() {
  const templateName = document.getElementById("templateName").value.trim();
  if (!templateName) {
    alert("Please enter a template name");
    return;
  }

  const templateDescription = document.getElementById(
    "templateDescription"
  ).value;

  // Save the current form elements as a template
  const template = {
    name: templateName,
    description: templateDescription,
    elements: JSON.stringify(formElements),
    createdAt: new Date().toISOString(),
  };

  // Add to template library
  templateLibrary[templateName] = template;

  // Save to local storage if available
  if (typeof localStorage !== "undefined") {
    try {
      const existingTemplates = JSON.parse(
        localStorage.getItem("formBuilderTemplates") || "{}"
      );
      existingTemplates[templateName] = template;
      localStorage.setItem(
        "formBuilderTemplates",
        JSON.stringify(existingTemplates)
      );
    } catch (e) {
      console.error("Error saving template to localStorage:", e);
    }
  }

  // Close modal
  const modalEl = document.getElementById("saveTemplateModal");
  const modal = bootstrap.Modal.getInstance(modalEl);
  modal.hide();

  // Update template menu
  updateTemplateMenu();

  // Show confirmation
  alert(`Template "${templateName}" saved successfully!`);
}

// Load templates from local storage
function loadTemplates() {
  if (typeof localStorage !== "undefined") {
    try {
      const storedTemplates = JSON.parse(
        localStorage.getItem("formBuilderTemplates") || "{}"
      );
      templateLibrary = storedTemplates;
      updateTemplateMenu();
    } catch (e) {
      console.error("Error loading templates from localStorage:", e);
    }
  }
}

// Update template dropdown menu
function updateTemplateMenu() {
  const templateMenu = document.getElementById("templateMenu");
  if (!templateMenu) return;

  // Clear existing items except for the built-in templates
  const builtInTemplates = Array.from(
    templateMenu.querySelectorAll('[data-template^="builtin-"]')
  );
  templateMenu.innerHTML = "";

  // Re-add built-in templates
  builtInTemplates.forEach((template) => {
    templateMenu.appendChild(template);
  });

  // Add separator if there are custom templates
  if (Object.keys(templateLibrary).length > 0) {
    const separator = document.createElement("li");
    separator.innerHTML = '<hr class="dropdown-divider">';
    templateMenu.appendChild(separator);
  }

  // Add custom templates
  for (const templateName in templateLibrary) {
    const template = templateLibrary[templateName];
    const li = document.createElement("li");
    li.innerHTML = `<a class="dropdown-item" href="#" data-template-name="${templateName}">${templateName}</a>`;
    li.querySelector("a").addEventListener("click", () =>
      loadTemplate(templateName)
    );
    templateMenu.appendChild(li);
  }
}

// Load a template
function loadTemplate(templateName) {
  if (templateName.startsWith("builtin-")) {
    // Load built-in template
    loadBuiltInTemplate(templateName);
  } else if (templateLibrary[templateName]) {
    // Ask for confirmation
    if (formElements.length > 0) {
      if (
        !confirm("Loading a template will replace your current form. Continue?")
      ) {
        return;
      }
    }

    // Save current state for undo
    saveToUndoStack();

    try {
      // Load template from library
      formElements = JSON.parse(templateLibrary[templateName].elements);
      refreshCanvas();
    } catch (e) {
      console.error("Error loading template:", e);
      alert("Failed to load the template.");
    }
  } else {
    alert("Template not found.");
  }
}

// Load built-in template
function loadBuiltInTemplate(templateId) {
  // Ask for confirmation if the canvas is not empty
  if (formElements.length > 0) {
    if (
      !confirm("Loading a template will replace your current form. Continue?")
    ) {
      return;
    }
  }

  // Save current state for undo
  saveToUndoStack();

  // Clear canvas
  formElements = [];

  switch (templateId) {
    case "builtin-registration-form":
      // Add registration form components
      addRegistrationFormTemplate();
      break;
    case "builtin-contact-form":
      // Add contact form components
      addContactFormTemplate();
      break;
    case "builtin-product-page":
      // Add product page components
      addProductPageTemplate();
      break;
    default:
      alert("Built-in template not found.");
      return;
  }

  // Refresh canvas to display the template
  refreshCanvas();
}

// Add registration form template (similar to the provided form)
function addRegistrationFormTemplate() {
  // Create header element
  const header = addElementToCanvas("header");
  header.properties.imageUrl = "../image/website.png";
  header.properties.altText = "GFree English Course Registration";
  header.properties.height = "auto";

  // Create navbar element
  const navbar = addElementToCanvas("navbar");
  navbar.properties.brand = "GFree English course";
  navbar.properties.variant = "light";
  navbar.properties.items = [
    { text: "Trang chủ", url: "#", active: true },
    { text: "Giới thiệu", url: "#", active: false },
    { text: "Khóa học", url: "#", active: false },
  ];

  // Create heading for the form
  const heading = addElementToCanvas("heading");
  heading.properties.text = "Danh sách đăng kí khóa học";
  heading.properties.level = 3;

  // Create table element
  const table = addElementToCanvas("table");
  table.properties.headers = [
    "STT",
    "Họ và tên",
    "Ngày sinh",
    "Số điện thoại",
    "Email",
    "Khóa học",
    "Hình thức học",
    "Kỹ năng cần luyện",
  ];
  table.properties.bordered = true;
  table.properties.hover = true;
  table.properties.striped = false;

  // Create footer element
  const footer = addElementToCanvas("footer");
  footer.properties.text = "© 2023 GFree English. All rights reserved.";
  footer.properties.variant = "primary";
}

// Initialize everything when the document is ready
document.addEventListener("DOMContentLoaded", () => {
  initDragAndDrop();

  // Initialize undo button
  const undoBtn = document.getElementById("undoBtn");
  if (undoBtn) {
    undoBtn.disabled = true;
    undoBtn.addEventListener("click", undoLastAction);
  }

  // Event listeners for buttons
  document.getElementById("previewBtn").addEventListener("click", showPreview);
  document.getElementById("exportBtn").addEventListener("click", exportCode);
  document
    .getElementById("copyCode")
    .addEventListener("click", copyCodeToClipboard);
  document.getElementById("clearCanvas").addEventListener("click", clearCanvas);

  // Event listener for download zip button if it exists
  const downloadZipBtn = document.getElementById("downloadZip");
  if (downloadZipBtn) {
    downloadZipBtn.addEventListener("click", downloadZip);
  }

  // Event listener for save template button if it exists
  const saveTemplateBtn = document.getElementById("saveTemplateBtn");
  if (saveTemplateBtn) {
    saveTemplateBtn.addEventListener("click", () => {
      new bootstrap.Modal(document.getElementById("saveTemplateModal")).show();
    });

    document
      .getElementById("saveTemplate")
      .addEventListener("click", saveAsTemplate);
  }

  // Set up tabs in the export modal
  document.querySelectorAll("#exportTabs .nav-link").forEach((tab) => {
    tab.addEventListener("click", (event) => {
      event.preventDefault();

      // Hide all tab content
      document
        .querySelectorAll("#exportTabs + .tab-content > .tab-pane")
        .forEach((pane) => {
          pane.classList.remove("show", "active");
        });

      // Show selected tab
      const target = document.querySelector(tab.getAttribute("href"));
      target.classList.add("show", "active");

      // Mark tab as active
      document.querySelectorAll("#exportTabs .nav-link").forEach((t) => {
        t.classList.remove("active");
      });
      tab.classList.add("active");
    });
  });

  // Load templates from local storage
  loadTemplates();

  // Add listeners to template menu items
  document.querySelectorAll("[data-template]").forEach((item) => {
    item.addEventListener("click", (e) => {
      e.preventDefault();
      const templateId = item.getAttribute("data-template");
      loadBuiltInTemplate(templateId);
    });
  });

  // Handle HTML view toggle
  const showHTMLSwitch = document.getElementById("showHTMLSwitch");
  if (showHTMLSwitch) {
    showHTMLSwitch.addEventListener("change", function () {
      const propertiesPanel = document.getElementById("propertiesPanel");
      const htmlPanel = document.getElementById("htmlPanel");

      if (this.checked) {
        propertiesPanel.classList.add("d-none");
        htmlPanel.classList.remove("d-none");
        updateHTMLView();
      } else {
        propertiesPanel.classList.remove("d-none");
        htmlPanel.classList.add("d-none");
      }
    });

    // HTML editor apply button
    const applyHTMLBtn = document.getElementById("applyHTML");
    if (applyHTMLBtn) {
      applyHTMLBtn.addEventListener("click", updateElementFromHTML);
    }
  }
});

// Update HTML view of selected element
function updateHTMLView() {
  if (!selectedElement) return;

  const element = formElements.find((el) => el.id === selectedElement);
  if (!element) return;

  const htmlEditor = document.getElementById("htmlEditor");
  const elementDiv = document.getElementById(selectedElement);

  // Remove element actions before getting innerHTML
  const actions = elementDiv.querySelector(".element-actions");
  actions.remove();

  // Get HTML content
  htmlEditor.value = elementDiv.innerHTML;

  // Re-add element actions
  elementDiv.appendChild(actions);
}

// Update element from HTML editor
function updateElementFromHTML() {
  if (!selectedElement) return;

  // Save current state for undo
  saveToUndoStack();

  const htmlEditor = document.getElementById("htmlEditor");
  const elementDiv = document.getElementById(selectedElement);

  // Get actions before replacing HTML
  const actions = elementDiv.querySelector(".element-actions");

  // Update HTML
  elementDiv.innerHTML = htmlEditor.value;

  // Re-add actions
  elementDiv.appendChild(actions);
}

// Create a template from an existing website like the one provided
function createTemplateFromExistingWebsite() {
  formElements = [];

  // Add header with banner
  const header = addElementToCanvas("header");
  header.properties.imageUrl = "../image/website.png";
  header.properties.altText = "Banner";
  header.properties.height = "auto";

  // Add navbar
  const navbar = addElementToCanvas("navbar");
  navbar.properties.brand = "GFree English course";
  navbar.properties.variant = "light";
  navbar.properties.items = [
    { text: "GFree English course", url: "#", active: true },
    { text: "Trang chủ", url: "#", active: false },
    { text: "Giới thiệu", url: "#", active: false },
    { text: "Khóa học", url: "#", active: false },
  ];

  // Add section header
  const sectionHeader = addElementToCanvas("heading");
  sectionHeader.properties.text = "Danh sách đăng kí khóa học";
  sectionHeader.properties.level = 3;

  // Add table
  const table = addElementToCanvas("table");
  table.properties.headers = [
    "STT",
    "Họ và tên",
    "Ngày sinh",
    "Số điện thoại",
    "Email",
    "Khóa học",
    "Hình thức học",
    "Kỹ năng cần luyện",
  ];
  table.properties.bordered = true;
  table.properties.striped = false;
  table.properties.hover = true;

  // Add a button that will trigger the modal
  const buttonElement = addElementToCanvas("button");
  buttonElement.properties.text = "Đăng ký";
  buttonElement.properties.type = "danger";
  buttonElement.properties.size = "sm";

  // Add footer
  const footer = addElementToCanvas("footer");
  footer.properties.text = `
    <h5 class="text-white">Thông tin sinh viên</h5>
    <p>Họ tên: Lê Thanh Long</p>
    <p>Mã sinh viên: 23630851</p>
    <p>Mã lớp: DHKTPM18A</p>
  `;
  footer.properties.variant = "primary";

  // Refresh canvas
  refreshCanvas();
}
