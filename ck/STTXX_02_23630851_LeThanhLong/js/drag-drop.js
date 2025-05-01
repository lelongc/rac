/**
 * Drag and Drop Logic for GFree English Course Web Builder
 * Enables dragging components from palette to canvas
 * Interacts with the PageModelManager to update the data model
 */

// Wrap all functionality in an IIFE to avoid polluting global scope
(function () {
  // Object to store the currently selected component
  const state = {
    selectedComponent: null,
    draggedComponentType: null,
  };

  // Initialize all drag and drop functionality
  function init() {
    setupDraggableComponents();
    setupDropZone();
    setupComponentSelection();
    setupEventListeners();
  }

  /**
   * Make components in the palette draggable
   */
  function setupDraggableComponents() {
    const draggables = document.querySelectorAll(".draggable-component");

    draggables.forEach((draggable) => {
      // Make the element draggable
      draggable.setAttribute("draggable", "true");

      // Add event listeners for drag start
      draggable.addEventListener("dragstart", handleDragStart);
      draggable.addEventListener("dragend", handleDragEnd);
    });
  }

  /**
   * Set up the canvas area as a drop zone
   */
  function setupDropZone() {
    const dropZone = document.querySelector(".canvas-container");

    // Add event listeners for drop events
    dropZone.addEventListener("dragover", handleDragOver);
    dropZone.addEventListener("dragenter", handleDragEnter);
    dropZone.addEventListener("dragleave", handleDragLeave);
    dropZone.addEventListener("drop", handleDrop);
  }

  /**
   * Set up event handlers for component selection in the canvas
   */
  function setupComponentSelection() {
    const canvas = document.querySelector(".canvas-container");

    // Use event delegation to handle clicks on components
    canvas.addEventListener("click", function (e) {
      // Check if we clicked on a component or one of its children
      const component = e.target.closest(".canvas-component");

      if (component) {
        // Deselect any previously selected component
        const previouslySelected = canvas.querySelector(
          ".canvas-component.selected"
        );
        if (previouslySelected) {
          previouslySelected.classList.remove("selected");
        }

        // Select this component
        component.classList.add("selected");
        state.selectedComponent = component.id;

        // Show component properties in the right panel
        showComponentProperties(component.id);

        // Prevent the click from bubbling up to the canvas
        e.stopPropagation();
      } else {
        // Clicked on canvas but not on a component - deselect all
        deselectAllComponents();
      }
    });
  }

  /**
   * Add additional event listeners for component interaction
   */
  function setupEventListeners() {
    // Listen for property changes
    document
      .getElementById("properties-panel")
      .addEventListener("change", handlePropertyChange);

    // Listen for page model updates
    document.addEventListener("modelUpdated", renderCanvas);

    // Listen for component deletion
    document.addEventListener("click", function (e) {
      if (e.target.closest(".delete")) {
        const component = e.target.closest(".canvas-component");
        if (component) {
          deleteComponent(component.id);
        }
      }
    });

    // Listen for component movement
    document.addEventListener("click", function (e) {
      const moveUpBtn = e.target.closest(".move-up");
      const moveDownBtn = e.target.closest(".move-down");

      if (moveUpBtn || moveDownBtn) {
        const component = e.target.closest(".canvas-component");
        if (component) {
          const componentId = component.id;
          const currentIndex = window.pageModelManager
            .getComponents()
            .findIndex((comp) => comp.id === componentId);

          if (moveUpBtn && currentIndex > 0) {
            window.pageModelManager.moveComponent(
              componentId,
              currentIndex - 1
            );
            notifyModelUpdated();
          } else if (
            moveDownBtn &&
            currentIndex < window.pageModelManager.getComponents().length - 1
          ) {
            window.pageModelManager.moveComponent(
              componentId,
              currentIndex + 1
            );
            notifyModelUpdated();
          }
        }
      }
    });

    // Setup save and preview functionality
    document
      .querySelector("button:has(.bi-save)")
      .addEventListener("click", saveWebsite);
    document
      .querySelector("button:has(.bi-play-fill)")
      .addEventListener("click", previewWebsite);
  }

  // --- Drag Event Handlers ---

  /**
   * Handle the start of a drag operation
   */
  function handleDragStart(e) {
    // Store the component type being dragged
    const componentType = this.getAttribute("data-component");
    state.draggedComponentType = componentType;

    // Set the drag effect and data
    e.dataTransfer.effectAllowed = "copy";
    e.dataTransfer.setData("text/plain", componentType);

    // Add dragging class for visual feedback
    this.classList.add("dragging");
  }

  /**
   * Handle the end of a drag operation
   */
  function handleDragEnd(e) {
    // Remove the dragging class
    this.classList.remove("dragging");
    state.draggedComponentType = null;
  }

  /**
   * Handle drag over event (required to allow dropping)
   */
  function handleDragOver(e) {
    // Prevent default to allow drop
    e.preventDefault();
    e.dataTransfer.dropEffect = "copy";
  }

  /**
   * Handle drag enter event for visual feedback
   */
  function handleDragEnter(e) {
    // Add a class to highlight the drop zone
    this.classList.add("highlight");

    // Hide the initial message when a component is being dragged over
    const dropzoneMessage = this.querySelector(".dropzone-message");
    if (dropzoneMessage) {
      dropzoneMessage.style.display = "none";
    }
  }

  /**
   * Handle drag leave event to remove visual feedback
   */
  function handleDragLeave(e) {
    // Only remove highlight if we're actually leaving the drop zone
    // and not just entering a child element
    if (!this.contains(e.relatedTarget)) {
      this.classList.remove("highlight");

      // Show the message again if there are no components
      const dropzoneMessage = this.querySelector(".dropzone-message");
      if (
        dropzoneMessage &&
        window.pageModelManager.getComponents().length === 0
      ) {
        dropzoneMessage.style.display = "block";
      }
    }
  }

  /**
   * Handle drop event to add a new component to the canvas
   */
  function handleDrop(e) {
    // Prevent the default action
    e.preventDefault();

    // Remove highlight class
    this.classList.remove("highlight");

    // Check if this is a component reordering (internal drag)
    const componentId = e.dataTransfer.getData("componentId");
    if (componentId) {
      // This is handled by the renderer's component reordering logic
      return;
    }

    // Get the component type from the drag data
    const componentType = e.dataTransfer.getData("text/plain");
    if (!componentType) return;

    // Determine drop position (for now, just append to the end)
    const position = null; // This will append to the end

    // Add the component to the model
    const newComponent = window.pageModelManager.addComponent(
      componentType,
      position
    );

    // Notify about the model update
    notifyModelUpdated();

    // Select the newly added component
    setTimeout(() => {
      const componentElement = document.getElementById(newComponent.id);
      if (componentElement) {
        componentElement.click();
      }
    }, 0);
  }

  // --- Component Management Functions ---

  /**
   * Delete a component from the model
   */
  function deleteComponent(componentId) {
    window.pageModelManager.removeComponent(componentId);
    notifyModelUpdated();
  }

  /**
   * Deselect all components in the canvas
   */
  function deselectAllComponents() {
    const selected = document.querySelector(".canvas-component.selected");
    if (selected) {
      selected.classList.remove("selected");
    }
    state.selectedComponent = null;

    // Hide the component properties in the right panel
    document.querySelector(".no-selection-message").style.display = "block";
    document.querySelector(".component-properties").style.display = "none";
  }

  /**
   * Show component properties in the right panel
   */
  function showComponentProperties(componentId) {
    const component = window.pageModelManager.getComponentById(componentId);

    if (!component) {
      return;
    }

    // Update the properties form
    document.querySelector(".no-selection-message").style.display = "none";
    const propertiesPanel = document.querySelector(".component-properties");
    propertiesPanel.style.display = "block";

    // Set general properties
    document.getElementById("prop-id").value = component.id;
    document.getElementById("prop-class").value = component.classes.join(" ");
    document.getElementById("prop-color").value = component.styles.color;
    document.getElementById("prop-bg-color").value =
      component.styles.backgroundColor;

    // Set component-specific properties
    const specificPropsContainer = document.getElementById(
      "specific-props-container"
    );
    specificPropsContainer.innerHTML = component.getPropertyControls();
  }

  /**
   * Handle property change in the properties panel
   */
  function handlePropertyChange(e) {
    const input = e.target;
    const property = input.getAttribute("data-property");

    if (!property || !state.selectedComponent) {
      return;
    }

    let value;
    if (input.type === "checkbox") {
      value = input.checked;
    } else {
      value = input.value;
    }

    const componentId = state.selectedComponent;
    window.pageModelManager.updateComponent(componentId, { [property]: value });

    notifyModelUpdated();
  }

  // --- Rendering Functions ---

  /**
   * Render the canvas based on the current model
   */
  function renderCanvas() {
    const canvas = document.querySelector(".canvas-container");
    const components = window.pageModelManager.getComponents();

    // Clear existing content but keep the dropzone message
    const dropzoneMessage = canvas.querySelector(".dropzone-message");
    canvas.innerHTML = "";

    // If we have no components, show the message
    if (components.length === 0) {
      canvas.appendChild(dropzoneMessage || createDropzoneMessage());
      return;
    }

    // Render each component
    components.forEach((component) => {
      const componentElement = component.render();
      canvas.appendChild(componentElement);
    });

    // Re-select the previously selected component if it still exists
    if (state.selectedComponent) {
      const selectedElement = document.getElementById(state.selectedComponent);
      if (selectedElement) {
        selectedElement.classList.add("selected");
      } else {
        state.selectedComponent = null;
      }
    }
  }

  /**
   * Create the dropzone message element
   */
  function createDropzoneMessage() {
    const message = document.createElement("div");
    message.className = "dropzone-message text-center text-muted py-5";
    message.innerHTML = `
            <i class="bi bi-arrow-left-square fs-1"></i>
            <p class="mt-3">Drag and drop components from the left panel to start building your page</p>
        `;
    return message;
  }

  /**
   * Notify that the model has been updated
   */
  function notifyModelUpdated() {
    document.dispatchEvent(new CustomEvent("modelUpdated"));
  }

  /**
   * Save the current website
   */
  function saveWebsite() {
    const modelJson = window.pageModelManager.saveModel(true);
    localStorage.setItem("gfree-builder-model", modelJson);
    alert("Website saved successfully!");
  }

  /**
   * Preview the current website
   */
  function previewWebsite() {
    // For now, just open a new window and render the components
    const previewWindow = window.open("", "_blank");

    const components = window.pageModelManager.getComponents();

    previewWindow.document.write(`
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Preview - GFree English Course</title>
                <link rel="stylesheet" href="../css/bootstrap.min.css">
            </head>
            <body>
                <div class="container">
                    ${components
                      .map((comp) => comp.render().outerHTML)
                      .join("")}
                </div>
                <script src="../js/bootstrap.bundle.min.js"></script>
            </body>
            </html>
        `);
  }

  /**
   * Load the saved model when available
   */
  function loadSavedModel() {
    const savedModel = localStorage.getItem("gfree-builder-model");
    if (savedModel) {
      window.pageModelManager.loadModel(savedModel);
      notifyModelUpdated();
    }
  }

  // Initialize when DOM is fully loaded
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", () => {
      init();
      loadSavedModel();
    });
  } else {
    init();
    loadSavedModel();
  }
})();
