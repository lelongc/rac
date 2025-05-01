/**
 * Renderer Module for GFree English Course Web Builder
 * Renders the data model to the canvas
 */

// Use an IIFE to avoid global namespace pollution
(function () {
  // Reference to the canvas container element
  let canvasContainer = null;

  // Currently selected component
  let selectedComponentId = null;

  /**
   * Initialize the renderer
   */
  function init() {
    // Get the canvas container element
    canvasContainer = document.querySelector(".canvas-container");

    if (!canvasContainer) {
      console.error("Canvas container not found!");
      return;
    }

    // Set up event listeners
    setupEventListeners();

    // Initial rendering
    render();
  }

  /**
   * Set up event listeners for rendering and interaction
   */
  function setupEventListeners() {
    // Listen for model updates
    document.addEventListener("modelUpdated", render);

    // Listen for component selection
    canvasContainer.addEventListener("click", handleComponentClick);

    // Listen for property changes
    document
      .getElementById("properties-panel")
      .addEventListener("change", handlePropertyChange);

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
          const components = window.pageModelManager.getComponents();
          const currentIndex = components.findIndex(
            (comp) => comp.id === componentId
          );

          if (moveUpBtn && currentIndex > 0) {
            window.pageModelManager.moveComponent(
              componentId,
              currentIndex - 1
            );
            notifyModelUpdated();
          } else if (moveDownBtn && currentIndex < components.length - 1) {
            window.pageModelManager.moveComponent(
              componentId,
              currentIndex + 1
            );
            notifyModelUpdated();
          }
        }
      }
    });
  }

  /**
   * Main render function - clears the canvas and renders all components
   */
  function render() {
    if (!canvasContainer) return;

    // Get all components from the model
    const components = window.pageModelManager.getComponents();

    // Clear existing content but keep the structure
    const dropzoneMessage = canvasContainer.querySelector(".dropzone-message");
    canvasContainer.innerHTML = "";

    // If we have no components, show the empty message
    if (components.length === 0) {
      const message = dropzoneMessage || createDropzoneMessage();
      canvasContainer.appendChild(message);
      return;
    }

    // Render each component
    components.forEach((component) => {
      const renderedComponent = renderComponent(component);
      canvasContainer.appendChild(renderedComponent);
    });

    // Restore selection if applicable
    if (selectedComponentId) {
      const selectedElement = document.getElementById(selectedComponentId);
      if (selectedElement) {
        selectComponent(selectedElement);
      } else {
        // If the selected component no longer exists, clear selection
        selectedComponentId = null;
        hidePropertyPanel();
      }
    }
  }

  /**
   * Render a single component to a DOM element
   */
  function renderComponent(component) {
    // Create a wrapper element
    const wrapper = document.createElement("div");
    wrapper.className = `canvas-component canvas-${component.type}`;
    wrapper.id = component.id;

    // Add custom classes if defined
    if (component.classes && component.classes.length > 0) {
      component.classes.forEach((cls) => wrapper.classList.add(cls));
    }

    // Apply inline styles
    wrapper.style.color = component.styles.color || "";
    wrapper.style.backgroundColor = component.styles.backgroundColor || "";

    // Set inner HTML from component template
    wrapper.innerHTML = component.getTemplate();

    // Add component actions (icons for move up/down, delete)
    addComponentActions(wrapper);

    // Mark as selected if this is the currently selected component
    if (component.id === selectedComponentId) {
      wrapper.classList.add("selected");
    }

    return wrapper;
  }

  /**
   * Add control buttons to component (move up/down, delete)
   */
  function addComponentActions(element) {
    const actions = document.createElement("div");
    actions.className = "component-actions";
    actions.innerHTML = `
            <button class="btn btn-sm btn-light move-up" title="Move Up"><i class="bi bi-arrow-up"></i></button>
            <button class="btn btn-sm btn-light move-down" title="Move Down"><i class="bi bi-arrow-down"></i></button>
            <button class="btn btn-sm btn-danger delete" title="Delete"><i class="bi bi-trash"></i></button>
        `;
    element.appendChild(actions);
  }

  /**
   * Create the dropzone message element for empty canvas
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
   * Handle clicks on components in the canvas
   */
  function handleComponentClick(e) {
    // Check if we clicked on a component or one of its children
    const component = e.target.closest(".canvas-component");

    // Ignore clicks on component action buttons
    if (e.target.closest(".component-actions")) {
      return;
    }

    if (component) {
      selectComponent(component);
      e.stopPropagation();
    } else {
      // Clicked on canvas but not on a component - deselect
      deselectAllComponents();
    }
  }

  /**
   * Select a component and show its properties
   */
  function selectComponent(component) {
    // Deselect any previously selected component
    deselectAllComponents();

    // Select this component
    component.classList.add("selected");
    selectedComponentId = component.id;

    // Dispatch an event to notify the properties panel
    document.dispatchEvent(
      new CustomEvent("componentSelected", {
        detail: { componentId: component.id },
      })
    );
  }

  /**
   * Deselect all components
   */
  function deselectAllComponents() {
    const selected = document.querySelectorAll(".canvas-component.selected");
    selected.forEach((el) => el.classList.remove("selected"));
    selectedComponentId = null;

    // Hide the property panel
    hidePropertyPanel();
  }

  /**
   * Show properties of the selected component in the right panel
   */
  function showComponentProperties(componentId) {
    const component = window.pageModelManager.getComponentById(componentId);
    if (!component) return;

    // Hide the "no selection" message
    document.querySelector(".no-selection-message").style.display = "none";

    // Show and populate the properties form
    const propertiesPanel = document.querySelector(".component-properties");
    propertiesPanel.style.display = "block";

    // Set general properties
    document.getElementById("prop-id").value = component.id;
    document.getElementById("prop-class").value = component.classes.join(" ");
    document.getElementById("prop-color").value =
      component.styles.color || "#000000";
    document.getElementById("prop-bg-color").value =
      component.styles.backgroundColor || "#ffffff";

    // Set component-specific properties
    const specificPropsContainer = document.getElementById(
      "specific-props-container"
    );
    specificPropsContainer.innerHTML = component.getPropertyControls();

    // Add event listeners to the newly added form controls
    setupPropertyEventListeners(specificPropsContainer);
  }

  /**
   * Hide the property panel
   */
  function hidePropertyPanel() {
    document.querySelector(".no-selection-message").style.display = "block";
    document.querySelector(".component-properties").style.display = "none";
  }

  /**
   * Set up event listeners for property controls
   */
  function setupPropertyEventListeners(container) {
    // Find all input elements
    const inputs = container.querySelectorAll("input, select, textarea");

    // Add change event listeners
    inputs.forEach((input) => {
      // Skip inputs that already have data-property attribute
      if (input.hasAttribute("data-property")) return;

      // Try to determine the property name from the input id
      let propName = input.id;
      if (propName && propName.startsWith("prop-")) {
        propName = propName.substring(5); // Remove the 'prop-' prefix
        input.setAttribute("data-property", propName);
      }
    });
  }

  /**
   * Handle property changes in the properties panel
   */
  function handlePropertyChange(e) {
    if (!selectedComponentId) return;

    const input = e.target;
    const property = input.getAttribute("data-property");

    if (!property) return;

    // Get value based on input type
    let value;
    if (input.type === "checkbox") {
      value = input.checked;
    } else {
      value = input.value;
    }

    // Special handling for classes
    if (property === "class") {
      const classes = value.split(" ").filter((c) => c.trim() !== "");
      window.pageModelManager.updateComponent(selectedComponentId, { classes });
    }
    // Special handling for nested properties like styles.color
    else if (property.includes(".")) {
      const [parentProp, childProp] = property.split(".");
      const component =
        window.pageModelManager.getComponentById(selectedComponentId);

      if (component && component[parentProp]) {
        component[parentProp][childProp] = value;
        window.pageModelManager.updateComponent(selectedComponentId, {
          [parentProp]: component[parentProp],
        });
      }
    }
    // Handle regular properties
    else {
      window.pageModelManager.updateComponent(selectedComponentId, {
        [property]: value,
      });
    }

    // Re-render to show changes
    notifyModelUpdated();
  }

  /**
   * Delete a component from the model
   */
  function deleteComponent(componentId) {
    // If deleting the selected component, clear selection
    if (componentId === selectedComponentId) {
      selectedComponentId = null;
      hidePropertyPanel();
    }

    window.pageModelManager.removeComponent(componentId);
    notifyModelUpdated();
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
