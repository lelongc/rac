document.addEventListener("DOMContentLoaded", function () {
  const componentLibrary = document.getElementById("component-library");
  const previewCanvas = document.getElementById("preview-canvas");
  const propertiesPanelContent = document.getElementById(
    "properties-panel-content"
  ); // Target the inner content div
  const deleteButton = document.getElementById("delete-component-btn");
  const exportHtmlButton = document.getElementById("export-html-btn");
  const htmlOutputTextarea = document.getElementById("html-output");
  const copyHtmlButton = document.getElementById("copy-html-btn");
  const htmlExportModalEl = document.getElementById("htmlExportModal");
  const htmlExportModal = new bootstrap.Modal(htmlExportModalEl); // Initialize modal instance
  const saveLayoutButton = document.getElementById("save-layout-btn");
  const clearLayoutButton = document.getElementById("clear-layout-btn");

  const initialPlaceholderHTML =
    '<p class="text-muted placeholder-text">Kéo thả component từ bên trái vào đây</p>';
  const nestedPlaceholderHTML =
    '<p class="text-muted placeholder-text">Kéo component vào đây</p>';
  const storageKey = "visualBuilderLayout";

  let selectedComponent = null;
  let componentCounter = 0; // To generate unique IDs

  // --- Utility Functions ---
  function generateUniqueId(prefix = "comp") {
    return `${prefix}-${Date.now()}-${componentCounter++}`;
  }

  // Basic function to add placeholder if an element is empty
  function ensurePlaceholder(container, placeholderHtml) {
    if (
      !container.querySelector(":scope > :not(.placeholder-text)") &&
      !container.querySelector(".placeholder-text")
    ) {
      container.insertAdjacentHTML("afterbegin", placeholderHtml);
    } else if (
      container.querySelector(":scope > :not(.placeholder-text)") &&
      container.querySelector(".placeholder-text")
    ) {
      const placeholder = container.querySelector(".placeholder-text");
      if (placeholder) placeholder.remove();
    }
  }

  // --- SortableJS Initialization ---

  function initializeSortable(
    element,
    groupName,
    acceptsFrom = ["shared"],
    isNestableContainer = false
  ) {
    return new Sortable(element, {
      group: {
        name: groupName,
        pull: groupName === "shared-library" ? "clone" : true, // Clone from library, move otherwise
        put: acceptsFrom,
      },
      animation: 150,
      sort: groupName !== "shared-library", // Allow sorting except in library
      filter: ".placeholder-text", // Don't allow dragging the placeholder itself
      fallbackOnBody: true, // Better dragging experience
      swapThreshold: 0.65, // How much needed to swap
      onAdd: function (evt) {
        const itemEl = evt.item;
        const targetContainer = evt.to; // The container where it was dropped
        const componentType = itemEl.getAttribute("data-component-type");
        const fromLibrary = evt.from.id === "component-library"; // Check if dragged from library

        // Remove placeholder from target container
        const placeholder = targetContainer.querySelector(
          ":scope > .placeholder-text"
        );
        if (placeholder) placeholder.remove();

        // --- Handle Component Creation/Moving ---
        if (fromLibrary) {
          // Create new component if dragged from library
          const newComponent = createComponentElement(componentType);
          if (newComponent) {
            targetContainer.replaceChild(newComponent, itemEl); // Replace clone with real element
            makeComponentSelectable(newComponent);
            // Initialize nested sortable if it's a container type
            if (
              newComponent.matches(
                ".preview-form-container, .preview-row-container"
              )
            ) {
              const nestedSortableTarget =
                newComponent.querySelector(".row, form"); // Target the inner .row or form
              if (nestedSortableTarget) {
                initializeNestedSortable(nestedSortableTarget, componentType);
                ensurePlaceholder(nestedSortableTarget, nestedPlaceholderHTML);
              }
            }
            selectComponent(newComponent); // Select the newly added component
          } else {
            itemEl.remove(); // Remove invalid clone
          }
        } else {
          // If moved within/between canvases, the element is already the real one
          // Just ensure it's selectable (might be needed if moved from another context)
          makeComponentSelectable(itemEl);
        }
        ensurePlaceholder(
          targetContainer,
          isNestableContainer ? nestedPlaceholderHTML : initialPlaceholderHTML
        );
        saveLayout(); // Save after adding
      },
      onRemove: function (evt) {
        // Ensure placeholder is added back to the source container if it becomes empty
        ensurePlaceholder(
          evt.from,
          evt.from.classList.contains("row") ||
            evt.from.classList.contains("form")
            ? nestedPlaceholderHTML
            : initialPlaceholderHTML
        );
        saveLayout(); // Save after removing
      },
      onUpdate: function (evt) {
        // Fired when sorting within the list is completed
        saveLayout(); // Save after reordering
      },
      // Add visual feedback for valid drop targets
      onMove: function (evt) {
        // Add class to potential drop target during drag
        if (evt.to !== evt.from) {
          evt.to.classList.add("sortable-ghost-nested");
        }
      },
      onEnd: function (evt) {
        // Clean up visual feedback class
        const potentialTargets = document.querySelectorAll(
          ".sortable-ghost-nested"
        );
        potentialTargets.forEach((el) =>
          el.classList.remove("sortable-ghost-nested")
        );
      },
    });
  }

  // Specific initialization for nested containers (Form, Row)
  function initializeNestedSortable(element, containerType) {
    let acceptsGroup = [];
    let groupName = "";

    if (containerType === "form-container") {
      groupName = "form-fields";
      // Form fields should only accept form elements
      acceptsGroup = ["shared-library", "form-fields"]; // Accept from library or other form containers
    } else if (containerType === "row-container") {
      groupName = "row-content";
      // Rows can accept almost anything (except maybe another row directly? depends on design)
      acceptsGroup = [
        "shared-library",
        "canvas-items",
        "form-fields",
        "row-content",
      ];
    } else {
      return; // Unknown container
    }

    // Filter what can be dropped INSIDE this container
    const nestedSortable = initializeSortable(
      element,
      groupName,
      acceptsGroup,
      true
    );

    // Add a more specific onAdd filter for nested containers
    const originalOnAdd = nestedSortable.options.onAdd;
    nestedSortable.options.onAdd = function (evt) {
      const itemEl = evt.item;
      const componentType = itemEl.getAttribute("data-component-type");
      let allowed = true;

      if (containerType === "form-container") {
        const allowedFormTypes = [
          "text-input",
          "email-input",
          "date-input",
          "select-input",
          "radio-group",
          "checkbox-group",
          "submit-button",
          "paragraph",
        ]; // Allow paragraph inside form too
        if (!allowedFormTypes.includes(componentType)) {
          allowed = false;
          alert(
            "Chỉ các trường form (Input, Select, Button, Paragraph...) mới được kéo vào Form Container."
          );
        }
      } else if (containerType === "row-container") {
        // Example: Prevent nesting a row directly inside another row for simplicity
        if (componentType === "row-container") {
          allowed = false;
          alert(
            "Không thể đặt Row trực tiếp vào trong Row khác (sử dụng Column nếu cần layout phức tạp)."
          );
        }
      }

      if (allowed) {
        // Call the original onAdd logic if the type is allowed
        originalOnAdd.call(this, evt);
      } else {
        // If not allowed, remove the element immediately
        itemEl.remove();
        // Ensure placeholder is back if the drop target is now empty
        ensurePlaceholder(evt.to, nestedPlaceholderHTML);
      }
    };
  }

  // Initialize main library and canvas
  initializeSortable(componentLibrary, "shared-library");
  const mainSortableCanvas = initializeSortable(previewCanvas, "canvas-items", [
    "shared-library",
    "row-content",
    "form-fields",
  ]); // Canvas accepts from library and nested containers

  // --- Component Creation ---
  function createComponentElement(type) {
    const element = document.createElement("div");
    element.classList.add("preview-component");
    element.setAttribute("data-component-type", type);
    element.id = generateUniqueId(type);

    // Default Style Data Attributes (examples)
    element.dataset.bgColor = ""; // Default: transparent
    element.dataset.textColor = ""; // Default: inherit
    element.dataset.padding = "10px"; // Default padding
    element.dataset.marginTop = "0px";
    element.dataset.marginBottom = "10px"; // Default bottom margin

    let innerHTML = "";

    switch (type) {
      // --- Layout ---
      case "row-container":
        element.classList.add("preview-row-container");
        // Bootstrap row needs direct children, so we add the sortable area inside
        innerHTML = `<div class="row"></div>`; // Sortable target will be the .row div
        element.dataset.padding = "0px"; // Row usually doesn't need outer padding
        break;

      // --- Basic ---
      case "header":
        element.classList.add("preview-header", "text-center"); // Removed mb-3, control via margin prop
        innerHTML = `<img src="https://via.placeholder.com/800x150?text=Header+Banner" alt="Header Banner" class="img-fluid">`;
        element.dataset.imgSrc =
          "https://via.placeholder.com/800x150?text=Header+Banner";
        element.dataset.padding = "0px"; // Image usually fills
        element.dataset.marginBottom = "15px";
        break;
      case "paragraph":
        element.classList.add("preview-paragraph");
        innerHTML = `<p>This is a paragraph. Click to edit text.</p>`;
        element.dataset.text = "This is a paragraph. Click to edit text.";
        element.dataset.textColor = "#212529"; // Default Bootstrap text color
        element.dataset.padding = "0px";
        break;
      case "image":
        element.classList.add("preview-image");
        innerHTML = `<img src="https://via.placeholder.com/300x150?text=Image" alt="Placeholder Image" class="img-fluid">`;
        element.dataset.imgSrc =
          "https://via.placeholder.com/300x150?text=Image";
        element.dataset.altText = "Placeholder Image";
        element.dataset.padding = "0px";
        break;
      case "footer":
        element.classList.add("preview-footer", "text-center"); // Base classes
        innerHTML = `<p>Footer Content - &copy; ${new Date().getFullYear()}</p>`;
        element.dataset.text = `Footer Content - &copy; ${new Date().getFullYear()}`;
        element.dataset.bgColor = "#f8f9fa"; // bg-light equivalent
        element.dataset.textColor = "#212529";
        element.dataset.padding = "20px";
        element.dataset.marginTop = "20px";
        element.dataset.marginBottom = "0px";
        break;

      // --- Navigation ---
      case "navbar":
        element.classList.add("preview-navbar");
        innerHTML = `
                    <nav class="navbar navbar-expand-lg navbar-light bg-light">
                      <div class="container-fluid"><a class="navbar-brand" href="#">Navbar</a><button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#${element.id}-nav" aria-controls="${element.id}-nav" aria-expanded="false"><span class="navbar-toggler-icon"></span></button><div class="collapse navbar-collapse" id="${element.id}-nav"><ul class="navbar-nav"><li class="nav-item"><a class="nav-link active" href="#">Home</a></li><li class="nav-item"><a class="nav-link" href="#">Links</a></li></ul></div></div>
                    </nav>`;
        element.dataset.padding = "0px"; // Navbar controls its own padding
        element.dataset.marginBottom = "15px";
        break;

      // --- Form Elements ---
      case "form-container":
        element.classList.add("preview-form-container");
        // Use a <form> tag as the sortable area
        innerHTML = `<form action="#" method="post"></form>`; // Sortable target is the <form>
        element.dataset.action = "#";
        element.dataset.method = "post";
        element.dataset.padding = "15px";
        break;
      case "text-input":
      case "email-input":
      case "date-input":
        const inputType = type.split("-")[0]; // text, email, date
        element.classList.add(`preview-${type}`, "mb-3"); // Use Bootstrap margin bottom
        innerHTML = `
                    <label for="${element.id}-input" class="form-label">Label</label>
                    <input type="${inputType}" class="form-control" id="${element.id}-input" placeholder="Enter value">
                    <small class="text-danger error-message" style="display: none;"></small>`;
        element.dataset.label = "Label";
        element.dataset.placeholder = "Enter value";
        if (type === "email-input")
          element.dataset.placeholder = "name@example.com";
        if (type === "date-input") element.dataset.placeholder = ""; // Date has no placeholder attribute
        element.dataset.required = "false";
        element.dataset.errorMessage = "This field is required.";
        element.dataset.padding = "0px"; // Form group manages padding usually
        element.dataset.marginTop = "0px";
        element.dataset.marginBottom = "0px"; // Handled by mb-3 class
        break;
      case "select-input":
      case "radio-group":
      case "checkbox-group":
        const isSelect = type === "select-input";
        element.classList.add(`preview-${type}`, "mb-3");
        const optionsHTML = `
                     <option value="opt1">Option 1</option>
                     <option value="opt2">Option 2</option>`;
        const checkRadioHTML = `
                     <div class="form-check"><input class="form-check-input" type="radio" name="${element.id}-radio" id="${element.id}-radio1" value="option1"><label class="form-check-label" for="${element.id}-radio1">Option 1</label></div>
                     <div class="form-check"><input class="form-check-input" type="radio" name="${element.id}-radio" id="${element.id}-radio2" value="option2"><label class="form-check-label" for="${element.id}-radio2">Option 2</label></div>`;
        const checkboxHTML = `
                     <div class="form-check"><input class="form-check-input" type="checkbox" value="check1" id="${element.id}-check1"><label class="form-check-label" for="${element.id}-check1">Checkbox 1</label></div>
                     <div class="form-check"><input class="form-check-input" type="checkbox" value="check2" id="${element.id}-check2"><label class="form-check-label" for="${element.id}-check2">Checkbox 2</label></div>`;

        innerHTML = `
                    <label for="${element.id}-${
          isSelect ? "select" : "group"
        }" class="form-label d-block">Group Label</label>
                    ${
                      isSelect
                        ? `<select class="form-select" id="${element.id}-select">${optionsHTML}</select>`
                        : ""
                    }
                    ${
                      type === "radio-group"
                        ? `<div class="options-wrapper">${checkRadioHTML}</div>`
                        : ""
                    }
                     ${
                       type === "checkbox-group"
                         ? `<div class="options-wrapper">${checkboxHTML}</div>`
                         : ""
                     }
                    <small class="text-danger error-message d-block" style="display: none;"></small>`;

        element.dataset.label = "Group Label";
        element.dataset.options = isSelect
          ? "Option 1=opt1\nOption 2=opt2"
          : type === "radio-group"
          ? "Option 1=option1\nOption 2=option2"
          : "Checkbox 1=check1\nCheckbox 2=check2";
        element.dataset.required = "false";
        if (!isSelect) element.dataset.inline = "false";
        element.dataset.errorMessage = "Please make a selection.";
        element.dataset.padding = "0px";
        element.dataset.marginTop = "0px";
        element.dataset.marginBottom = "0px"; // mb-3 class handles it
        break;
      case "submit-button":
        element.classList.add("preview-submit-button");
        innerHTML = `<button type="submit" class="btn btn-primary">Submit</button>`;
        element.dataset.text = "Submit";
        element.dataset.btnClass = "btn-primary"; // Store only the style class
        element.dataset.padding = "0px"; // Button padding is internal
        element.dataset.marginTop = "15px"; // Add margin top by default
        break;
      default:
        console.warn("Unknown component type:", type);
        return null;
    }

    element.innerHTML = innerHTML;
    // Apply initial styles from data attributes
    updateComponentVisuals(element);
    return element;
  }

  // --- Selection & Properties ---

  function makeComponentSelectable(componentEl) {
    // Prevent adding listener multiple times
    if (componentEl.dataset.selectableInitialized) return;
    componentEl.dataset.selectableInitialized = "true";

    componentEl.addEventListener("click", function (event) {
      event.stopPropagation(); // Critical to prevent selecting parent when clicking child

      const clickedInsideInteractive = event.target.matches(
        "input, button, select, textarea, a, .form-check-input, .form-check-label"
      );
      const isDirectTarget =
        event.target === componentEl ||
        event.target.parentElement === componentEl ||
        event.target.closest(".preview-component") === componentEl;

      // Select if click is not on an interactive element OR if clicking the component background/non-interactive part directly
      if (
        isDirectTarget &&
        (!clickedInsideInteractive ||
          event.target.matches("label.form-label, p, img, div.row"))
      ) {
        selectComponent(componentEl);
      } else if (!isDirectTarget) {
        // If click somehow bubbles but target is outside, do nothing or deselect
      }
    });
  }

  function selectComponent(componentEl) {
    if (selectedComponent === componentEl) return; // Already selected

    if (selectedComponent) {
      selectedComponent.classList.remove("selected");
    }

    selectedComponent = componentEl;
    if (selectedComponent) {
      selectedComponent.classList.add("selected");
      displayProperties(selectedComponent);
      deleteButton.style.display = "inline-block";
    } else {
      propertiesPanelContent.innerHTML =
        '<p class="text-muted">Chọn một component trong Preview để chỉnh sửa thuộc tính.</p>';
      deleteButton.style.display = "none";
    }
  }

  function displayProperties(componentEl) {
    propertiesPanelContent.innerHTML = ""; // Clear previous properties
    const componentType = componentEl.getAttribute("data-component-type");
    const data = componentEl.dataset; // Access data attributes

    // --- Property Grouping ---
    const addGroupHeader = (title) => {
      propertiesPanelContent.insertAdjacentHTML(
        "beforeend",
        `<h6>${title}</h6>`
      );
    };

    // --- Content Properties ---
    addGroupHeader("Content");
    switch (componentType) {
      case "header":
      case "image":
        addPropertyInput("Image Source (URL)", "imgSrc", "url");
        addPropertyInput("Alt Text", "altText");
        break;
      case "paragraph":
        addPropertyInput("Text Content (HTML)", "text", "textarea");
        break;
      case "footer":
        addPropertyInput("Footer Text (HTML)", "text", "textarea");
        break;
      case "navbar":
        // Basic placeholder - Navbar config is complex
        propertiesPanelContent.insertAdjacentHTML(
          "beforeend",
          "<p><small>Navbar content (brand, links) requires more advanced editing.</small></p>"
        );
        break;
      case "form-container":
        addPropertyInput("Form Action URL", "action", "url");
        addPropertyInput("Form Method", "method", "select", ["post", "get"]);
        break;
      case "text-input":
      case "email-input":
      case "date-input":
        addPropertyInput("Label", "label");
        if (componentType !== "date-input")
          addPropertyInput("Placeholder", "placeholder");
        addPropertyInput("Required", "required", "checkbox");
        addPropertyInput("Error Message", "errorMessage");
        break;
      case "select-input":
      case "radio-group":
      case "checkbox-group":
        addPropertyInput("Label", "label");
        addPropertyInput(
          "Options (Label=Value per line)",
          "options",
          "textarea"
        );
        addPropertyInput("Required", "required", "checkbox");
        if (componentType !== "select-input")
          addPropertyInput("Display Inline", "inline", "checkbox");
        addPropertyInput("Error Message", "errorMessage");
        break;
      case "submit-button":
        addPropertyInput("Button Text", "text");
        const btnClasses = [
          "btn-primary",
          "btn-secondary",
          "btn-success",
          "btn-danger",
          "btn-warning",
          "btn-info",
          "btn-light",
          "btn-dark",
          "btn-link",
        ];
        addPropertyInput("Button Style", "btnClass", "select", btnClasses);
        break;
      case "row-container":
        propertiesPanelContent.insertAdjacentHTML(
          "beforeend",
          "<p><small>Row is a layout container. Add components inside it.</small></p>"
        );
        break;
      default:
        propertiesPanelContent.insertAdjacentHTML(
          "beforeend",
          `<p><small>No specific content properties for ${componentType}.</small></p>`
        );
    }

    // --- Styling Properties (Common) ---
    // Only add styling group if component is not a container meant to be invisible (like row)
    if (componentType !== "row-container") {
      addGroupHeader("Styling");
      addPropertyInput("Background Color", "bgColor", "color");
      addPropertyInput("Text Color", "textColor", "color");
      addPropertyInput("Padding (e.g., 10px, 5px 10px)", "padding");
      addPropertyInput("Margin Top (e.g., 10px)", "marginTop");
      addPropertyInput("Margin Bottom (e.g., 10px)", "marginBottom");
    }

    // --- Helper for adding properties ---
    function addPropertyInput(label, dataKey, type = "text", options = null) {
      const formGroup = document.createElement("div");
      formGroup.classList.add("mb-2");

      const labelEl = document.createElement("label");
      labelEl.textContent = label;
      labelEl.classList.add("form-label");
      // Generate a unique ID for the input for the label's 'for' attribute
      const inputId = `${componentEl.id}-prop-${dataKey}`;
      labelEl.htmlFor = inputId;

      let inputEl;
      const currentValue = componentEl.dataset[dataKey];

      // ... (Input creation logic - mostly same as before, ensure inputId is set) ...
      if (type === "checkbox") {
        formGroup.classList.add("form-check");
        inputEl = document.createElement("input");
        inputEl.type = "checkbox";
        inputEl.classList.add("form-check-input");
        inputEl.id = inputId;
        labelEl.classList.remove("form-label");
        labelEl.classList.add("form-check-label");
        inputEl.checked = currentValue === "true";

        inputEl.addEventListener("change", () => {
          componentEl.dataset[dataKey] = inputEl.checked ? "true" : "false";
          updateComponentVisuals(componentEl);
          saveLayout(); // Save on change
        });
        formGroup.appendChild(inputEl);
        formGroup.appendChild(labelEl); // Label after checkbox
      } else if (type === "textarea") {
        inputEl = document.createElement("textarea");
        inputEl.classList.add("form-control");
        inputEl.rows = 4;
        inputEl.id = inputId;
        inputEl.value = currentValue || "";
        inputEl.addEventListener("input", () => {
          componentEl.dataset[dataKey] = inputEl.value;
          updateComponentVisuals(componentEl);
          saveLayout();
        });
        formGroup.appendChild(labelEl);
        formGroup.appendChild(inputEl);
      } else if (type === "select" && Array.isArray(options)) {
        inputEl = document.createElement("select");
        inputEl.classList.add("form-select");
        inputEl.id = inputId;
        options.forEach((opt) => {
          const optionEl = document.createElement("option");
          if (typeof opt === "object" && opt !== null) {
            optionEl.value = opt.value;
            optionEl.textContent = opt.text;
          } else {
            optionEl.value = opt;
            optionEl.textContent = opt;
          }
          inputEl.appendChild(optionEl);
        });
        inputEl.value = currentValue || "";
        inputEl.addEventListener("change", () => {
          componentEl.dataset[dataKey] = inputEl.value;
          updateComponentVisuals(componentEl);
          saveLayout();
        });
        formGroup.appendChild(labelEl);
        formGroup.appendChild(inputEl);
      } else {
        // text, number, color, url etc.
        inputEl = document.createElement("input");
        inputEl.type = type;
        inputEl.classList.add("form-control");
        inputEl.id = inputId;
        if (type === "color" && !currentValue) {
          inputEl.value = "#000000"; // Default for color picker if empty
        } else {
          inputEl.value = currentValue || "";
        }

        inputEl.addEventListener("input", () => {
          componentEl.dataset[dataKey] = inputEl.value;
          updateComponentVisuals(componentEl);
          saveLayout();
        });
        formGroup.appendChild(labelEl);
        formGroup.appendChild(inputEl);
      }
      propertiesPanelContent.appendChild(formGroup);
    } // end addPropertyInput helper
  } // end displayProperties

  function updateComponentVisuals(componentEl) {
    const type = componentEl.getAttribute("data-component-type");
    const data = componentEl.dataset;

    // --- Apply Common Styles ---
    componentEl.style.backgroundColor = data.bgColor || ""; // Use empty string to revert to CSS default
    componentEl.style.color = data.textColor || "";
    componentEl.style.padding = data.padding || "";
    componentEl.style.marginTop = data.marginTop || "";
    componentEl.style.marginBottom = data.marginBottom || "";

    // --- Update Specific Content/Structure ---
    switch (type) {
      case "row-container":
        // Row container style is applied above, content updated via nesting
        break;
      case "header":
      case "image":
        const img = componentEl.querySelector("img");
        if (img) {
          img.src = data.imgSrc || "";
          img.alt = data.altText || "";
        }
        break;
      case "paragraph":
        const p = componentEl.querySelector("p");
        if (p) p.innerHTML = data.text || "";
        break;
      case "footer":
        const footerP = componentEl.querySelector("p");
        if (footerP) footerP.innerHTML = data.text || "";
        break;
      case "navbar":
        // More complex updates needed for brand, links etc.
        break;
      case "form-container":
        const form = componentEl.querySelector("form");
        if (form) {
          form.action = data.action || "#";
          form.method = data.method || "post";
        }
        break;
      case "text-input":
      case "email-input":
      case "date-input":
        const label = componentEl.querySelector(".form-label");
        const input = componentEl.querySelector("input");
        const errorMsgEl = componentEl.querySelector(".error-message");
        if (label) label.textContent = data.label || "";
        if (input) {
          if (data.placeholder !== undefined && type !== "date-input")
            input.placeholder = data.placeholder;
          input.required = data.required === "true";
        }
        if (errorMsgEl) errorMsgEl.textContent = data.errorMessage || "";
        // Maybe add logic: errorMsgEl.style.display = input.required && !input.value ? 'block' : 'none';
        break;
      case "select-input":
      case "radio-group":
      case "checkbox-group":
        const groupLabel = componentEl.querySelector(".form-label");
        const optionsContainer =
          type === "select-input"
            ? componentEl.querySelector("select")
            : componentEl.querySelector(".options-wrapper");
        const errorMsgGroup = componentEl.querySelector(".error-message");
        if (groupLabel) groupLabel.textContent = data.label || "";

        const optionsRaw = data.options || "";
        const optionsArray = optionsRaw
          .split("\n")
          .map((line) => line.trim())
          .filter((line) => line.includes("="))
          .map((line) => {
            const parts = line.split("=");
            return { text: parts[0].trim(), value: parts[1].trim() };
          });

        if (optionsContainer) {
          optionsContainer.innerHTML = ""; // Clear existing options
          if (type === "select-input") {
            optionsArray.forEach((opt) => {
              optionsContainer.insertAdjacentHTML(
                "beforeend",
                `<option value="${opt.value}">${opt.text}</option>`
              );
            });
            optionsContainer.required = data.required === "true";
          } else {
            // Radio/Checkbox
            const inputType = type === "radio-group" ? "radio" : "checkbox";
            const nameAttr =
              type === "radio-group" ? `${componentEl.id}-radio` : "";
            const isInline = data.inline === "true";
            optionsArray.forEach((opt, index) => {
              const checkDivClass = `form-check ${
                isInline ? "form-check-inline" : ""
              }`;
              const inputId = `${componentEl.id}-${inputType}${index}`;
              const checkHTML = `
                                <div class="${checkDivClass}">
                                  <input class="form-check-input" type="${inputType}" value="${
                opt.value
              }" id="${inputId}" ${nameAttr ? `name="${nameAttr}"` : ""}>
                                  <label class="form-check-label" for="${inputId}">${
                opt.text
              }</label>
                                </div>`;
              optionsContainer.insertAdjacentHTML("beforeend", checkHTML);
            });
          }
        }
        if (errorMsgGroup) errorMsgGroup.textContent = data.errorMessage || "";
        break;
      case "submit-button":
        const button = componentEl.querySelector("button");
        if (button) {
          button.textContent = data.text || "Submit";
          button.className = `btn ${data.btnClass || "btn-primary"}`; // Ensure 'btn' class is always present
        }
        break;
    }
  }

  // --- Event Listeners ---

  // Clicking outside components deselects
  document.addEventListener("click", function (event) {
    const target = event.target;
    // Check if click is outside the preview canvas AND outside the properties panel AND not the delete button
    if (
      !previewCanvas.contains(target) &&
      !propertiesPanelContent
        .closest(".properties-container")
        .contains(target) &&
      target !== deleteButton &&
      !target.closest("button")
    ) {
      if (selectedComponent) {
        selectedComponent.classList.remove("selected");
        selectedComponent = null;
        propertiesPanelContent.innerHTML =
          '<p class="text-muted">Chọn một component trong Preview để chỉnh sửa thuộc tính.</p>';
        deleteButton.style.display = "none";
      }
    } else if (target === previewCanvas) {
      // Click directly on canvas background
      if (selectedComponent) {
        selectedComponent.classList.remove("selected");
        selectedComponent = null;
        propertiesPanelContent.innerHTML =
          '<p class="text-muted">Chọn một component trong Preview để chỉnh sửa thuộc tính.</p>';
        deleteButton.style.display = "none";
      }
    }
  });

  // Delete button
  deleteButton.addEventListener("click", function () {
    if (selectedComponent) {
      const parentContainer = selectedComponent.parentElement;
      parentContainer.removeChild(selectedComponent);
      ensurePlaceholder(
        parentContainer,
        parentContainer.classList.contains("row") ||
          parentContainer.tagName === "FORM"
          ? nestedPlaceholderHTML
          : initialPlaceholderHTML
      );
      selectedComponent = null;
      propertiesPanelContent.innerHTML =
        '<p class="text-muted">Chọn một component trong Preview để chỉnh sửa thuộc tính.</p>';
      deleteButton.style.display = "none";
      saveLayout(); // Save after deleting
    }
  });

  // Export HTML button
  exportHtmlButton.addEventListener("click", function () {
    const previewClone = previewCanvas.cloneNode(true); // Clone to avoid modifying the original

    // Basic Cleanup Attempt (Remove builder-specific artifacts)
    previewClone.querySelectorAll(".preview-component").forEach((el) => {
      el.classList.remove("selected", "preview-component"); // Remove selection and base preview class
      // Remove specific preview classes like 'preview-text-input' if desired
      const typeClass = Array.from(el.classList).find((cls) =>
        cls.startsWith("preview-")
      );
      if (typeClass) el.classList.remove(typeClass);
      // Remove temporary IDs if they aren't needed in output
      // el.removeAttribute('id');
      // Remove data attributes used only by the builder (optional)
      // delete el.dataset.selectableInitialized; ... etc.
      // Remove style attribute if styles should come from CSS file instead (complex)
      // el.removeAttribute('style');
    });
    previewClone
      .querySelectorAll(".sortable-ghost, .sortable-drag")
      .forEach((el) => el.remove()); // Remove SortableJS artifacts
    previewClone
      .querySelectorAll("[data-selectable-initialized]")
      .forEach((el) => delete el.dataset.selectableInitialized); // Remove internal flag
    previewClone
      .querySelectorAll(".placeholder-text")
      .forEach((el) => el.remove()); // Remove placeholders

    // Format HTML slightly (basic indentation)
    // This is very rudimentary, a proper library would be needed for good formatting
    const rawHtml = previewClone.innerHTML;
    // const formattedHtml = formatHtml(rawHtml); // Placeholder for a real formatting function
    htmlOutputTextarea.value = rawHtml; // Use raw HTML for now

    htmlExportModal.show();
  });

  // Copy HTML button in modal
  copyHtmlButton.addEventListener("click", function () {
    htmlOutputTextarea.select();
    try {
      document.execCommand("copy");
      copyHtmlButton.textContent = "Copied!";
      setTimeout(() => {
        copyHtmlButton.textContent = "Copy Code";
      }, 2000);
    } catch (err) {
      console.error("Failed to copy HTML: ", err);
      alert("Failed to copy HTML. Please copy manually.");
    }
  });

  // --- Persistence (localStorage) ---
  function saveLayout() {
    // Clean up before saving: remove selection class
    if (selectedComponent) selectedComponent.classList.remove("selected");
    const layoutHtml = previewCanvas.innerHTML;
    localStorage.setItem(storageKey, layoutHtml);
    // Re-select if needed (optional, might be better to deselect on save)
    // if (selectedComponent) selectedComponent.classList.add('selected');
    console.log("Layout saved.");
  }

  function loadLayout() {
    const savedLayout = localStorage.getItem(storageKey);
    if (savedLayout) {
      previewCanvas.innerHTML = savedLayout;
      // Re-initialize interactivity for loaded components
      previewCanvas.querySelectorAll(".preview-component").forEach((el) => {
        makeComponentSelectable(el);
        // Re-initialize nested sortables
        if (el.matches(".preview-form-container, .preview-row-container")) {
          const nestedTarget = el.querySelector(".row, form");
          const type = el.dataset.componentType;
          if (nestedTarget && type) {
            initializeNestedSortable(nestedTarget, type);
            ensurePlaceholder(nestedTarget, nestedPlaceholderHTML); // Check placeholder
          }
        }
      });
      ensurePlaceholder(previewCanvas, initialPlaceholderHTML); // Check top-level placeholder
      console.log("Layout loaded.");
    } else {
      ensurePlaceholder(previewCanvas, initialPlaceholderHTML); // Ensure placeholder if nothing saved
    }
  }

  // Save button
  saveLayoutButton.addEventListener("click", function () {
    saveLayout();
    // Add visual feedback (optional)
    saveLayoutButton.innerHTML = '<i class="bi bi-check-lg"></i> Saved';
    setTimeout(() => {
      saveLayoutButton.innerHTML = '<i class="bi bi-save"></i> Lưu Layout';
    }, 1500);
  });

  // Clear button
  clearLayoutButton.addEventListener("click", function () {
    if (confirm("Bạn có chắc chắn muốn xóa toàn bộ layout hiện tại không?")) {
      localStorage.removeItem(storageKey);
      previewCanvas.innerHTML = initialPlaceholderHTML; // Reset canvas
      propertiesPanelContent.innerHTML =
        '<p class="text-muted">Chọn một component trong Preview để chỉnh sửa thuộc tính.</p>';
      deleteButton.style.display = "none";
      selectedComponent = null;
      console.log("Layout cleared.");
    }
  });

  // --- Initial Load ---
  loadLayout();
}); // End DOMContentLoaded
